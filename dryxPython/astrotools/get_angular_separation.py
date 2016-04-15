#!/usr/local/bin/python
# encoding: utf-8
"""
*Get the angular separation between 2 sets of coordinates*

:Author:
    David Young

:Date Created:
    November 4, 2014

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    dat_get_angular_separation <ra1> <dec1> <ra2> <dec2>

    -h, --help            show this help message
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import math
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times
# from ..__init__ import *


def main(arguments=None):
    """
    *The main function used when ``get_angular_separation.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    # setup the command-line util settings
    su = tools(
        arguments=arguments,
        docString=__doc__,
        logLevel="WARNING",
        options_first=True
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
        '--- STARTING TO RUN THE get_angular_separation.py AT %s' %
        (startTime,))

    # call the worker function
    # x-if-settings-or-database-credientials
    angularSeparation, north, east = get_angular_separation(
        log=log,
        ra1=ra1,
        dec1=dec1,
        ra2=ra2,
        dec2=dec2
    )

    print """%(angularSeparation)6.4f\" (%(north)6.4f\" N, %(east)6.4f\" E)""" % locals()

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE get_angular_separation.py AT %s (RUNTIME: %s) --' %
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
# LAST MODIFIED : November 4, 2014
# CREATED : November 4, 2014
# AUTHOR : DRYX
def get_angular_separation(
        log,
        ra1,
        dec1,
        ra2,
        dec2):
    """
    *get angular separation*

    **Key Arguments:**
        - ``log`` -- logger

    **Return:**
        - None

    .. todo::

        - @review: when complete, clean get_angular_separation function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``get_angular_separation`` function')

    import dryxPython.astrotools as dat

    # constants
    pi = (4 * math.atan(1.0))
    DEG_TO_RAD_FACTOR = pi / 180.0
    RAD_TO_DEG_FACTOR = 180.0 / pi

    # if required, convert coordinates to decimal degrees
    if ':' in str(ra1):
        ra1 = dat.ra_sexegesimal_to_decimal.ra_sexegesimal_to_decimal(ra1)
    if ':' in str(dec1):
        dec1 = dat.declination_sexegesimal_to_decimal.declination_sexegesimal_to_decimal(
            dec1)
    if ':' in str(ra2):
        ra2 = dat.ra_sexegesimal_to_decimal.ra_sexegesimal_to_decimal(ra2)
    if ':' in str(dec2):
        dec2 = dat.declination_sexegesimal_to_decimal.declination_sexegesimal_to_decimal(
            dec2)

    ra1 = float(ra1)
    dec1 = float(dec1)
    ra2 = float(ra2)
    dec2 = float(dec2)

    log.debug("""ra1: `%(ra1)s`""" % locals())
    log.debug("""dec1: `%(dec1)s`""" % locals())
    log.debug("""ra2: `%(ra2)s`""" % locals())
    log.debug("""dec2: `%(dec2)s`""" % locals())

    angularSeparation = None

    aa = (90.0 - dec1) * DEG_TO_RAD_FACTOR
    bb = (90.0 - dec2) * DEG_TO_RAD_FACTOR
    cc = (ra1 - ra2) * DEG_TO_RAD_FACTOR
    one = math.cos(aa) * math.cos(bb)
    two = math.sin(aa) * math.sin(bb) * math.cos(cc)

    # Because acos() returns NaN outside the ranges of -1 to +1
    # we need to check this.  Double precision decimal places
    # can give values like 1.0000000000002 which will throw an
    # exception.

    three = one + two
    if (three > 1.0):
        three = 1.0
    if (three < -1.0):
        three = -1.0

    angularSeparation = math.acos(three) * RAD_TO_DEG_FACTOR * 3600.0

    # Now work out N-S, E-W separations (object 1 relative to 2)
    north = -(dec1 - dec2) * 3600.0
    east = -(ra1 - ra2) * \
        math.cos((dec1 + dec2) * DEG_TO_RAD_FACTOR / 2.) * 3600.0

    log.info('completed the ``get_angular_separation`` function')
    return angularSeparation, north, east

# use the tab-trigger below for new function
# xt-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
