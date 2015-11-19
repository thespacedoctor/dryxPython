#!/usr/bin/python
# -*- coding: utf-8 -*-
""" **mysql**

**A handful of useful mysql python methods**

| Created by David Young on October 8, 2012
| If you have any questions requiring this script please email me: d.r.young@qub.ac.uk

**dryx syntax**
 | ``xxx`` = come back here and do some more work
 | ``_someObject`` = a 'private' object that should only be changed for debugging

**notes**:
 - Dave started work on this file on October 8, 2012
 - This is a growing repository for Dave's custom MySQL classes and functions """

import sys
import os
import MySQLdb
import time

############################################
# MAIN LOOP - USED FOR DEBUGGING           #
############################################
# def main():
#     import pesstoMarshallPythonPath as pp
#     pp.set_python_path()
#     import dryxPython.mysql as m
#     import pmCommonUtils as p
# SETUP DB CONNECTION AND A LOGGER
#     dbConn, log = p.settings()
#     ## START LOGGING ##
#     log.info('----- STARTING TO RUN THE mysql -----')
# WRITE DEBUG CODE HERE
#     dbConn.commit()
#     dbConn.close()
#     ## FINISH LOGGING ##
#     log.info('----- FINISHED ATTEMPT TO RUN THE mysql -----')
#     return
##########################################################################
# CLASSES                                                                                   #
##########################################################################
############################################
# PUBLIC FUNCTIONS                         #
############################################
############################################
# PRIVATE (HELPER) FUNCTIONS               #
############################################
##########################################################
# DATABASE CONNECTION GIVEN YAML DICTIONARY OF PARAMETERS #
###########################################################


def set_db_connection(pathToYamlFile):
    """Get a database connection using settings in yaml file. Given the location of a YAML dictionary containing database credientials,
    this function will setup and return the connection

    ****Key Arguments:****
        - ``pathToYamlFile`` -- path to the YAML dictionary.

    Returns:
        - ``dbConn`` -- connection to the MySQL database """

    # # IMPORTS ##
    import logging
    import yaml
    import MySQLdb as ms

    import sys
    # # IMPORT THE YAML CONNECTION DICTIONARY ##
    try:
        logging.info(
            'importing the yaml database connection dictionary from ' + pathToYamlFile)
        stream = file(pathToYamlFile, 'r')
        connDict = yaml.load(stream)
    except:
        logging.critical(
            'could not load the connect dictionary from ' + pathToYamlFile)
        sys.exit(1)
    # ESTABLISH A DB CONNECTION
    try:
        logging.info('connecting to the ' + connDict[
                     'db'] + ' database on ' + connDict['host'])
        dbConn = ms.connect(
            host=connDict['host'],
            user=connDict['user'],
            passwd=connDict['password'],
            db=connDict['db'],
            use_unicode=True,
            charset='utf8'
        )
        dbConn.autocommit(True)
    except Exception as e:
        logging.critical('could not connect to the ' + connDict['db'] + ' database on ' + connDict['host'] + ' : '
                         + str(e) + '\n')
    return dbConn


##########################################################################
# EXECUTE A MYSQL WRITE COMMAND GIVEN A QUERY (STRING) AND A DATABASE CONNECTION   #
##########################################################################
# LAST MODIFIED : 20121023
# CREATED : 20121023

