#!/usr/local/bin/python
# encoding: utf-8
"""
*A collection of functions and classes to help work with csv files*

:Author:
    David Young

:Date Created:
    June 24, 2013

:Notes:
    - If you have any questions requiring this script please email me: davidrobertyoung@gmail.com

.. todo::
    
    - [ ] when complete, extract all code out of the main function and add cl commands
    - [ ] make internal function private
    - [ ] pull all general functions and classes into dryxPythonModules
"""
################# GLOBAL IMPORTS ####################
import sys
import os

######################################################
# MAIN LOOP - USED FOR DEBUGGING OR WHEN SCRIPTING   #
######################################################


def main():
    """
    *The main function used when ``csvtools.py`` run as a single script from the cl*
    """
    ########## PRE-IMPORT SETUP ##########
    relativePathToProjectRoot = "../../../"
    import dryxPython.projectsetup as dps
    projectSetup = dps.projectSetup(
        dbConn=False,
        relativePathToProjectRoot=relativePathToProjectRoot
    )
    global settings, contentPaths
    dbConn, log, settings, contentPaths = projectSetup.get_project_atrributes()

    ########## IMPORTS ##########
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import dryxPython.commonutils as cu

    ## START LOGGING ##
    startTime = cu.get_now_sql_datetime()
    log.info('--- STARTING TO RUN THE csvtools.py AT %s' % (startTime,))

    # SET GLOBAL VARIABLES

    # WRITE CODE HERE

    if dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = cu.get_now_sql_datetime()
    runningTime = cu.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE csvtools.py AT %s (RUNTIME: %s) --' %
        (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : June 14, 2013
# CREATED : June 14, 2013
# AUTHOR : DRYX


def convert_csv_file_to_python_list_of_dictionaries(
        log,
        csvFilePath,
        delimiter="|"):
    """
    *Convert a CSV file to a python list of dictionaries {"columnHeader": "value"}*

    **Key Arguments:**
        - ``log`` -- logger
        - ``csvFilePath`` -- path to the the csv file
        - ``delimiter`` -- the csv delimiter

    **Return:**
        - ``dictionaryList`` -- list of dictionaries containing data from the csv file
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import csv
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ################ >ACTION(S) ################
    try:
        log.debug("attempting to open and read the csv file into a python list")
        with open(csvFilePath, 'rb') as csvFile:
            csvFileContents = csv.reader(csvFile, delimiter=delimiter)
            dictionaryList = []

            headerList = csvFileContents.next()
            # csvFileContents = csvFileContents[1:]

            for row in csvFileContents:
                thisDictionary = {}
                for i in range(len(row)):
                    thisDictionary[headerList[i].strip()] = row[i].strip()
                dictionaryList.append(thisDictionary)

        csvFile.closed
    except Exception, e:
        log.error(
            "could not open and read the csv file into a python list - failed with this error: %s " %
            (str(e),))
        return -1

    return dictionaryList

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

import sqlquery_to_csv_file
