#!/usr/bin/env python
# encoding: utf-8
"""
get_outliers_from_list.py
=========================
:Summary:
    Given a list of data - return a list of the outlier indices

:Author:
    David Young

:Date Created:
    March 13, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    dcu_get_outliers_from_list --pythonList=<pythonList> --sigmaLimit=<sigmaLimit>
    
    -h, --help        show this help message
    -v, --version     show version
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
import __init__ as dcu
import numpy as np


def main(arguments=None):
    """
    The main function used when ``get_outliers_from_list.py`` is run as a single script from the cl, or when installed as a cl command
    """
    ########## IMPORTS ##########
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ## ACTIONS BASED ON WHICH ARGUMENTS ARE RECIEVED ##
    ## PRINT COMMAND-LINE USAGE IF NO ARGUMENTS PASSED
    if arguments == None:
        arguments = docopt(__doc__)

    # x-unpackge-settings-in-main-function
    ## SETUP LOGGER -- DEFAULT TO CONSOLE LOGGER IF NONE PROVIDED IN SETTINGS
    if 'settings' in locals() and "logging settings" in settings:
        log = dl.setup_dryx_logging(
            yaml_file=arguments["--settingsFile"]
        )
    elif "--logger" not in arguments or arguments["--logger"] is None:
        log = dl.console_logger(
            level="WARNING"
        )
        log.debug('logger setup')

    # unpack remaining cl arguments using `exec` to setup the variable names
    # automatically
    for arg, val in arguments.iteritems():
        varname = arg.replace("--", "")
        if isinstance(val, str):
            exec(varname + " = '%s'" % (val,))
        else:
            exec(varname + " = %s" % (val,))
        if arg == "--dbConn":
            dbConn = val
        log.debug('%s = %s' % (varname, val,))

    # x-setup-database-connection-in-main-function

    ## START LOGGING ##
    startTime = dcu.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE get_outliers_from_list.py AT %s' %
        (startTime,))

    pythonList = map(float, pythonList.split(','))
    sigmaLimit = float(sigmaLimit)

    # call the worker function
    # x-if-settings-or-database-credientials
    mean, rms_scatter, outliers = get_outliers_from_list(
        log=log,
        alist=pythonList,
        sigmaLimit=sigmaLimit
    )

    print "The list was: %(pythonList)s" % locals()
    print "Mean value: %(mean)0.2f" % locals()
    print "rms scatter from mean: %(rms_scatter)0.2f" % locals()

    stringList = ""
    for i in outliers:
        thisNum = pythonList[i]
        if len(stringList):
            stringList = """%(stringList)s, %(thisNum)s""" % locals()
        else:
            stringList = """%(thisNum)s""" % locals()
    if len(stringList):
        print "the outliers in this list > %(sigmaLimit)s sigma from the mean are: %(stringList)s" % locals()
    else:
        print "there are no outliers in the list > %(sigmaLimit)s sigma from the mean" % locals()

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE get_outliers_from_list.py AT %s (RUNTIME: %s) --' %
        (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
## LAST MODIFIED : March 12, 2014
## CREATED : March 12, 2014
## AUTHOR : DRYX


def get_outliers_from_list(
        log,
        alist,
        sigmaLimit):
    """get outliers in list

    **Key Arguments:**
        - ``log`` -- logger
        - ``list`` -- list to find outlier in 
        - ``sigmaLimit`` -- the sigma limit beyond which to flag list value as outlier

    **Return:**
        - ``outliers`` -- list of indices at which outliers where found in input list

    **Todo**
        - @review: when complete, clean get_outliers_from_list function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##

    ## LOCAL APPLICATION ##

    log.info('starting the ``get_outliers_from_list`` function')
    ## TEST THE ARGUMENTS
    listArray = np.array(alist)
    mean = np.mean(listArray)

    scatter = []
    for x in listArray:
        scatter.append(np.abs(mean - x))
    scatter = np.array(scatter)

    rms_scatter = np.sqrt(np.mean(scatter ** 2))

    outliers = []
    limit = rms_scatter * sigmaLimit
    for i, v in enumerate(scatter):
        # print """value, limit: %(v)0.2f, %(limit)0.2f""" % locals()
        if v > limit:
            outliers.append(i)

    ## VARIABLES ##

    log.info('completed the ``get_outliers_from_list`` function')
    return mean, rms_scatter, outliers

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