def execute_mysql_write_query(
    sqlQuery,
    dbConn,
    log,
    quiet=False,
    Force=False,
    manyValueList=False
):
    """ Execute a MySQL write command given a sql query

            ****Key Arguments:****
                - ``sqlQuery`` -- the MySQL command to execute
                - ``dbConn`` -- the db connection
                - ``Force`` -- do not exit code if error occurs
                - ``manyValueList`` -- a list of value tuples if executing more than one insert

            **Return:**
                - ``None`` """

    # # > IMPORTS ##
    import MySQLdb
    import warnings
    warnings.filterwarnings('error', category=MySQLdb.Warning)
    # ##########################################################
    # >ACTION(S)                                              #
    # ##########################################################
    # CREATE DB CURSOR

    log.debug('starting execute_mysql_write_query')

    message = ""
    try:
        cursor = dbConn.cursor(MySQLdb.cursors.DictCursor)
    except Exception as e:
        log.error('could not create the database cursor.')
    # EXECUTE THE SQL COMMAND
    try:
        if manyValueList == False:
            cursor.execute(sqlQuery)
        else:
            # cursor.executemany(sqlQuery, manyValueList)
            # INSET LARGE LISTS IN BATCHES TO STOP MYSQL SERVER BARFING
            batch = 100000
            offset = 0
            stop = 0
            while stop == 0:
                thisList = manyValueList[offset:offset + batch]
                offset += batch
                a = len(thisList)
                cursor.executemany(sqlQuery, thisList)
                if len(thisList) < batch:
                    stop = 1

    except MySQLdb.Error as e:
        if e[0] == 1050 and 'already exists' in e[1]:
            log.info(str(e) + '\n')
        elif e[0] == 1062:
                           # Duplicate Key error
            log.debug('Duplicate Key error: %s' % (str(e), ))
            message = "duplicate key error"
        elif e[0] == 1061:
                           # Duplicate Key error
            log.debug('index already exists: %s' % (str(e), ))
            message = "index already exists"
        else:
            sqlQueryTrim = sqlQuery[:1000]
            message = 'MySQL write command not executed for this query: << %s >>\nThe error was: %s ' % (sqlQuery,
                                                                                                         str(e))
            if Force == False:
                log.error(message)
                sys.exit(0)
            else:
                log.warning(message)
                return -1
    except Exception as e:
        if "truncated" in str(e):
            log.error('%s\n Here is the sqlquery:\n%s' % (str(e), sqlQuery))
            if manyValueList:
                log.error('... and the values:\n%s' % (thisList, ))
            sys.exit(0)
        else:
            sqlQuery = sqlQuery[:2000]
            log.error(
                'MySQL write command not executed for this query: << %s >>\nThe error was: %s ' %
                (sqlQuery, str(e)))
            if Force == False:
                sys.exit(0)
            return -1
    # CLOSE THE CURSOR
    cOpen = True
    count = 0
    while cOpen:
        try:
            cursor.close()
            cOpen = False
        except Exception as e:
            time.sleep(1)
            count += 1
            if count == 10:
                log.warning('could not close the db cursor ' + str(e) + '\n')
                raise e
                count = 0

    log.debug('finished execute_mysql_write_query')
    return message


##########################################################################
# EXECUTE A MYSQL SELECT COMMAND GIVEN A QUERY (STRING) AND A DATABASE CONNECTION  #
##########################################################################
# LAST MODIFIED : 20121023
# CREATED : 20121023

def execute_mysql_read_query(
    sqlQuery,
    dbConn,
    log,
    quiet=False
):
    """ Execute a MySQL select command given a query

    ****Key Arguments:****
     - ``sqlQuery`` -- the MySQL command to execute
     - ``dbConn`` -- the db connection

    **Return:**
     - ``rows`` -- the rows returned by the sql query """

    # # > IMPORTS ##

    # ##########################################################
    # >ACTION(S)                                              #
    # ##########################################################
    # CREATE DB CURSOR
    try:
        cursor = dbConn.cursor(MySQLdb.cursors.DictCursor)
    except Exception as e:
        log.error('could not create the database cursor: %s' % (e, ))
        raise IOError('could not create the database cursor: %s' % (e, ))
    # EXECUTE THE SQL COMMAND
    try:
        cursor.execute(sqlQuery)
        rows = cursor.fetchall()
    except Exception as e:
        sqlQuery = sqlQuery[:1000]
        if quiet == False:
            log.error(
                'MySQL raised an error - read command not executed.\n' + str(e) + '\nHere is the sqlQuery\n\t%(sqlQuery)s' % locals())
            raise e
    # CLOSE THE CURSOR
    try:
        cursor.close()
    except Exception as e:
        log.warning('could not close the db cursor ' + str(e) + '\n')
    return rows


