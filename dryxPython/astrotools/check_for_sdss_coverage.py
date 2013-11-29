#!/usr/local/bin/python
# encoding: utf-8
"""
check_for_sdss_coverage.py
==========================
:Summary:
    Command-line tool to check for SDSS coverage

:Author:
    David Young

:Date Created:
    November 22, 2013

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    dat_check_for_sdss_coverage --ra=<ra-in-decimal-degrees> --dec=<dec-in-decimal-degrees>

    -h, --help    show this help message
    -v, --version show version
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu


def main(arguments=None):
    """
    The main function used when ``check_for_sdss_coverage.py`` is run as a single script from the cl, or when installed as a cl command
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
            level="DEBUG"
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
        '--- STARTING TO RUN THE check_for_sdss_coverage.py AT %s' %
        (startTime,))

    # call the worker function
    # x-if-settings-or-database-credientials
    check_for_sdss_coverage(
        log=log,
        raDeg=ra,
        decDeg=dec
    )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE check_for_sdss_coverage.py AT %s (RUNTIME: %s) --' %
        (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
## LAST MODIFIED : November 22, 2013
## CREATED : November 22, 2013
## AUTHOR : DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method


def check_for_sdss_coverage(
        log,
        raDeg,
        decDeg,
        url="http://skyserver.sdss3.org/public/en/tools/search/x_sql.aspx"
):
    """Check an ra and dec for SDSS DR9 image coverage

        **Key Arguments:**
            - ``log`` -- python logger
            - ``raDeg`` -- ra in decimal degrees
            - ``decDeg`` -- dec in decimal degrees

        **Return:**
            - ``match`` -- true or false depending on if in the sdss footprint
    """
    ################ > IMPORTS ################
    import dryxPython.mysql as m

    ################ >SETTINGS ################
    raDeg = float(raDeg)
    decDeg = float(decDeg)

    raUpper = raDeg + 0.001
    raLower = raDeg - 0.001
    declUpper = decDeg + 0.01
    declLower = decDeg - 0.01

    ################ >ACTION(S) ################
    sqlQuery = "SELECT TOP 1 rerun, camcol, field FROM PhotoObj WHERE ra BETWEEN %s and %s AND dec BETWEEN %s and %s" % (
        raLower, raUpper, declLower, declUpper,)
    log.debug('sqlQuery: %s' % (sqlQuery,))
    try:
        log.debug(
            "attempting to determine whether object is in SDSS DR9 footprint")
        result = _query(
            sql=sqlQuery,
            url=url,
            fmt="html",
            log=log)
    except Exception, e:
        log.error(
            "could not determine whether object is in SDSS DR9 footprint - failed with this error %s: " %
            (str(e),))
        return -1

    log.debug('result: %s' % (result,))

    if "No objects have been found" in result:
        match = False
        print "This location is NOT in the SDSS footprint"
    elif "cornsilk" in result:
        match = True
        print "This location IS in the SDSS footprint"
    else:
        match = 999
        print "Not sure if image in SDSS"

    log.debug('sdss match: %s' % (match,))

    return match

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


def _filtercomment(sql):
    "Get rid of comments starting with --"
    import os
    fsql = ''
    for line in sql.split('\n'):
        fsql += line.split('--')[0] + ' ' + os.linesep
    return fsql


def _query(sql, url, fmt, log):
    "Run query and return file object"
    import urllib
    import urllib2
    fsql = _filtercomment(sql)
    params = urllib.urlencode({'cmd': fsql, 'format': fmt})
    log.debug('params %s' % (params,))
    # url = url + '?%s' % params
    req = urllib2.Request(url, params)
    response = urllib2.urlopen(req)
    result = response.read()

    # result = urllib.urlopen(url + '?%s' % params)
    # log.debug('url: %s' % (url,))
    return result

############################################
# CODE TO BE DEPECIATED                    #
############################################
if __name__ == '__main__':
    main()

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
