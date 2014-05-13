#!/usr/bin/env python
# encoding: utf-8
"""
sqlquery_to_csv_file.py
=================
:Summary:
    Generate human readable csv data from the data passed in

:Author:
    David Young

:Date Created:
    May 7, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import io
import csv
import re
from decimal import Decimal
from datetime import datetime
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import htmlframework as dhf
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil
from dryxPython import mysql as dms
# from ..__init__ import *

###################################################################
# CLASSES                                                         #
###################################################################
# x-class-module-worker-tmpx
# class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
## LAST MODIFIED : May 7, 2014
## CREATED : May 7, 2014
## AUTHOR : DRYX
def sqlquery_to_csv_file(
        dbConn,
        log,
        sqlQuery,
        csvType="human",
        csvTitle="data exported from database",
        csvFilename="data exported from database.txt",
        returnFormat="plainText"):
    """human readable

    **Key Arguments:**
        - ``dbConn`` -- mysql database connection
        - ``log`` -- logger
        - ``sqlQuery`` -- the sqlQuery to convert to csv
        - ``csvType`` -- "human" or "machine"
        - ``csvTitle`` -- title for the exported data
        - ``csvFilename`` -- the filename for the csv file to be downloaded
        - ``returnFormat`` -- what format to return the data [ plainText | webpage | downloadLink ]

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean sqlquery_to_csv_file function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log.info('starting the ``sqlquery_to_csv_file`` function')
    rows = dms.execute_mysql_read_query(
        sqlQuery=sqlQuery,
        dbConn=dbConn,
        log=log
    )

    tableColumnNames = rows[0].keys()
    columnWidths = []
    columnWidths[:] = [len(tableColumnNames[i])
                       for i in range(len(tableColumnNames))]

    output = io.BytesIO()
    ## setup csv styles
    if csvType == "machine":
        delimiter = ","
    elif csvType == "human":
        delimiter = "|"
    writer = csv.writer(output, dialect='excel', delimiter=delimiter,
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    dividerWriter = csv.writer(output, dialect='excel', delimiter="+",
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)

    ## add column names to csv
    header = []
    divider = []
    allRows = []

    ## clean up data
    for row in rows:
        for c in tableColumnNames:
            if isinstance(row[c], float) or isinstance(row[c], long) or isinstance(row[c], Decimal):
                row[c] = "%6.2f" % row[c]
            elif isinstance(row[c], datetime):
                thisDate = str(row[c])[:10]
                row[c] = "%(thisDate)s" % locals()

    ## set the column widths
    for row in rows:
        for i, c in enumerate(tableColumnNames):
            if len(str(row[c])) > columnWidths[i]:
                columnWidths[i] = len(str(row[c]))

    ## fill in the data
    for row in rows:
        thisRow = []
        ## table border for human readable
        if csvType == "human":
            thisRow.append("")

        for i, c in enumerate(tableColumnNames):
            if csvType == "human":
                row[c] = str(str(row[c]).ljust(columnWidths[i] + 2)
                             .rjust(columnWidths[i] + 3))
            thisRow.append(row[c])
        ## table border for human readable
        if csvType == "human":
            thisRow.append("")
        allRows.append(thisRow)

    ## table borders for human readable
    if csvType == "human":
        header.append("")
        divider.append("")

    for i, c in enumerate(tableColumnNames):
        if csvType == "machine":
            header.append(c)
        elif csvType == "human":
            header.append(
                c.ljust(columnWidths[i] + 2).rjust(columnWidths[i] + 3))
            divider.append('-' * (columnWidths[i] + 3))

    ## table border for human readable
    if csvType == "human":
        header.append("")
        divider.append("")

    if csvType == "machine":
        writer.writerow(header)
    elif csvType == "human":
        dividerWriter.writerow(divider)
        writer.writerow(header)
        dividerWriter.writerow(divider)

    ## write out the data
    writer.writerows(allRows)
    ## table border for human readable
    if csvType == "human":
        dividerWriter.writerow(divider)

    now = datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    output = output.getvalue()
    output = """%(csvTitle)s (exported on %(now)s)\n%(output)s""" % locals(
    )

    now = datetime.now()
    now = now.strftime("%Y%m%dt%H%M%S")

    csvFilename = csvFilename.replace(" ", "_")
    filename = """%(csvFilename)s_%(now)s.txt""" % locals()

    matchObject = re.search(
        r"^(.*)\.(.*)$",
        csvFilename,
        flags=0  # re.S
    )

    if matchObject:
        filename = matchObject.group(1)
        ext = matchObject.group(2)
        filename = """%(filename)s_%(now)s.%(ext)s""" % locals()

    ################ >ACTION(S) ###############
    if returnFormat == "plainText":
        returnOutput = output
    elif returnFormat == "webpageView":
        webpage = dhf.htmlDocument(
            contentType="text/plain",
            content=output
        )
        returnOutput = webpage
    elif returnFormat == "webpageDownload":
        webpage = dhf.htmlDocument(
            contentType="text/plain",
            content=output,
            attachmentSaveAsName=filename
        )
        returnOutput = webpage

    log.info('completed the ``sqlquery_to_csv_file`` function')
    return returnOutput

# use the tab-trigger below for new function
# x-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

############################################
# CODE TO BE DEPECIATED                    #
############################################

if __name__ == '__main__':
    main()

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