########################################################################
# GENERATE & POPULATE A MYSQL TABLE FROM DICTIONARY (WRTITEN BY DRYX)  #
########################################################################
# LAST MODIFIED : 20121023
# CREATED : 20121023

def convert_dictionary_to_mysql_table(
        dbConn,
        log,
        dictionary,
        dbTableName,
        uniqueKeyList=[],
        createHelperTables=False,
        dateModified=False,
        returnInsertOnly=False):
    """ Convert a python dictionary into a mysql table

    **Key Arguments:**
        - ``log`` -- logger
        - ``dictionary`` -- python dictionary
        - ``dbConn`` -- the db connection
        - ``dbTableName`` -- name of the table you wish to add the data to (or create if it does not exist)
        - ``uniqueKeyList`` - a lists column names that need combined to create the primary key
        - ``createHelperTables`` -- create some helper tables with the main table, detailing original keywords etc
        - ``returnInsertOnly`` -- returns only the insert command (does not execute it)

    **Return:**
        - ``None`` """

    # # >IMPORTS ##
    import MySQLdb as mdb
    import re
    import yaml
    import time
    import datetime
    from dryxPython import commonutils as dcu
    # import ordereddict as c  # REMOVE WHEN PYTHON 2.7 INSTALLED ON PSDB
    import collections as c
    import dryxPython.mysql as dms

    log.debug('starting convert_dictionary_to_mysql_table')

    if returnInsertOnly == False:
        # TEST THE ARGUMENTS
        if str(type(dbConn).__name__) != "Connection":
            message = 'Please use a valid MySQL DB connection.'
            log.critical(message)
            raise TypeError(message)

        if not isinstance(dictionary, dict):
            message = 'Please make sure "dictionary" argument is a dict type.'
            log.critical(message)
            raise TypeError(message)

        if not isinstance(uniqueKeyList, list):
            message = 'Please make sure "uniqueKeyList" is a list'
            log.critical(message)
            raise TypeError(message)

        for i in uniqueKeyList:
            if i not in dictionary.keys():
                message = 'Please make sure values in "uniqueKeyList" are present in the "dictionary" you are tring to convert'
                log.critical(message)
                raise ValueError(message)

        for k, v in dictionary.iteritems():
            # log.debug('k: %s, v: %s' % (k, v,))
            if isinstance(v, list) and len(v) != 2:
                message = 'Please make sure the list values in "dictionary" 2 items in length'
                log.critical("%s: in %s we have a %s (%s)" %
                             (message, k, v, type(v)))
                raise ValueError(message)
            if isinstance(v, list):
                if not (isinstance(v[0], str) or isinstance(v[0], int) or isinstance(v[0], bool) or isinstance(v[0], float) or isinstance(v[0], long) or isinstance(v[0], datetime.date) or v[0] == None):
                    message = 'Please make sure values in "dictionary" are of an appropriate value to add to the database, must be str, float, int or bool'
                    log.critical("%s: in %s we have a %s (%s)" %
                                 (message, k, v, type(v)))
                    raise ValueError(message)
            else:
                if not (isinstance(v, str) or isinstance(v, int) or isinstance(v, bool) or isinstance(v, float) or isinstance(v, long) or isinstance(v, unicode) or isinstance(v, datetime.date) or v == None):
                    this = type(v)
                    message = 'Please make sure values in "dictionary" are of an appropriate value to add to the database, must be str, float, int or bool : %(k)s is a %(this)s' % locals(
                    )
                    log.critical("%s: in %s we have a %s (%s)" %
                                 (message, k, v, type(v)))
                    raise ValueError(message)

        if not isinstance(createHelperTables, bool):
            message = 'Please make sure "createHelperTables" is a True or False'
            log.critical(message)
            raise TypeError(message)

        # TEST IF TABLE EXISTS
        tableExists = does_mysql_table_exist(dbConn, log, dbTableName)

        # CREATE THE TABLE IF IT DOES NOT EXIST
        if tableExists is False:
            sqlQuery = """
                CREATE TABLE `%(dbTableName)s`
                (`primaryId` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'An internal counter',
                PRIMARY KEY (`primaryId`))
                ENGINE=MyISAM AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
            """ % locals()
            dms.execute_mysql_write_query(
                sqlQuery=sqlQuery,
                dbConn=dbConn,
                log=log
            )

    reFeedParserClass = re.compile('FeedParserDict')
    reDatetime = re.compile('^[0-9]{4}-[0-9]{2}-[0-9]{2}T')
    reTypeTime = re.compile('struct_time')
    qCreateColumn = ''
    formattedKey = ''
    formattedKeyList = []
    myValues = []

    # ADD EXTRA COLUMNS TO THE DICTIONARY
    dictionary['dateCreated'] = [
        str(dcu.get_now_sql_datetime()), "date row was created"]
    if dateModified:
        dictionary['dateModified'] = [
            str(dcu.get_now_sql_datetime()), "date row was modified"]

    # ITERATE THROUGH THE DICTIONARY AND GENERATE THE A TABLE COLUMN WITH THE
    # NAME OF THE KEY, IF IT DOES NOT EXIST
    count = len(dictionary)
    i = 1
    for (key, value) in dictionary.items():
        if (isinstance(value, list) and value[0] is None):
            del dictionary[key]
    # SORT THE DICTIONARY BY KEY
    odictionary = c.OrderedDict(sorted(dictionary.items()))
    for (key, value) in odictionary.iteritems():

        formattedKey = key.replace(" ", "_").replace("-", "_")
        # DEC A KEYWORD IN MYSQL - NEED TO CHANGE BEFORE INGEST
        if formattedKey == "dec":
            formattedKey = "decl"
        if formattedKey == "DEC":
            formattedKey = "DECL"

        formattedKeyList.extend([formattedKey])
        if len(key) > 0:
            # CONVERT LIST AND FEEDPARSER VALUES TO YAML (SO I CAN PASS IT AS A
            # STRING TO MYSQL)
            if isinstance(value, list) and (isinstance(value[0], list) or reFeedParserClass.search(str(type(value[0])))):
                value[0] = yaml.dump(value[0])
                value[0] = str(value[0])
            # REMOVE CHARACTERS THAT COLLIDE WITH MYSQL
            # if type(value[0]) == str or type(value[0]) == unicode:
            #     value[0] = value[0].replace('"', """'""")
            # JOIN THE VALUES TOGETHER IN A LIST - EASIER TO GENERATE THE MYSQL
            # COMMAND LATER
            if isinstance(value, str):
                value = value.replace('\\', '\\\\')
                value = value.replace('"', '\\"')
                try:
                    udata = value.decode("utf-8", "ignore")
                    value = udata.encode("ascii", "ignore")
                except:
                    log.error('cound not decode value %(value)s' % locals())

                # log.debug('udata: %(udata)s' % locals())

            if isinstance(value, unicode):
                value = value.replace('"', '\\"')
                value = value.encode("ascii", "ignore")

            if isinstance(value, list) and isinstance(value[0], unicode):
                myValues.extend(['%s' % value[0].strip()])
            elif isinstance(value, list):
                myValues.extend(['%s' % (value[0], )])
            else:
                myValues.extend(['%s' % (value, )])

            if returnInsertOnly == False:
                # CHECK IF COLUMN EXISTS YET
                colExists = \
                    "SELECT *\
                                    FROM information_schema.COLUMNS\
                                    WHERE TABLE_SCHEMA=DATABASE()\
                                        AND COLUMN_NAME='" \
                    + formattedKey + "'\
                                        AND TABLE_NAME='" + dbTableName + """'"""
                try:
                    # log.debug('checking if the column '+formattedKey+' exists
                    # in the '+dbTableName+' table')
                    rows = execute_mysql_read_query(
                        colExists,
                        dbConn,
                        log,
                    )
                except Exception as e:
                    log.error('something went wrong' + str(e) + '\n')

                # IF COLUMN DOESN'T EXIT - GENERATE IT
                if len(rows) == 0:
                    qCreateColumn = """ALTER TABLE %s ADD %s""" % (
                        dbTableName, formattedKey)
                    if not isinstance(value, list):
                        value = [value]
                    if reDatetime.search(str(value[0])):
                        # log.debug('Ok - a datetime string was found')
                        qCreateColumn += ' datetime DEFAULT NULL'
                    elif formattedKey == 'updated_parsed' or formattedKey == 'published_parsed' or formattedKey \
                            == 'feedName' or formattedKey == 'title':
                        qCreateColumn += ' varchar(100) DEFAULT NULL'
                    elif (isinstance(value[0], str) or isinstance(value[0], unicode)) and len(value[0]) < 30:
                        qCreateColumn += ' varchar(100) DEFAULT NULL'
                    elif (isinstance(value[0], str) or isinstance(value[0], unicode)) and len(value[0]) >= 30 and len(value[0]) < 80:
                        qCreateColumn += ' varchar(100) DEFAULT NULL'
                    elif isinstance(value[0], str) or isinstance(value[0], unicode):
                        columnLength = 450 + len(value[0]) * 2
                        qCreateColumn += ' varchar(' + str(
                            columnLength) + ') DEFAULT NULL'
                    elif isinstance(value[0], int) and abs(value[0]) <= 9:
                        qCreateColumn += ' tinyint DEFAULT NULL'
                    elif isinstance(value[0], int):
                        qCreateColumn += ' int DEFAULT NULL'
                    elif isinstance(value[0], float) or isinstance(value[0], long):
                        qCreateColumn += ' double DEFAULT NULL'
                    elif isinstance(value[0], bool):
                        qCreateColumn += ' tinyint DEFAULT NULL'
                    elif isinstance(value[0], list):
                        qCreateColumn += ' varchar(1024) DEFAULT NULL'
                    else:
                        # log.debug('Do not know what format to add this key in
                        # MySQL - removing from dictionary: %s, %s'
                                 # % (key, type(value[0])))
                        formattedKeyList.pop()
                        myValues.pop()
                        qCreateColumn = None
                    if qCreateColumn:
                        # ADD COMMENT TO GIVE THE ORGINAL KEYWORD IF formatted FOR
                        # MYSQL
                        if key is not formattedKey:
                            qCreateColumn += " COMMENT 'original keyword: " + \
                                key + """'"""
                        # CREATE THE COLUMN IF IT DOES NOT EXIST
                        try:
                            log.info('creating the ' +
                                     formattedKey + ' column in the ' + dbTableName + ' table')
                            message = execute_mysql_write_query(
                                qCreateColumn,
                                dbConn,
                                log,
                            )
                        except Exception as e:
                            # log.debug('qCreateColumn: %s' % (qCreateColumn, ))
                            log.error('could not create the ' + formattedKey + ' column in the ' + dbTableName
                                      + ' table -- ' + str(e) + '\n')

    if returnInsertOnly == False:
        # GENERATE THE INDEX NAME - THEN CREATE INDEX IF IT DOES NOT YET EXIST
        if len(uniqueKeyList):
            for i in range(len(uniqueKeyList)):
                uniqueKeyList[i] = uniqueKeyList[
                    i].replace(" ", "_").replace("-", "_")
                if uniqueKeyList[i] == "dec":
                    uniqueKeyList[i] = "decl"
                if uniqueKeyList[i] == "DEC":
                    uniqueKeyList[i] = "DECL"

            indexName = uniqueKeyList[0].replace(" ", "_").replace("-", "_")
            for i in range(len(uniqueKeyList) - 1):
                indexName += '_' + uniqueKeyList[i + 1]

            indexName = dcu.make_lowercase_nospace(indexName)
            rows = execute_mysql_read_query(
                """SELECT COUNT(*) FROM INFORMATION_SCHEMA.STATISTICS WHERE TABLE_SCHEMA = DATABASE() AND
                                        TABLE_NAME = '"""
                + dbTableName + """' AND INDEX_NAME = '""" +
                indexName + """'""",
                dbConn,
                log,
            )
            exists = rows[0]['COUNT(*)']
            # log.debug('uniqueKeyList: %s' % (uniqueKeyList,))
            if exists == 0:
                if isinstance(uniqueKeyList, list):
                    uniqueKeyList = ','.join(uniqueKeyList)

                addUniqueKey = 'ALTER TABLE ' + dbTableName + \
                    ' ADD unique ' + indexName + """ (""" + uniqueKeyList + ')'
                # log.debug('HERE IS THE COMMAND:'+addUniqueKey)
                message = execute_mysql_write_query(
                    addUniqueKey,
                    dbConn,
                    log,
                )

    if returnInsertOnly == True:
        myKeys = ','.join(formattedKeyList)
        valueString = ("%s, " * len(myValues))[:-2]
        insertCommand = """INSERT IGNORE INTO """ + dbTableName + \
            """ (""" + myKeys + """) VALUES (""" + valueString + """)"""
        mv = []
        mv[:] = [None if m == "None" else m for m in myValues]
        valueTuple = tuple(mv)

        return insertCommand, valueTuple

    # GENERATE THE INSERT COMMAND - IGNORE DUPLICATE ENTRIES
    myKeys = ','.join(formattedKeyList)
    myValues = '" ,"'.join(myValues)
    # log.debug(myValues+" ------ PRESTRIP")
    # REMOVE SOME CONVERSION NOISE
    myValues = myValues.replace('time.struct_time', '')
    myValues = myValues.replace(
        '- !!python/object/new:feedparser.FeedParserDict', '')
    myValues = myValues.replace(
        '!!python/object/new:feedparser.FeedParserDict', '')
    myValues = myValues.replace('dictitems:', '')
    myValues = myValues.replace('dictitems', '')
    myValues = myValues.replace('!!python/unicode:', '')
    myValues = myValues.replace('!!python/unicode', '')
    myValues = myValues.replace('"None"', 'null')
    # log.debug(myValues+" ------ POSTSTRIP")
    addValue = """INSERT IGNORE INTO """ + dbTableName + \
        """ (""" + myKeys + """) VALUES (\"""" + myValues + """\")"""
    # log.debug(addValue)

    message = ""
    try:
        # log.debug('adding new data to the %s table; query: %s' % (dbTableName, addValue))
        message = execute_mysql_write_query(
            addValue,
            dbConn,
            log,
        )

    except Exception as e:
        log.error("could not add new data added to the table '" +
                  dbTableName + "' : " + str(e) + '\n')

    log.debug('finished convert_dictionary_to_mysql_table')

    return message


