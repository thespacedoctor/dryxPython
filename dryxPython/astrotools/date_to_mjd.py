#!/usr/local/bin/python
# encoding: utf-8
"""
*Convert a date to an MJD*

:Author:
    David Young

:Date Created:
    February 10, 2015

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    dat_date_to_mjd <date>

    -h, --help            show this help message
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
import readline
import glob
import pickle
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times
# from ..__init__ import *


def tab_complete(text, state):
    return (glob.glob(text + '*') + [None])[state]


def main(arguments=None):
    """
    *The main function used when ``date_to_mjd.py`` is run as a single script from the cl, or when installed as a cl command*
    """
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
        '--- STARTING TO RUN THE date_to_mjd.py AT %s' %
        (startTime,))

    # call the worker function
    # x-if-settings-or-database-credientials
    mjd = date_to_mjd(
        log=log,
        date=date
    )
    print mjd.get()

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE date_to_mjd.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################


class date_to_mjd():

    """
    *The worker class for the date_to_mjd module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``date`` -- date to convert to MJD

    .. todo::

        - @review: when complete, clean date_to_mjd class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
        self,
        log,
        date
    ):
        self.log = log
        log.debug("instansiating a new 'date_to_mjd' object")
        self.date = date

        # xt-self-arg-tmpx

        # Initial Actions
        regex = re.compile(r'\D')
        self.date = regex.sub("", self.date)

        if len(self.date) < 8:
            log.error(
                'cound not convert date to mjd - make sure you have input a valid date' % locals())

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """
        *get the date_to_mjd object*

        **Return:**
            - ``date_to_mjd``

        .. todo::

            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        import time
        mjd = None

        year = self.date[0:4]
        month = self.date[4:6]
        day = self.date[6:8]
        hours = self.date[8:10]
        minutes = self.date[10:12]
        seconds = self.date[12:]

        if not len(hours):
            hours = 0
        if not len(minutes):
            minutes = 0
        if not len(seconds):
            seconds = 0

        t = (int(year), int(month), int(day), int(hours),
             int(minutes), int(seconds), 0, 0, 0)
        unixtime = int(time.mktime(t))
        mjd = unixtime / 86400.0 - 2400000.5 + 2440587.5

        self.log.info('completed the ``get`` method')
        return mjd
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
