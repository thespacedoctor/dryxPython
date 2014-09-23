#!/usr/local/bin/python
# encoding: utf-8
"""
convert_list_of_urls_to_pdfs.py
===============================
:Summary:
    Convert a list of URLs (from ifttt at the minute) to PDFs

:Author:
    David Young

:Date Created:
    September 22, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    dwc_convert_list_of_urls_to_pdfs -s <pathToSettingsFile>

    -h, --help            show this help message
    -v, --version         show version
    -s, --settings        the settings file
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import string
import codecs
from datetime import datetime, date, time
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil
import pdfkit

# from ..__init__ import *


def main(arguments=None):
    """
    The main function used when ``convert_list_of_urls_to_pdfs.py`` is run as a single script from the cl, or when installed as a cl command
    """
    # setup the command-line util settings
    su = setup_main_clutil(
        arguments=arguments,
        docString=__doc__,
        logLevel="DEBUG"
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
        '--- STARTING TO RUN THE convert_list_of_urls_to_pdfs.py AT %s' %
        (startTime,))

    # call the worker function
    # x-if-settings-or-database-credientials
    convert_list_of_urls_to_pdfs(
        log=log,
        pathToRequestDirectory=settings["urls_to_pdf"]["urlListDirectory"],
        pathToPDFDirectory=settings["urls_to_pdf"]["outputDirectory"]
    )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE convert_list_of_urls_to_pdfs.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################
# xt-class-module-worker-tmpx
# xt-class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : September 22, 2014
# CREATED : September 22, 2014
# AUTHOR : DRYX
def convert_list_of_urls_to_pdfs(
        log,
        pathToRequestDirectory,
        pathToPDFDirectory):
    """convert list of urls to pdfs

    **Key Arguments:**
        - ``log`` -- logger

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean convert_list_of_urls_to_pdfs function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``convert_list_of_urls_to_pdfs`` function')

    # wkhtmltopdf options
    options = {
        'page-size': 'A3'
        # 'margin-top': '0.75in',
        # 'margin-right': '0.75in',
        # 'margin-bottom': '0.75in',
        # 'margin-left': '0.75in',
        # 'encoding': "UTF-8"
    }

    # list the files in the requests directory
    basePath = pathToRequestDirectory
    for d in os.listdir(basePath):
        if os.path.isfile(os.path.join(basePath, d)):
            title = d
            title = title.replace(".txt", "")
            pathToReadFile = os.path.join(basePath, d)
            try:
                log.debug("attempting to open the file %s" % (pathToReadFile,))
                readFile = codecs.open(
                    pathToReadFile, encoding='utf-8', mode='r')
                thisData = readFile.read()
                readFile.close()
            except IOError, e:
                message = 'could not open the file %s' % (pathToReadFile,)
                log.critical(message)
                raise IOError(message)
            readFile.close()

            url = thisData
            log.debug("""URL: %(url)s""" % locals())
            log.debug("""TITLE: %(title)s """ % locals())
            now = datetime.now()
            now = now.strftime("%Y%m%dt%H%M%S")
            outputPath = pathToPDFDirectory + \
                "/%(title)s_%(now)s.pdf" % locals()
            # RECODE INTO ASCII
            url = url.encode("ascii", "ignore")
            outputPath = outputPath.encode("ascii", "ignore")
            pdfkit.from_url(str(url), str(outputPath), options=options)

            exists = os.path.exists(outputPath)
            if exists:
                os.remove(pathToReadFile)
            else:
                log.error('cound not create the %(title)s pdf' % locals())
                source = pathToReadFile
                destination = "%(pathToPDFDirectory)s/%(d)s" % locals()
                try:
                    log.debug("attempting to rename file %s to %s" %
                              (source, destination))
                    os.rename(source, destination)
                except Exception, e:
                    log.error(
                        "could not rename file %s to %s - failed with this error: %s " % (source, destination, str(e),))
                    sys.exit(0)

    log.info('completed the ``convert_list_of_urls_to_pdfs`` function')
    return None

# use the tab-trigger below for new function
# xt-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