########################################################################
#  FUNCTION TO SET A FLAG TO A GIVEN VALUE          (WRTITEN BY DRYX)  #
########################################################################
# LAST MODIFIED : 20121105
# CREATED : 20121105

def set_flag(
    dbConn,
    log,
    tableName,
    flagColumn,
    flagValue,
    primaryKeyColumn,
    primaryKeyId,
):
    """ Set a flag in a db table to a given value

            ****Key Arguments:****
                - ``dbConn`` -- db connection
                - ``tableName`` -- db table name
                - ``flagColumn`` -- flag column name
                - ``flagValue`` -- value flag is to be set to
                - ``primaryKeyColumn`` -- primaryKey column name
                - ``primaryKeyId`` -- single id of the row you wish to set the flag for

            **Return:**
                - ``None`` """

    # # > IMPORTS ##
    import dryxPython.mysql as m
    # # >SETTINGS ##
    # ##########################################################
    # >ACTION(S)                                              #
    # ##########################################################
    # CREATE THE MYSQL COMMAND TO UPDATE FLAG
    sqlQuery = 'update ' + tableName + ' set ' + flagColumn + ' = ' + str(flagValue) + ' where ' + primaryKeyColumn \
        + ' = ' + str(primaryKeyId)
    try:
        log.debug('update the ingested flags for ' + tableName)
        m.execute_mysql_write_query(
            sqlQuery,
            dbConn,
            log,
        )
    except Exception as e:
        log.error('cound not update the ingested flags for %s, error: %s' %
                  (tableName, str(e)))
        return -1
    return None


