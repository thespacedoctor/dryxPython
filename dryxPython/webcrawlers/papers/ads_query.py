#!/usr/bin/env python
# encoding: utf-8
"""
ads_query.py
============
:Summary:
    Query the ADS database and return data in a sensible format

:Author:
    David Young

:Date Created:
    May 23, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython

# xdocopt-usage-tempx
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
import xml.etree.ElementTree as ET
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu

from fundamentals import tools, times
from ..__init__ import *


def main(arguments=None):
    """
    The main function used when ``ads_query.py`` is run as a single script from the cl, or when installed as a cl command
    """
    ########## IMPORTS ##########
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    su = tools(
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
    startTime = times.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE ads_query.py AT %s' %
        (startTime,))

    # call the worker function
    # x-if-settings-or-database-credientials
    ads_query(
        log=log,
        dbConn=dbConn,
    )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE ads_query.py AT %s (RUNTIME: %s) --' %
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
# LAST MODIFIED : May 23, 2014
# CREATED : May 23, 2014
# AUTHOR : DRYX
def ads_query(
        log,
        queryString=False,
        numberOfResults=5000,
        atels=False,
        cbets=False,
        url=False
):
    """query the ads archive for papers relating to a specific query

    **Key Arguments:**
        - ``log`` -- logger

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean ads_query function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log.info('starting the ``ads_query`` function')

    paperDictionary = {}

    # build the url
    if not url:
        url = """http://adsabs.harvard.edu/cgi-bin/basic_connect?qsearch=%(queryString)s&version=1&sort=NDATE&nr_to_return=%(numberOfResults)s&data_type=SHORT_XML""" % locals(
        )
    urlDoc = singleWebDocumentDownloader(
        url=url,
        downloadDirectory="/tmp",
        log=log,
        timeStamp=1,
        credentials=False
    )

    # download the xml file
    pathToReadFile = urlDoc
    try:
        log.debug("attempting to open the file %s" % (pathToReadFile,))
        readFile = open(pathToReadFile, 'r')
        thisData = readFile.read()
        readFile.close()
    except IOError, e:
        message = 'could not open the file %s' % (pathToReadFile,)
        log.critical(message)
        raise IOError(message)
    readFile.close()

    # remove crap that hinders xml parsing
    # fromstring = thisData.replace(
    #     """<records xmlns="http://ads.harvard.edu/schema/abs/1.1/references" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://ads.harvard.edu/schema/abs/1.1/references http://ads.harvard.edu/schema/abs/1.1/references.xsd" retrieved="182" start="1" selected="182">""", "<records>")

    regex = re.compile(r'<records xmlns.*>')
    thisData = regex.sub("<records>", thisData, count=1)

    pathToWriteFile = urlDoc
    try:
        log.debug("attempting to open the file %s" % (pathToWriteFile,))
        writeFile = open(pathToWriteFile, 'w')
    except IOError, e:
        message = 'could not open the file %s' % (pathToWriteFile,)
        log.critical(message)
        raise IOError(message)
    writeFile.write(thisData)
    writeFile.close()

    # PARSE THE XML
    tree = ET.parse(urlDoc)
    root = tree.getroot()

    for record in root.iter('record'):

        # find paper metadata
        journal = record.find('journal').text
        if not atels and "astronomer's telegram" in journal.lower():
            continue
        if not cbets and "central bureau" in journal.lower():
            continue
        log.debug('journal: %(journal)s' % locals())
        bibcode = record.find('bibcode').text
        log.debug('bibcode: %(bibcode)s' % locals())
        title = record.find('title').text
        log.debug('title: %(title)s' % locals())
        pubdate = record.find('pubdate').text
        log.debug('pubdate: %(pubdate)s' % locals())

        paperDictionary[bibcode] = {}
        paperDictionary[bibcode]["title"] = title
        paperDictionary[bibcode]["pubdate"] = pubdate
        paperDictionary[bibcode]["journal"] = journal

        # find all paper links
        for link in record.findall('link'):
            linkType = link.get('type')
            log.debug('linkType: %(linkType)s' % locals())
            name = link.find('name').text
            log.debug('name: %(name)s' % locals())
            url = link.find('url').text
            log.debug('url: %(url)s' % locals())
            count = link.find('count')
            if count is not None:
                count = count.text
                log.debug('count: %(count)s' % locals())
            else:
                count = 0
            if "abstract" in linkType.lower():
                paperDictionary[bibcode]["abstract_url"] = url
            if "ejournal" in linkType.lower():
                paperDictionary[bibcode]["ejournal_url"] = url
            if "article" in linkType.lower():
                paperDictionary[bibcode]["article_url"] = url
            if "preprint" in linkType.lower():
                paperDictionary[bibcode]["preprint_url"] = url
            if "citations" in linkType.lower():
                paperDictionary[bibcode]["citations_url"] = url
                paperDictionary[bibcode]["citations_count"] = count
            if "refcit" in linkType.lower():
                paperDictionary[bibcode]["refcit_url"] = url
                paperDictionary[bibcode]["refcit_count"] = count

        # find paper authors
        authors = record.findall('author')
        theseAuthors = ""
        if len(authors) > 3:
            total = 3
            append = " et al."
        else:
            total = len(authors)
            append = ""
        for i in range(total):
            theseAuthors = theseAuthors + authors[i].text + "; "
        theseAuthors = theseAuthors[0:-2] + append
        log.debug('authors: %(theseAuthors)s' % locals())
        paperDictionary[bibcode]["authors"] = theseAuthors

    log.info('completed the ``ads_query`` function')
    return paperDictionary

# use the tab-trigger below for new function
# xt-def-with-logger

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
