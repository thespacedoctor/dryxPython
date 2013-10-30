#!/usr/local/bin/python
# encoding: utf-8
"""
csvtools.py
===============
:Summary:
    A collection of functions and classes to help work with csv files

:Author:
    David Young

:Date Created:
    June 24, 2013

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script please email me: d.r.young@qub.ac.uk

:Tasks:
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
    The main function used when ``csvtools.py`` run as a single script from the cl
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

    ## SET GLOBAL VARIABLES

    ## WRITE CODE HERE

    if dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = cu.get_now_sql_datetime()
    runningTime = cu.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE csvtools.py AT %s (RUNTIME: %s) --' % (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
## LAST MODIFIED : June 14, 2013
## CREATED : June 14, 2013
## AUTHOR : DRYX
def convert_csv_file_to_python_list_of_dictionaries(
        log,
        csvFilePath,
        delimiter="|"):
    """Convert a CSV file to a python list of dictionaries {"columnHeader": "value"}

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
        log.error("could not open and read the csv file into a python list - failed with this error: %s " % (str(e),))
        return -1

    return dictionaryList

## LAST MODIFIED : June 21, 2013
## CREATED : June 21, 2013
## AUTHOR : DRYX
def convert_python_list_of_dictionaries_to_csv(
        listOfDictionaries,
        csvFilePath,
        log):
    """Converts a python list of dictionaries into a csv file with header = dictionary keys.

    **Key Arguments:**
        - ``listOfDictionaries`` -- the list of dictionaries { csvHeader : value }
        - ``csvFilePath`` -- the path of the file to export the content to as a csv file
        - ``log`` -- logger

    **Return:**
        - None

    **Todo**
    - [ ] when complete, clean convert_python_module_content_to_autoSnippet_csv function & add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import csv
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log.info('starting the ``convert_python_module_content_to_autoSnippet_csv`` function')
    ## VARIABLES ##

    with open(csvFilePath, 'wb') as csvfile:
        writer = csv.writer(
            csvfile,
            dialect= 'excel'
        )
        if len(listOfDictionaries) > 0:
            writer.writerow(listOfDictionaries[0].keys())
            for dictionary in listOfDictionaries:
                writer.writerow(dictionary.values())
    csvfile.close()

    log.info('completed the ``convert_python_module_content_to_autoSnippet_csv`` function')
    return

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
