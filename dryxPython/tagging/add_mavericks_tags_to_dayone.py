#!/usr/local/bin/python
# encoding: utf-8
"""
*Extract out the tags from a dayone XML file and add them as mavericks tags*

:Author:
    David Young

:Date Created:
    February 25, 2014

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    dt_add_mavericks_tags_to_dayone --pathToDoentry=<pathToDoentry>

    -h, --help              show this help message
    -v, --version           show version
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from . import mavericks


def main(arguments=None):
    """
    *The main function used when ``add_mavericks_tags_to_dayone.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    ########## IMPORTS ##########
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ## ACTIONS BASED ON WHICH ARGUMENTS ARE RECIEVED ##
    # PRINT COMMAND-LINE USAGE IF NO ARGUMENTS PASSED
    if arguments == None:
        arguments = docopt(__doc__)

    # SETUP LOGGER -- DEFAULT TO CONSOLE LOGGER IF NONE PROVIDED IN SETTINGS
    if "--logger" not in arguments or arguments["--logger"] is None:
        log = dl.console_logger(
            level="DEBUG"
        )
        log.debug('logger setup')

    # unpack remaining cl arguments using `exec` to setup the variable names
    # automatically
    for arg, val in arguments.iteritems():
        varname = arg.replace("--", "")
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
        '--- STARTING TO RUN THE add_mavericks_tags_to_dayone.py AT %s' %
        (startTime,))

    # call the worker function
    add_mavericks_tags_to_dayone(
        log=log,
        pathToDoentry=pathToDoentry,
    )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE add_mavericks_tags_to_dayone.py AT %s (RUNTIME: %s) --' %
        (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : February 25, 2014
# CREATED : February 25, 2014
# AUTHOR : DRYX


def add_mavericks_tags_to_dayone(
    log,
    pathToDoentry,
):
    """
    *add_mavericks_tags_to_dayone*

    **Key Arguments:**
        - ``log`` -- the logger
        - ``pathToDoentry`` -- path to the dayone .doentry file

    **Return:**
        - None

    .. todo::

        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    dayOneTags = []

    pathToReadFile = pathToDoentry
    try:
        log.debug("attempting to open the file %s" % (pathToReadFile,))
        readFile = open(pathToReadFile, 'r')
        thisData = readFile.read()
        readFile.close()
    except IOError, e:
        message = 'could not open the file %s' % (pathToReadFile,)
        log.critical(message)
        raise IOError(message)

    log.debug('thisData: %(thisData)s' % locals())

    matchObjects = re.finditer(
        r'<key>Tags</key>\s+<array>(.*)</array>', thisData, flags=re.S)

    for match in matchObjects:
        thisMatch = match.group(1)
        log.debug('match: %(thisMatch)s' % locals())
        tags = re.finditer(
            r'<string>(.*?)</string>',
            match.group(1),
            flags=0  # re.S
        )
        for tag in tags:
            thisTag = tag.group(1)
            dayOneTags.append(thisTag)
            log.info('thisTag: %(thisTag)s' % locals())

    readFile.close()

    tag_file = mavericks.tag_file.tag_file
    tag_file(
        log=log,
        pathToFile=pathToDoentry,
        mode="set",
        tagList=dayOneTags)

    return None

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
