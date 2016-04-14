#!/usr/local/bin/python
# encoding: utf-8
"""
*Convert MJD to date*

:Author:
    David Young

:Date Created:
    March 26, 2015

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    dat_mjd_to_date [-sf] <mjd>

    -h, --help            show this help message
    -f, --fraction        date fraction fromat
    -s, --sqlDate         sql date format
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import readline
import glob
import pickle
from datetime import datetime
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times
# from ..__init__ import *


def tab_complete(text, state):
    return (glob.glob(text + '*') + [None])[state]


def main(arguments=None):
    """
    *The main function used when ``mjd_to_date.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    # setup the command-line util settings
    su = tools(
        arguments=arguments,
        docString=__doc__,
        logLevel="DEBUG",
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
        '--- STARTING TO RUN THE mjd_to_date.py AT %s' %
        (startTime,))

    # call the worker function
    # x-if-settings-or-database-credientials
    thisDate = mjd_to_date(
        log=log,
        mjd=float(mjd),
        fraction=fractionFlag,
        sqlDate=sqlDateFlag
    )
    print thisDate.get()

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE mjd_to_date.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################


class mjd_to_date():

    """
    *The worker class for the mjd_to_date module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``mjd`` -- mjd
        - ``sqlDate`` -- return sqlDate format
        - ``fraction`` -- return date fraction format

    .. todo::

        - @review: when complete, clean mjd_to_date class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
        self,
        log,
        mjd,
        sqlDate=False,
        fraction=False
    ):
        self.log = log
        log.debug("instansiating a new 'mjd_to_date' object")
        self.mjd = mjd
        self.sqlDate = sqlDate
        self.fraction = fraction

        # xt-self-arg-tmpx

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """
        *get the mjd_to_date object*

        **Return:**
            - ``mjd_to_date``

        .. todo::

            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        if self.fraction:
            return self._get_date_fractions()

        thisDate = self._mjd_to_date()

        if self.sqlDate:
            thisDate = thisDate.replace(" ", "T")

        self.log.info('completed the ``get`` method')
        return thisDate

    def _mjd_to_date(
            self):
        """
        *mjd to date*

        **Key Arguments:**
            # -

        **Return:**
            - None

        .. todo::

            - @review: when complete, clean _mjd_to_date method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_mjd_to_date`` method')

        unixtime = (self.mjd + 2400000.5 - 2440587.5) * 86400.0
        theDate = datetime.utcfromtimestamp(unixtime)
        secs = float(theDate.strftime("%S.%f"))
        secs = """%(secs)05.2f""" % locals()
        if float(secs) == 60.:
            millisec = 1 / (24. * 60 * 60 * 1000)
            unixtime = (self.mjd + 2400000.5 - 2440587.5 + millisec) * 86400.0
            theDate = datetime.utcfromtimestamp(unixtime)
            secs = float(theDate.strftime("%S.%f"))
            secs = """%(secs)05.2f""" % locals()

        theDate = theDate.strftime("%Y-%m-%d %H:%M:") + secs

        self.log.info('completed the ``_mjd_to_date`` method')
        return theDate

    # use the tab-trigger below for new method
    def _get_date_fractions(
            self):
        """
        *get date fractions*

        **Key Arguments:**
            # -

        **Return:**
            - None

        .. todo::

            - @review: when complete, clean _get_date_fractions method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_get_date_fractions`` method')

        unixtime = (self.mjd + 2400000.5 - 2440587.5) * 86400.0
        theDate = datetime.utcfromtimestamp(unixtime)
        dateString = theDate.strftime("%Y:%m:%d:%H:%M:%S")
        (year, month, day, hour, min, sec) = dateString.split(':')
        dayFraction = int(day) + int(hour) / 24.0 + int(min) / \
            (24.0 * 60.0) + int(sec) / (24.0 * 60.0 * 60.0)
        dateFraction = "%s %s %05.2f" % (year, month, dayFraction)

        self.log.info('completed the ``_get_date_fractions`` method')
        return dateFraction

    # use the tab-trigger below for new method
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
