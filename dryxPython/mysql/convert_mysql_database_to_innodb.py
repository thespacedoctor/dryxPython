#!/usr/bin/env python
# encoding: utf-8
"""
*Convert the Collate of tables within database to `latin1_swedish_ci` and the charset to `latin1`*

:Author:
    David Young

:Date Created:
    April 28, 2014

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    dms_convert_mysql_database_to_innodb -s <settingsFile>
    dms_convert_mysql_database_to_innodb -s <settingsFile> -t <tableSchema>

    -h, --help          show this help message
    -v, --version       show version
    -s, --settingsFile  path to a yaml settings file
    -t, --tableSchema   the table schema to update (excludes all other table schemas from change)
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu

from . import execute_mysql_read_query
from . import execute_mysql_write_query


def main(arguments=None):
    """
    *The main function used when ``convert_mysql_database_to_innodb.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    ########## IMPORTS ##########
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    from fundamentals import tools, times

    su = tools(
        arguments=arguments,
        docString=__doc__
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
        '--- STARTING TO RUN THE convert_mysql_database_to_innodb.py AT %s' %
        (startTime,))

    if "tableSchema" not in locals():
        tableSchema = False

    # call the worker function
    # x-if-settings-or-database-credientials
    convert_mysql_database_to_innodb(
        log=log,
        dbConn=dbConn,
        tableSchema=tableSchema,
    )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE convert_mysql_database_to_innodb.py AT %s (RUNTIME: %s) --' %
        (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################
# class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : April 28, 2014
# CREATED : April 28, 2014
# AUTHOR : DRYX
def convert_mysql_database_to_innodb(
        log,
        dbConn,
        tableSchema=False
):
    """
    *convert_mysql_database_to_innodb*

    **Key Arguments:**
        - ``log`` -- the logger
        - ``dbConn`` -- the database connection

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
    if tableSchema:
        tableSchema = """ and table_schema like "%(tableSchema)s%%" """ % locals(
        )
    else:
        tableSchema = ""

    sqlQuery = """
        SELECT CONCAT('ALTER TABLE ',table_schema,'.',table_name,' ENGINE=InnoDB ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;')
            FROM information_schema.tables
            WHERE 1=1
                AND engine = 'MyISAM'
                AND table_schema NOT IN ('information_schema', 'mysql', 'performance_schema') %(tableSchema)s and table_name not like "%%view%%";
    """ % locals()
    rows = execute_mysql_read_query(
        sqlQuery=sqlQuery,
        dbConn=dbConn,
        log=log
    )

    for row in rows:
        sqlQuery = row.values()[0]

        try:
            log.debug("attempting to change table to InnoDB")
            execute_mysql_write_query(
                sqlQuery=sqlQuery,
                dbConn=dbConn,
                log=log,
                Force=True
            )
        except Exception, e:
            log.warning(
                "could not change table to InnoDB - failed with this error: %s " % (str(e),))

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
