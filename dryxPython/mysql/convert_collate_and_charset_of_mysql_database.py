#!/usr/bin/env python
# encoding: utf-8
"""
convert_collate_and_charset_of_mysql_database.py
================================================
:Summary:
    Convert the Collate of tables within database to `latin1_swedish_ci` and the charset to `latin1`

:Author:
    David Young

:Date Created:
    April 28, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython

# @review Code to be added to the package setup.py file        
# 'dms_convert_collate_and_charset_of_mysql_database=dryxPython.mysql.convert_collate_and_charset_of_mysql_database:main'

Usage:
    dms_convert_collate_and_charset_of_mysql_database -s <settingsFile> -c <charset> -l <collate>
    dms_convert_collate_and_charset_of_mysql_database -s <settingsFile> -c <charset> -l <collate> -t <tableSchema>

    -h, --help          show this help message
    -v, --version       show version
    -s, --settingsFile  path to a yaml settings file
    -t, --tableSchema   the table schema to update (excludes all other table schemas from change)
    -c, --charset       character set for the tables
    -l, --collation     table collation
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil
from . import execute_mysql_write_query
from . import execute_mysql_read_query


def main(arguments=None):
    """
    The main function used when ``convert_collate_and_charset_of_mysql_database.py`` is run as a single script from the cl, or when installed as a cl command
    """
    ########## IMPORTS ##########
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    su = setup_main_clutil(
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
    startTime = dcu.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE convert_collate_and_charset_of_mysql_database.py AT %s' %
        (startTime,))

    if "tableSchema" not in locals():
        tableSchema = False

    # call the worker function
    # x-if-settings-or-database-credientials
    convert_collate_and_charset_of_mysql_database(
        log=log,
        dbConn=dbConn,
        charset=charset,
        collate=collate,
        tableSchema=tableSchema,
    )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE convert_collate_and_charset_of_mysql_database.py AT %s (RUNTIME: %s) --' %
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
def convert_collate_and_charset_of_mysql_database(
        log,
        dbConn,
        charset,
        collate,
        tableSchema=False
):
    """convert_collate_and_charset_of_mysql_database

    **Key Arguments:**
        - ``log`` -- the logger
        - ``dbConn`` -- the database connection

    **Return:**
        - None

    **Todo**
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
        SELECT 
        CONCAT('ALTER TABLE ',
            table_schema,
            '.',
            table_name,
            ' CONVERT TO CHARACTER SET %(charset)s COLLATE %(collate)s;')
        FROM
            information_schema.tables
        WHERE
            1 = 1
        AND table_schema NOT IN ('information_schema' , 'mysql', 'performance_schema')
        %(tableSchema)s 
        and table_name not like '%%view%%'
        and TABLE_COLLATION != '%(collate)s';        
    """ % locals()
    rows = execute_mysql_read_query(
        sqlQuery=sqlQuery,
        dbConn=dbConn,
        log=log
    )

    for row in rows:
        sqlQuery = row.values()[0]
        execute_mysql_write_query(
            sqlQuery=sqlQuery,
            dbConn=dbConn,
            log=log
        )

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
