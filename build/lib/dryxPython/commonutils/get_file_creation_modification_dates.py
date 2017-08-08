#!/usr/local/bin/python
# encoding: utf-8
"""
*Get the file creation and modification dates*

:Author:
    David Young

:Date Created:
    December 10, 2013

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    get_file_creation_modification_dates --pathToFile=<pathToFile>

    -h, --help    show this help message
    -v, --version show version
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
import __init__ as dcu


def main(arguments=None):
    """
    *The main function used when ``get_file_creation_modification_dates.py`` is run as a single script from the cl, or when installed as a cl command*
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
        '--- STARTING TO RUN THE get_file_creation_modification_dates.py AT %s' %
        (startTime,))

    # call the worker function
    # x-if-settings-or-database-credientials
    dateCreated, dateModified = get_file_creation_modification_dates(
        log=log,
        pathToFile=pathToFile,
    )

    print "Created: %s, Modified: %s" % (dateCreated, dateModified)

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE get_file_creation_modification_dates.py AT %s (RUNTIME: %s) --' %
        (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : December 10, 2013
# CREATED : December 10, 2013
# AUTHOR : DRYX


def get_file_creation_modification_dates(
        log,
        pathToFile,
):
    """
    *get_file_creation_modification_dates*

    **Key Arguments:**
        - ``log`` -- the logger
        - ``pathToFile`` -- pathToFile

    **Return:**
        - ``dateCreated`` and ``dateModified`` -- the date the file was created and last modified

    .. todo::

        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import os
    import datetime
    from time import strftime
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    dateCreated = os.path.getctime(pathToFile)
    dateCreated = datetime.datetime.fromtimestamp(dateCreated)
    dateModified = os.path.getmtime(pathToFile)
    dateModified = datetime.datetime.fromtimestamp(dateModified)

    return dateCreated, dateModified

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