##########################################################################
# LAST MODIFIED : November 23, 2012
# CREATED : November 23, 2012
# AUTHOR : DRYX

def add_column_to_db_table(
    tableName,
    colName,
    colType,
    dbConn,
):
    """ Add a column of agiven name to a database table

            ****Key Arguments:****
                - ``tableName`` -- name of table to add column to
                - ``dbConn`` -- database hosting the above table
                - ``colName`` -- name of the column to add
                - ``colType`` -- type of the column to be added
                - ``default`` -- the default value of the column to be added

            **Return:**
                - ``None`` """

    # ############### > IMPORTS ################
    # ############### >SETTINGS ################
    # ############### >ACTION(S) ################
    colsToAdd = {colName: colType}
    # CHECK IF COLUMN EXISTS YET - IF NOT CREATE IT
    for key in colsToAdd.keys():
        colExists = \
            "SELECT *\
                                FROM information_schema.COLUMNS\
                                WHERE TABLE_SCHEMA=DATABASE()\
                                    AND COLUMN_NAME='" \
            + key + "'\
                                    AND TABLE_NAME='" + tableName + """'"""
        colExists = execute_mysql_read_query(
            colExists,
            dbConn,
            log,
        )
        if not colExists:
            sqlQuery = 'ALTER TABLE ' + tableName + ' ADD ' + \
                key + ' ' + colsToAdd[key] + ' DEFAULT NULL'
            (sqlQuery, dbConn, log)
    return None


