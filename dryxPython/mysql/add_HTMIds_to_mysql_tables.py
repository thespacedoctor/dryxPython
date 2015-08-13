#!/usr/local/bin/python
# encoding: utf-8
"""
add_htmids_to_mysql_table.py
============================
:Summary:
    Give the credientials and the RA and DEC columns, add HTM ids to MySQL table

:Author:
    David Young

:Date Created:
    August 12, 2015

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    dms_add_htmids_to_mysql_table -s <pathToSettingsFile> <tableName> <primaryIdCol> <raCol> <decCol>
    dms_add_htmids_to_mysql_table --host=<host> --user=<user> --passwd=<passwd> --dbName=<dbName> <tableName> <primaryIdCol> <raCol> <decCol>

    -h, --help            show this help message
    -v, --version         show version
    -s, --settings        the settings file
"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
import readline
import glob
import pickle
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil
# from ..__init__ import *


def tab_complete(text, state):
    return (glob.glob(text + '*') + [None])[state]


def main(arguments=None):
    """
    The main function used when ``add_htmids_to_mysql_table.py`` is run as a single script from the cl, or when installed as a cl command
    """
    # setup the command-line util settings
    su = setup_main_clutil(
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
    startTime = dcu.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE add_htmids_to_mysql_table.py AT %s' %
        (startTime,))

    # set options interactively if user requests
    if "interactiveFlag" in locals() and interactiveFlag:

        # load previous settings
        moduleDirectory = os.path.dirname(__file__) + "/resources"
        pathToPickleFile = "%(moduleDirectory)s/previousSettings.p" % locals()
        try:
            with open(pathToPickleFile):
                pass
            previousSettingsExist = True
        except:
            previousSettingsExist = False
        previousSettings = {}
        if previousSettingsExist:
            previousSettings = pickle.load(open(pathToPickleFile, "rb"))

        # x-raw-input
        # x-boolean-raw-input
        # x-raw-input-with-default-value-from-previous-settings

        # save the most recently used requests
        pickleMeObjects = []
        pickleMe = {}
        theseLocals = locals()
        for k in pickleMeObjects:
            pickleMe[k] = theseLocals[k]
        pickle.dump(pickleMe, open(pathToPickleFile, "wb"))

    print locals()

    # call the worker function
    # x-if-settings-or-database-credientials
    add_HTMIds_to_mysql_tables(
        raColName=raCol,
        declColName=decCol,
        tableName=tableName,
        dbConn=dbConn,
        log=log,
        primaryIdColumnName=primaryIdCol
    )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE add_htmids_to_mysql_table.py AT %s (RUNTIME: %s) --' %
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
def add_HTMIds_to_mysql_tables(
        raColName,
        declColName,
        tableName,
        dbConn,
        log,
        primaryIdColumnName="primaryId"):
    """ Calculate and append HTMId info to a mysql db table containing ra and dec columns

    ****Key Arguments:****
        - ``raColName`` -- ra in sexegesimal
        - ``declColName`` -- dec in sexegesimal
        - ``tableName`` -- name of table to add htmid info to
        - ``dbConn`` -- database hosting the above table
        - ``log`` -- logger

    **Return:**
        - ``None`` """

    # # > IMPORTS ##
    import MySQLdb as ms
    import dryxPython.mysql as m
    from dryxPython.kws import utils as u
    # # >SETTINGS ##

    # TEST TABLE EXIST
    sqlQuery = """show tables"""
    rows = m.execute_mysql_read_query(
        sqlQuery=sqlQuery,
        dbConn=dbConn,
        log=log
    )
    tableList = []
    for row in rows:
        tableList.extend(row.values())
    if tableName not in tableList:
        message = "The %s table does not exist in the database" % (tableName,)
        log.critical(message)
        raise IOError(message)

    # TEST COLUMN EXISTS
    cursor = dbConn.cursor(ms.cursors.DictCursor)
    sqlQuery = """SELECT * FROM %s LIMIT 1""" % (tableName,)
    cursor.execute(sqlQuery)
    rows = cursor.fetchall()
    desc = cursor.description
    existingColumns = []
    for i in range(len(desc)):
        existingColumns.append(desc[i][0])
    if (raColName not in existingColumns) or (declColName not in existingColumns):
        message = 'Please make sure you have got the naes of the RA and DEC columns correct'
        log.critical(message)
        raise IOError(message)

    # >ACTION(S)   ###
    htmCols = {
        'htm16ID': 'BIGINT(20)',
        'htm20ID': 'BIGINT(20)',
        'cx': 'DOUBLE',
        'cy': 'DOUBLE',
        'cz': 'DOUBLE',
    }

    # CHECK IF COLUMNS EXISTS YET - IF NOT CREATE FROM
    for key in htmCols.keys():
        try:
            log.debug(
                'attempting to check and generate the HTMId columns for the %s db table' %
                (tableName, ))
            colExists = \
                """SELECT *
                    FROM information_schema.COLUMNS
                    WHERE TABLE_SCHEMA=DATABASE()
                    AND COLUMN_NAME='%s'
                    AND TABLE_NAME='%s'""" \
                % (key, tableName)
            colExists = m.execute_mysql_read_query(
                colExists,
                dbConn,
                log,
            )
            if not colExists:
                sqlQuery = 'ALTER TABLE ' + tableName + ' ADD ' + \
                    key + ' ' + htmCols[key] + ' DEFAULT NULL'
                m.execute_mysql_write_query(
                    sqlQuery,
                    dbConn,
                    log,
                )
        except Exception as e:
            log.critical('could not check and generate the HTMId columns for the %s db table - failed with this error: %s '
                         % (tableName, str(e)))
            return -1
    # SELECT THE ROWS WHERE THE HTMIds ARE NOT SET
    sqlQuery = """SELECT %s, %s, %s from %s where htm16ID is NULL""" % (
        primaryIdColumnName, raColName, declColName, tableName)
    rows = m.execute_mysql_read_query(
        sqlQuery,
        dbConn,
        log,
    )
    # NOW GENERATE THE HTMLIds FOR THESE ROWS
    for row in rows:
        if row[raColName] is None or row[declColName] is None:
            continue
        else:
            (thisRa, thisDec) = (
                float(row[raColName]), float(row[declColName]))
            htm16ID = u.htmID(
                thisRa,
                thisDec,
                16,
            )
            htm20ID = u.htmID(
                thisRa,
                thisDec,
                20,
            )
            (cx, cy, cz) = u.calculate_cartesians(thisRa, thisDec)
            sqlQuery = \
                """UPDATE %s SET htm16ID=%s, htm20ID=%s,cx=%s,cy=%s,cz=%s
                                                    where %s = '%s'""" \
                % (
                tableName,
                htm16ID,
                htm20ID,
                cx,
                cy,
                cz,
                primaryIdColumnName,
                row[primaryIdColumnName],
            )
            try:
                log.debug(
                    'attempting to update the HTMIds for new objects in the %s db table' % (tableName, ))
                m.execute_mysql_write_query(
                    sqlQuery,
                    dbConn,
                    log,
                )
            except Exception as e:
                log.critical('could not update the HTMIds for new objects in the %s db table - failed with this error: %s '
                             % (tableName, str(e)))
                return -1

    # APPLY INDEXES IF NEEDED
    try:
        sqlQuery = u"""
            ALTER TABLE %(tableName)s  ADD INDEX `idx_htm20ID` (`htm20ID` ASC);
            ALTER TABLE %(tableName)s  ADD INDEX `idx_htm16ID` (`htm16ID` ASC);
        """ % locals()
        m.execute_mysql_write_query(
            sqlQuery=sqlQuery,
            dbConn=dbConn,
            log=log
        )
    except Exception, e:
        log.info('no index needed on table: %(e)s' % locals())

    return None

# use the tab-trigger below for new function
# xt-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
