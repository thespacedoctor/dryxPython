#!/usr/local/bin/python
# encoding: utf-8
"""
*Shift a give set of coordinates North and East*

:Author:
    David Young

:Date Created:
    December 2, 2014

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    dat_shift_coordinates <ra> <dec> <north> <east>

    -h, --help            show this help message
    <ra>                  ra in sexigesimal or decimal degrees
    <dec>                 dec in sexigesimal or decimal degrees
    <north>               move north by this many arcsec
    <east>                move east by this many arcsec
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import readline
import glob
import math
from docopt import docopt

from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times
# from ..__init__ import *


def tab_complete(text, state):
    return (glob.glob(text + '*') + [None])[state]


def main(arguments=None):
    """
    *The main function used when ``shift_coordinates.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    from dryxPython import astrotools as dat
    # setup the command-line util settings
    su = tools(
        arguments=arguments,
        docString=__doc__,
        logLevel="WARNING",
        options_first=False
    )
    arguments, settings, log, dbConn = su.setup()

    # tab completion for raw_input
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(tab_complete)

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
        '--- STARTING TO RUN THE shift_coordinates.py AT %s' %
        (startTime,))

    # set options interactively if user requests
    # if interactiveFlag:
    # x-raw-input
    # x-boolean-raw-input
    #     pass

    # call the worker function
    # x-if-settings-or-database-credientials
    newCoords = shift_coordinates(
        log=log,
        ra=ra,
        dec=dec,
        north=float(north),
        east=float(east)
    )

    raNew, decNew = newCoords.get()

    raSex = dat.ra_to_sex(
        ra=raNew,
        delimiter=':'
    )
    decSex = dat.dec_to_sex(
        dec=decNew,
        delimiter=':'
    )

    print """%(raNew)6.4f, %(decNew)6.4f (%(raSex)s, %(decSex)s)""" % locals()

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE shift_coordinates.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################


class shift_coordinates():

    """
    *The worker class for the shift_coordinates module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``ra`` -- ra in sexigesimal or decimal degrees
        - ``dec`` -- dec in sexigesimal or decimal degrees
        - ``north`` -- north in arcsec
        - ``east`` -- east in arcsec

    .. todo::

        - @review: when complete, clean shift_coordinates class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
            self,
            log,
            ra,
            dec,
            north,
            east,

    ):
        self.log = log
        log.debug("instansiating a new 'shift_coordinates' object")
        self.ra = ra
        self.dec = dec
        self.north = north / 3600.
        self.east = east / 3600.

        # xt-self-arg-tmpx

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes
        # constants
        self.pi = (4 * math.atan(1.0))
        self.DEG_TO_RAD_FACTOR = self.pi / 180.0
        self.RAD_TO_DEG_FACTOR = 180.0 / self.pi

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions
        try:
            self.ra = float(self.ra)
        except:
            self.ra = dat.ra_sexegesimal_to_decimal.ra_sexegesimal_to_decimal(
                ra=self.ra)
        try:
            self.dec = float(self.dec)
        except:
            self.dec = dat.declination_sexegesimal_to_decimal.declination_sexegesimal_to_decimal(
                dec=self.dec)

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """
        *get the shift_coordinates object*

        **Return:**
            - ``shift_coordinates``

        .. todo::

            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        dec2 = self.dec + self.north

        ra2 = self.ra + \
            ((self.east) /
             (math.cos((self.dec + dec2) * self.DEG_TO_RAD_FACTOR / 2.)))

        self.log.info('completed the ``get`` method')
        return ra2, dec2
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx

# xt-class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# xt-worker-def

# use the tab-trigger below for new function
# xt-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
