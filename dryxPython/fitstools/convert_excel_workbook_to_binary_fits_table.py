#!/usr/local/bin/python
# encoding: utf-8
"""
convert_excel_workbook_to_binary_fits_table.py
==============================================
:Summary:
    Convert an excel spreadsheet (with correctly labeled speadsheets) into a FITS binary table

:Author:
    David Young

:Date Created:
    February 10, 2015

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:

Usage:
    dft_convert_excel_workbook_to_binary_fits_table -e <pathToExcelFile> -o <pathToOutputFits>

    -h, --help            show this help message
    -e, --excel           the path to the excel file
    -o, --output          the path to the output fits file
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import readline
import glob
import pickle
import pyfits as pf
import numpy as np
from datetime import datetime, date, time
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil


def tab_complete(text, state):
    return (glob.glob(text + '*') + [None])[state]


def main(arguments=None):
    """
    The main function used when ``convert_excel_workbook_to_binary_fits_table.py`` is run as a single script from the cl, or when installed as a cl command
    """
    # setup the command-line util settings
    su = setup_main_clutil(
        arguments=arguments,
        docString=__doc__,
        logLevel="DEBUG",
        options_first=False
    )
    arguments, settings, log, dbConn = su.setup()

    # unpack remaining cl arguments using `exec` to setup the variable names
    # automatically
    for arg, val in arguments.iteritems():
        if arg[0] == "-":
            varname = arg.replace("-", "") + "Flag"
        else:
            varname = arg.replace("<", "").replace(">", "")
        if isinstance(val, str) or isinstance(val, unicode):
            exec(varname + " = '%s'" % (val,))
        else:
            exec(varname + " = %s" % (val,))
        if arg == "--dbConn":
            dbConn = val
        log.debug('%s = %s' % (varname, val,))

    ## START LOGGING ##
    startTime = dcu.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE convert_excel_workbook_to_binary_fits_table.py AT %s' %
        (startTime,))

    # call the worker function
    fitsFile = convert_excel_workbook_to_binary_fits_table(
        log=log,
        pathToWorkbook=pathToExcelFile,
        pathToOutputFits=pathToOutputFits
    )
    fitsFile.get()

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE convert_excel_workbook_to_binary_fits_table.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################


class convert_excel_workbook_to_binary_fits_table():

    """
    The worker class for the convert_excel_workbook_to_binary_fits_table module

    **Key Arguments:**
        - ``log`` -- logger
        - ``pathToWorkbook`` -- path to the excel workbook
        - ``pathToOutputFits`` -- path to the output fits file

    **Todo**
    """
    # Initialisation

    def __init__(
        self,
        log,
        pathToWorkbook,
        pathToOutputFits
    ):
        self.log = log
        self.pathToWorkbook = pathToWorkbook
        self.pathToOutputFits = pathToOutputFits

        # xt-self-arg-tmpx

        self.log.debug(
            "instansiating a new 'convert_excel_workbook_to_binary_fits_table' object")

        # Variable Data Atrributes
        self.primaryHeaderSheet = None
        self.visibleSheets = []
        self.extHeaderSheets = []
        self.dataTableSheets = []

        # Initial Actions
        # Open the Workbook
        from xlrd import open_workbook, cellname, cellnameabs, colname
        self.wb = open_workbook(self.pathToWorkbook, formatting_info=True)

        # Find the primary header, extension headers and the data tables
        for sheet in self.wb.sheets():
            if sheet.visibility == 0:
                # sheet is visible
                if "primary" in sheet.name.lower() and "header" in sheet.name.lower():
                    self.primaryHeaderSheet = sheet
                if "ext" in sheet.name.lower() and "header" in sheet.name.lower():
                    self.extHeaderSheets.append(sheet)
                if "data" in sheet.name.lower() and "table" in sheet.name.lower():
                    self.dataTableSheets.append(sheet)
                self.visibleSheets.append(sheet)

        # sort the extension headers
        self.extHeaderSheets = list(self.extHeaderSheets)
        self.extHeaderSheets = sorted(
            self.extHeaderSheets, key=lambda x: x.name, reverse=False)

        # sort the data tables
        self.dataTableSheets = list(self.dataTableSheets)
        self.dataTableSheets = sorted(
            self.dataTableSheets, key=lambda x: x.name, reverse=False)

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """get the convert_excel_workbook_to_binary_fits_table object

        **Return:**
            - ``convert_excel_workbook_to_binary_fits_table``

        **Todo**
        """
        self.log.info('starting the ``get`` method')

        # generate the prinary header HDU
        primaryHeader = self._generate_fits_header(
            sheet=self.primaryHeaderSheet, primary=True)
        primHdu = pf.PrimaryHDU(header=primaryHeader, data=None)
        primHdu.verify('fix')

        # generate all the extension headers and the data units (i.e. all binary
        # Table HDUs)
        binaryTableHDUList = []
        for eh, dt in zip(self.extHeaderSheets, self.dataTableSheets):
            # header first
            extensionHeader = self._generate_fits_header(
                sheet=eh, primary=False)
            # then the data
            binaryTableHDU = self._generate_data_table_unit(
                dataSheet=dt, extSheet=eh)
            # attach header and verify
            binaryTableHDU.header = extensionHeader
            binaryTableHDU.verify('fix')
            binaryTableHDUList.append(binaryTableHDU)

        hduList = [primHdu]
        hduList.extend(binaryTableHDUList)
        self.hduList = hduList
        self._write_fits_file()

        self.log.info('completed the ``get`` method')
        return None

    def _generate_fits_header(
            self,
            sheet,
            primary=True):
        """ generate primary fits header

        **Key Arguments:**
            - ``sheet`` -- sheet to generate header from
            - ``primary`` -- is this a primary HDU header?

        **Return:**
            - ``fitsHeader`` -- the header

        **Todo**
        """
        self.log.info('starting the ``_generate_fits_header`` method')

        # GENERATE THE FITS HEADER
        if primary:
            primHdu = pf.PrimaryHDU()
            fitsHeader = primHdu.header
        else:
            fitsHeader = pf.Header()

        # find col indexes for keywords, values and comments (first row in
        # excel)
        for col in range(sheet.ncols):
            if str(sheet.cell(0, col).value).lower() == "keyword":
                keywordIndex = col
            elif str(sheet.cell(0, col).value).lower() == "value":
                valueIndex = col
            elif str(sheet.cell(0, col).value).lower() == "comment":
                commentIndex = col

        # for all remaining rows, grab the header data
        for row in range(1, sheet.nrows):
            # get keyword
            keyword = sheet.cell(row, keywordIndex).value
            # get and tidy value
            value = sheet.cell(row, valueIndex).value
            if ("tindx" in keyword.lower() or "tpric" in keyword.lower()) and value == 1:
                value = True
            if isinstance(value, str) or isinstance(value, unicode):
                value = value.strip()
                if not len(value):
                    continue
                if value == 'T' or value.lower() == 'true':
                    value = True
                elif value == 'F' or value.lower() == 'false':
                    value = False
                elif value.lower() == "%now%":
                    now = datetime.now()
                    now = now.strftime("%Y-%m-%dT%H:%M:%S")
                    value = now
            if isinstance(value, float):
                if value % 1 == 0:
                    value = int(value)
            # get comment
            comment = sheet.cell(row, commentIndex).value

            # create card and add to header
            if isinstance(keyword, unicode):
                keyword = keyword.encode("utf8")
            if isinstance(value, unicode):
                value = value.encode("utf8")
            if isinstance(comment, unicode):
                comment = comment.encode("utf8")

            if keyword in fitsHeader:
                fitsHeader[keyword] = (value, comment)
            else:
                card = pf.Card(keyword, value, comment)
                fitsHeader.append(card)

        self.log.info('completed the ``_generate_fits_header`` method')
        return fitsHeader

    def _write_fits_file(
            self):
        """ write fits file

        **Key Arguments:**

        **Return:**
            - None

        **Todo**
        """
        self.log.info('starting the ``_write_fits_file`` method')

        # build and fix HDU list
        hduList = pf.HDUList(self.hduList)
        hduList.verify("fix")

        # write to file
        hduList.writeto(self.pathToOutputFits, checksum=True, clobber=True)

        self.log.info('completed the ``_write_fits_file`` method')
        return None

    def _generate_data_table_unit(
            self,
            dataSheet,
            extSheet):
        """ generate data table unit

        **Key Arguments:**
            - ``dataSheet`` -- the excel sheet containing the data
            - ``extSheet`` -- sheet containing the extension  data header

        **Return:**
            - ``binTableHdu`` -- the table HDU (pre-header population)

        **Todo**
        """
        self.log.info('starting the ``_generate_data_table_unit`` method')

        # read the format dictionary in from the extension header sheet
        for col in range(extSheet.ncols):
            if str(extSheet.cell(0, col).value).lower() == "keyword":
                keywordIndex = col
            elif str(extSheet.cell(0, col).value).lower() == "value":
                valueIndex = col
            elif str(extSheet.cell(0, col).value).lower() == "comment":
                commentIndex = col

        # read in the column formats from the ext header sheet
        typesDict = {}
        formDict = {}
        nullDict = {}
        for row in range(1, extSheet.nrows):
            for col in range(extSheet.ncols):
                rowKey = extSheet.cell(row, keywordIndex).value
                rowValue = extSheet.cell(row, valueIndex).value
                rowComment = extSheet.cell(row, commentIndex).value
                if "ttype" in rowKey.lower():
                    typesDict[rowValue] = rowKey
                elif "tform" in rowKey.lower():
                    formDict[rowKey] = rowValue
                elif "tnull" in rowKey.lower():
                    if isinstance(rowValue, float):
                        if rowValue % 1 == 0:
                            rowValue = int(rowValue)
                    nullDict[rowKey] = rowValue

        # determine length of data table
        tableLength = 0
        dataSheetName = dataSheet.name
        self.log.debug("""datasheet name: `%(dataSheetName)s`""" % locals())
        print dataSheet.colinfo_map
        for row in range(dataSheet.nrows):
            tableLength = row
            rowBlank = True
            for col in range(dataSheet.ncols):
                if not dataSheet.colinfo_map[col].hidden:
                    if dataSheet.cell_type(row, col) != 0 and dataSheet.cell_type(row, col) != 6:
                        rowBlank = False
                        break
            if rowBlank:
                tableLength = row
                break

        self.log.debug("data sheet tableLength :%(tableLength)s" % locals())

        # read in the column names from the datasheet - create a dictionary of
        masterColDict = {}
        allColumns = []
        for col in range(dataSheet.ncols):
            if not dataSheet.colinfo_map[col].hidden:
                colName = dataSheet.cell(0, col).value
                if not len(colName) or colName not in typesDict:
                    continue
                colValues = []
                for row in range(1, tableLength):
                    cellValue = dataSheet.cell(row, col).value
                    if (isinstance(cellValue, str) or isinstance(cellValue, unicode)) and len(cellValue) == 0:
                        cellValue = None

                    colValues.append(cellValue)
                # FIND TYPE NUMBER
                colType = typesDict[colName]
                colTypeIndex = int(colType.replace("TTYPE", ""))
                colTypeIndex = """TTYPE%(colTypeIndex)05.0f""" % locals()
                colForm = colType.replace("TTYPE", "TFORM")
                colForm = formDict[colForm]
                colNull = colType.replace("TTYPE", "TNULL")
                if colNull in nullDict:
                    colNull = nullDict[colNull]
                else:
                    colNull = None
                colValues = np.array(colValues)
                masterColDict[colTypeIndex] = {"name": colName,
                                               "type": colType, "form": colForm, "array": colValues, "null": colNull}
        # sort masterColDict by keys
        import collections
        omasterColDict = collections.OrderedDict(sorted(masterColDict.items()))
        for k, v in omasterColDict.iteritems():
            try:
                self.log.debug(
                    "attempting to generate the column for the FITS binary table")
                thisColumn = pf.Column(
                    name=v["name"], format=v["form"], array=v["array"], null=v["null"])
            except Exception, e:
                self.log.debug(v["name"])
                self.log.debug(v["form"])
                self.log.debug(v["array"])
                self.log.debug(v["null"])
                self.log.error(
                    "could not generate the column for the FITS binary table - failed with this error: %s " % (str(e),))
                sys.exit(0)

            allColumns.append(thisColumn)
        binTableHdu = pf.BinTableHDU.from_columns(allColumns)

        self.log.info('completed the ``_generate_data_table_unit`` method')

        return binTableHdu

if __name__ == '__main__':
    main()