# LAST MODIFIED : January 9, 2014
# CREATED : January 9, 2014
# AUTHOR : DRYX


def does_mysql_table_exist(
        dbConn,
        log,
        dbTableName):
    """does mysql table exist

    **Key Arguments:**
        - ``dbConn`` -- mysql database connection
        - ``log`` -- logger
        - ``dbTableName`` -- the database tablename

    **Return:**
        - ``tableExists`` -- True or False

    **Todo**
        - @review: when complete, clean does_mysql_table_exist function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    log.info('starting the ``does_mysql_table_exist`` function')
    # TEST THE ARGUMENTS

    ## VARIABLES ##
    sqlQuery = """
        SELECT count(*)
        FROM information_schema.tables
        WHERE table_name = '%(dbTableName)s'
    """ % locals()
    tableExists = execute_mysql_read_query(
        sqlQuery=sqlQuery,
        dbConn=dbConn,
        log=log
    )

    if tableExists[0]["count(*)"] == 0:
        tableExists = False
    else:
        tableExists = True

    log.info('completed the ``does_mysql_table_exist`` function')
    return tableExists

# LAST MODIFIED : December 11, 2012
# CREATED : December 11, 2012
# AUTHOR : DRYX


def get_db_table_column_names(
    dbConn,
    log,
    dbTable,
):
    """get database table column names

    ****Key Arguments:****
        - ``dbConn`` -- mysql database connection
        - ``log`` -- logger
        - ``dbTable`` -- database tablename

    **Return:**
        - ``columnNames`` -- table column names """

    # ############### > IMPORTS ################
    # ############### > VARIABLE SETTINGS ######
    sqlQuery = """SELECT *
                                FROM %s
                                LIMIT 1""" \
        % (dbTable, )
    # ############### >ACTION(S) ################
    try:
        log.debug('attempting to find column names for dbTable %s' %
                  (dbTable, ))
        rows = execute_mysql_read_query(
            sqlQuery,
            dbConn,
            log,
        )
    except Exception as e:
        log.error(
            'could not find column names for dbTable %s - failed with this error: %s ' %
            (dbTable, str(e)))
        return -1
    columnNames = rows[0].keys()
    return columnNames


# LAST MODIFIED : August 25, 2015
# CREATED : August 25, 2015
# AUTHOR : DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method
def insert_list_of_dictionaries_into_database(
        dbConn,
        log,
        dictList,
        dbTableName,
        uniqueKeyList=[],
        createHelperTables=False,
        dateModified=False,
        batchSize=2500):
    """insert list of dictionaries into database

    **Key Arguments:**
        - ``dbConn`` -- mysql database connection
        - ``log`` -- logger
        # copy usage method(s) here and select the following snippet from the command palette:
        # x-setup-docstring-keys-from-selected-usage-options

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean insert_list_of_dictionaries_into_database function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info(
        'starting the ``insert_list_of_dictionaries_into_database`` function')

    if len(dictList):
        convert_dictionary_to_mysql_table(
            dbConn=dbConn,
            log=log,
            dictionary=dictList[0],
            dbTableName=dbTableName,
            uniqueKeyList=uniqueKeyList,
            createHelperTables=createHelperTables,
            dateModified=dateModified)

    total = len(dictList[1:])
    batches = int(total / batchSize)

    start = 0
    end = 0
    theseBatches = []
    for i in range(batches + 1):
        end = end + batchSize
        start = i * batchSize
        thisBatch = dictList[start:end]
        theseBatches.append(thisBatch)

    totalCount = total
    count = 0

    for batch in theseBatches:
        count += len(batch)
        if count > batchSize:
            # Cursor up one line and clear line
            sys.stdout.write("\x1b[1A\x1b[2K")
        if count > totalCount:
            count = totalCount
        print "%(count)s / %(totalCount)s rows inserted into %(dbTableName)s" % locals()

        inserted = False
        while inserted == False:
            theseInserts = []
            for aDict in batch:
                insertCommand, valueTuple = convert_dictionary_to_mysql_table(
                    dbConn=dbConn,
                    log=log,
                    dictionary=aDict,
                    dbTableName=dbTableName,
                    uniqueKeyList=uniqueKeyList,
                    createHelperTables=createHelperTables,
                    dateModified=dateModified,
                    returnInsertOnly=True
                )
                theseInserts.append(valueTuple)

            message = ""
            # log.debug('adding new data to the %s table; query: %s' % (dbTableName, addValue))
            message = execute_mysql_write_query(
                insertCommand,
                dbConn,
                log,
                Force=False,
                manyValueList=theseInserts
            )
            if message == "unknown column":
                sys.exit(0)
                for aDict in batch:
                    convert_dictionary_to_mysql_table(
                        dbConn=dbConn,
                        log=log,
                        dictionary=aDict,
                        dbTableName=dbTableName,
                        uniqueKeyList=uniqueKeyList,
                        createHelperTables=createHelperTables,
                        dateModified=dateModified
                    )
            else:
                inserted = True

    log.info(
        'completed the ``insert_list_of_dictionaries_into_database`` function')
    return None

# use the tab-trigger below for new function
# xt-def-with-logger


import convert_collate_and_charset_of_mysql_database
import convert_mysql_database_to_innodb
import execute_mysql_script
import add_HTMIds_to_mysql_tables


if __name__ == '__main__':
    main()
