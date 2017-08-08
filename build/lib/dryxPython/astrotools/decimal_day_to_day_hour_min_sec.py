#!/usr/local/bin/python
# encoding: utf-8
"""
*Convert decimal day to days hours mins sec*

:Author:
    David Young

:Date Created:
    April 21, 2015

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython

# xdocopt-usage-tempx
"""
################# GLOBAL IMPORTS ####################
import sys
import os
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

    # call the worker function
    # x-if-settings-or-database-credientials
    decimal_day_to_day_hour_min_sec(
        log=log,
    )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE decimal_day_to_day_hour_min_sec.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : April 21, 2015
# CREATED : April 21, 2015
# AUTHOR : DRYX
def decimal_day_to_day_hour_min_sec(
        log,
        daysFloat):
    """
    *decimal day to day hour min sec*

    **Key Arguments:**
        - ``log`` -- logger

    **Return:**
        - None

    .. todo::

        - @review: when complete, clean decimal_day_to_day_hour_min_sec function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``decimal_day_to_day_hour_min_sec`` function')

    daysInt = int(daysFloat)
    hoursFloat = (daysFloat - daysInt) * 24.
    hoursInt = int(hoursFloat)
    minsFloat = (hoursFloat - hoursInt) * 60.
    minsInt = int(minsFloat)
    secFloat = (minsFloat - minsInt) * 60.

    log.info('completed the ``decimal_day_to_day_hour_min_sec`` function')
    return daysInt, hoursInt, minsInt, secFloat

# use the tab-trigger below for new function
# xt-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
