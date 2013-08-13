#!/usr/local/bin/python
# encoding: utf-8
"""
constants
===============
:Summary:
    Some commonly used constants

:Author:
    David Young

:Date Created:
    March 22, 2013

:dryx syntax:
    - ``xxx`` = come back here and do some more work
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script please email me: d.r.young@qub.ac.uk
"""
################# GLOBAL IMPORTS ####################
import sys
import os

######################################################
# MAIN LOOP - USED FOR DEBUGGING OR WHEN SCRIPTING   #
######################################################
def main():
    """one-line summary

    Key Arguments:
        -
        - dbConn -- mysql database connection
        - log -- logger

    Return:
        - None
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import pesstoMarshallPythonPath as pp
    pp.set_python_path()
    import pmCommonUtils as p
    import dryxPython.commonutils as cu

    ################ > SETUP ##################
    ## SETUP DB CONNECTION AND A LOGGER
    dbConn, log = p.settings()
    ## START LOGGING ##
    startTime = cu.get_now_sql_datetime()
    log.info('--- STARTING TO RUN THE constants AT %s' % (startTime,))

    ################ > VARIABLE SETTINGS ######
    ################ >ACTION(S) ###############

    dbConn.commit ()
    dbConn.close ()
    ## FINISH LOGGING ##
    endTime = cu.get_now_sql_datetime()
    runningTime = cu.calculate_time_difference(startTime,endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE constants AT %s (RUNTIME: %s) --' % (endTime,runningTime,))
    return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()


###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
