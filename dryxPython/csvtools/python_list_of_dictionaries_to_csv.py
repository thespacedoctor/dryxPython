#!/usr/local/bin/python
# encoding: utf-8
"""
python_list_of_dictionaries_to_csv.py
=====================================
:Summary:
    Convert a python list of dictionaries to pretty csv output

:Author:
    David Young

:Date Created:
    December 2, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import io
import csv
from decimal import Decimal
from datetime import datetime
import readline
import glob
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times
# from ..__init__ import *


def tab_complete(text, state):
    return (glob.glob(text + '*') + [None])[state]

###################################################################
# CLASSES                                                         #
###################################################################
# xt-class-module-worker-tmpx
# xt-class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : December 2, 2014
# CREATED : December 2, 2014
# AUTHOR : DRYX
def python_list_of_dictionaries_to_csv(
        log,
        datalist,
        csvType="human"):
    """python list of dictionaries to csv

    **Key Arguments:**
        - ``log`` -- logger
        - ``csvType`` -- human or machine

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean python_list_of_dictionaries_to_csv function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``python_list_of_dictionaries_to_csv`` function')

    if not len(datalist):
        return "NO MATCH"

    tableColumnNames = datalist[0].keys()
    columnWidths = []
    columnWidths[:] = [len(tableColumnNames[i])
                       for i in range(len(tableColumnNames))]

    output = io.BytesIO()
    # setup csv styles
    if csvType == "machine":
        delimiter = ","
    elif csvType == "human":
        delimiter = "|"
    writer = csv.writer(output, dialect='excel', delimiter=delimiter,
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    dividerWriter = csv.writer(output, dialect='excel', delimiter="+",
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # add column names to csv
    header = []
    divider = []
    allRows = []

    # clean up data
    for row in datalist:
        for c in tableColumnNames:
            if isinstance(row[c], float) or isinstance(row[c], long) or isinstance(row[c], Decimal):
                row[c] = "%0.4f" % row[c]
            elif isinstance(row[c], datetime):
                thisDate = str(row[c])[:10]
                row[c] = "%(thisDate)s" % locals()

    # set the column widths
    for row in datalist:
        for i, c in enumerate(tableColumnNames):
            if len(str(row[c])) > columnWidths[i]:
                columnWidths[i] = len(str(row[c]))

    # fill in the data
    for row in datalist:
        thisRow = []
        # table border for human readable
        if csvType == "human":
            thisRow.append("")

        for i, c in enumerate(tableColumnNames):
            if csvType == "human":
                row[c] = str(str(row[c]).ljust(columnWidths[i] + 2)
                             .rjust(columnWidths[i] + 3))
            thisRow.append(row[c])
        # table border for human readable
        if csvType == "human":
            thisRow.append("")
        allRows.append(thisRow)

    # table borders for human readable
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

    # table border for human readable
    if csvType == "human":
        header.append("")
        divider.append("")

    if csvType == "machine":
        writer.writerow(header)
    elif csvType == "human":
        dividerWriter.writerow(divider)
        writer.writerow(header)
        dividerWriter.writerow(divider)

    # write out the data
    writer.writerows(allRows)
    # table border for human readable
    if csvType == "human":
        dividerWriter.writerow(divider)

    output = output.getvalue()
    output = output.strip()

    log.info('completed the ``python_list_of_dictionaries_to_csv`` function')
    return output

# use the tab-trigger below for new function
# xt-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
