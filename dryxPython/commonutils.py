#!/usr/local/bin/python
# encoding: utf-8
"""
**commonutils**

A collection of miscellaneous useful utilities

| Initially created by David Young on October 8, 2012
| If you have any questions requiring this script please email me: d.r.young@qub.ac.uk

dryx syntax:
    - ``xxx`` = come back here and do some more work
    - ``_someObject`` = a 'private' object that should only be changed for debugging
"""
############################################
# MAIN LOOP - USED FOR DEBUGGING           #
############################################


def main():
    # print
    # calculate_time_difference("2010-03-15T09:23:24","2013-01-15T05:34:42")
    print get_current_mjd()

    #print get_now_sql_datetime()
    #dryx_mkdir('/Users/Dave/Desktop/shit')
    return


## LAST MODIFIED : November 2012
## CREATED : November 2012
## AUTHOR : DRYX
# class logger():
#     """
#     Uses the settings provided in a YAML dictionary to setup a logger(s) for you python program.
# It is best to place the YAML dictionary somewhere accessable to most
# users - i.e. a folder in the root directory.

#     Variable Attributes:
#         - ``settingsFilePath`` -- the path to the YAML dictionary containing settings for the logger(s)

#     Returns:
#         - ``logger`` -- the logger that can be passed to other functions and classes to be used throughout your program.
#     """
#     ###################### GLOBAL IMPORTS ######################
#     import logging
#     import log.config
#     import yaml
#     ################ PUBLIC VARIABLE ATTRIBUTES ################
#     settingsFilePath = None
#     ############### PRIVATE VARIABLE ATTRIBUTES ###############
#     def __init__(self):
#       pass
#     ############### METHODS ####################################
#     def get_object(self):
#       """
#       Method to *set* and *get* the logger(s)
#       """

#       # IMPORT YAML LOGGING DICTIONARY FROM THE GIVEN PATH
#       log.config.dictConfig(yaml.load(open(self.settingsFilePath, 'r')))
#       # SET THE ROOT LOGGER
#       logger = log.getLogger(__name__)

#       return logger


## LAST MODIFIED : 20121026
## CREATED : 20121026
def get_now_datetime_filestamp():
    """A datetime stamp to be appended to the end of filenames:
        ``YYYYMMDDtHHMMSS``

        **Return:**
            - ``now`` -- current time and date in filename format
    """
    ## > IMPORTS ##
    from datetime import datetime, date, time

    ## >SETTINGS ##

    ###########################################################
    # >ACTION(S)                                              #
    ###########################################################
    now = datetime.now()
    now = now.strftime("%Y%m%dt%H%M%S")

    return now


############################################################################
#  RETURNS A MYSQL STYLE TIMESTAMP (WRTITEN BY DRYX)                        #
############################################################################
## LAST MODIFIED : 20121031
## CREATED : 20121031
def get_now_sql_datetime():
    """A datetime stamp in MySQL format:
        ``YYYY-MM-DDTHH:MM:SS``

        **Return:**
            - ``now`` -- current time and date in MySQL format
    """
    ## > IMPORTS ##
    from datetime import datetime, date, time

    ## >SETTINGS ##
    ###########################################################
    # >ACTION(S)                                              #
    ###########################################################
    now = datetime.now()
    now = now.strftime("%Y-%m-%dT%H:%M:%S")

    return now


######################################################################################################################
## LAST MODIFIED : 20121108
## CREATED : 20121108
## AUTHOR : DRYX
def make_lowercase_nospace(theString):
    """Convert a string to a neatly formated filename type - no space, commas, lowercase etc

            **Key Arguments:**
                - ``theString`` -- the string to be made pretty

            **Return:**
                - ``prettyString`` -- the formatted string
    """
    ################ > IMPORTS ################
    ################ >SETTINGS ################
    ################ >ACTION(S) ################
    x = (theString.replace(" ", "_")).strip()
    x = (x.replace(",", "_")).strip()
    x = x.lower()
    prettyString = x
    return prettyString


###########################################################################
#  GIVEN A URL, EXTRACTS THE FILENAME AFTER THE LAST '/' (WRTITEN BY DRYX)#
###########################################################################
## LAST MODIFIED : 20121031
## CREATED : 20121031
def extract_filename_from_url(log, url):
    """
        get the filename from a URL.
        Will return '*untitled.html*', if no filename is found.

        **Key Arguments:**
            - ``url`` -- the url to extract filename from

        Returns:
            - ``filename`` -- the filename
    """
    ## > IMPORTS ##
    import re
    ## >SETTINGS ##

    ###########################################################
    # >ACTION(S)                                              #
    ###########################################################
    # EXTRACT THE FILENAME FROM THE URL
    try:
        log.debug("extracting filename from url " + url)
        reEoURL = re.compile('([\w\.]*)$')
        filename = reEoURL.findall(url)[0]
        #log.debug(filename)
        if(len(filename) == 0):
            filename = 'untitled.html'
        if not (re.search('\.', filename)):
            filename = filename + '.html'
    except Exception as e:
        log.error("could not extracting filename from url : " + str(e) + "\n")

    return filename


########################################################################################################
#  GIVEN A FILENAME AND A DATE, WILL APPEND A DATE STAMP TO AND RETURN THE FILENAME (WRTITEN BY DRYX)  #
########################################################################################################
## LAST MODIFIED : 20121031
## CREATED : 20121031
def append_now_datestamp_to_filename(log, filename):
    """append the current datestamp to the end of the filename (before the extension).

            **Key Arguments:**
                - ``filename`` -- the filename

            Return:
                - ``dsFilename`` -- datestamped filename
    """
    ## > IMPORTS ##
    ## >SETTINGS ##

    ###########################################################
    # >ACTION(S)                                              #
    ###########################################################
    try:
        #log.debug("appending date stamp to the filename : "+filename)
        sliced = filename.split('.')
        dsFilename = sliced[0] + '_' + get_now_datetime_filestamp()
        if len(sliced) == 2:
            dsFilename += '.' + sliced[1]
        else:
            dsFilename += ".xhtml"
    except Exception as e:
        log.error("could not append date stamp to the filename : " +
                  filename + " : " + str(e) + "\n")

    return dsFilename

## LAST MODIFIED : December 12, 2012
## CREATED : December 12, 2012
## AUTHOR : DRYX


def pretty_date(date):
    """convert date to a relative datetime (e.g. +15m, +2hr, +1w)

    **Key Arguments:**
        - ``date`` -- absolute date

    **Return:**
        - a relative date
    """
    ################ > IMPORTS ################
    from datetime import datetime

    ################ > VARIABLE SETTINGS ######

    ################ >ACTION(S) ################
    diff = datetime.now() - date
    s = diff.seconds
    ###############################
    if diff.days == 1:
            return ' + 1d'
    elif diff.days > 1:
            return ' +{0}d'.format(diff.days)
    elif s <= 1:
            return ' just now'
    elif s < 60:
            return ' +{0}sec'.format(s)
    elif s < 120:
            return ' +1min'
    elif s < 3600:
            return ' +{0}min'.format(s / 60)
    elif s < 7200:
            return ' +1hr'
    else:
            return ' +{0}hr'.format(s / 3600)


## LAST MODIFIED : January 19, 2013
## CREATED : January 19, 2013
## AUTHOR : DRYX


def calculate_time_difference(startDate, endDate):
    """Return the time difference between two dates

    **Key Arguments:**
        - ``startDate`` -- the first date in YYYY-MM-DDTHH:MM:SS format
        - ``endDate`` -- the final date YYYY-MM-DDTHH:MM:SS format

    **Return:**
        - ``diffDate`` -- the difference between the two dates in Y,M,D,h,m,s (string)
    """
    ################ > IMPORTS ################
    from datetime import datetime
    from dateutil import relativedelta

    ################ > VARIABLE SETTINGS ######

    ################ >ACTION(S) ################
    startDate = datetime.strptime(startDate, '%Y-%m-%dT%H:%M:%S')
    endDate = datetime.strptime(endDate, '%Y-%m-%dT%H:%M:%S')
    d = relativedelta.relativedelta(endDate, startDate)

    relTime = ""
    if d.years > 0:
        relTime += str(d.years) + "yrs "
    if d.months > 0:
        relTime += str(d.months) + "mths "
    if d.days > 0:
        relTime += str(d.days) + "dys "
    if d.hours > 0:
        relTime += str(d.hours) + "h "
    if d.minutes > 0:
        relTime += str(d.minutes) + "m "
    if d.seconds > 0:
        relTime += str(d.seconds) + "s"
    ###############################
    return relTime


## LAST MODIFIED : 20121101
## CREATED : 20121101
def dryx_mkdir(log, directoryPath):
    """Create a directory if it does not yet exist

            **Key Arguments:**
                - ``directoryPath`` -- absolute/relative path to required directory

            **Return:**
                - ``None``
    """
    ## > IMPORTS ##
    import os

    ## >SETTINGS ##

    ###########################################################
    # >ACTION(S)                                              #
    ###########################################################
    if not os.path.exists(directoryPath):
        try:
            log.debug('creating the ' + directoryPath + ' d i rectory')
            os.mkdir(directoryPath)
        except Exception as e:
            log.error("could not create the " +
                      directoryPath + " directory" + str(e) + "\n")
    else:
        log.debug(directoryPath + ' directory already exists')

    return None

## LAST MODIFIED : December 10, 2012
## CREATED : December 10, 2012
## AUTHOR : DRYX


def strip_whitespace_from_dictionary_values(log, dictionary):
    """Strip the leading and trailing whitespace from dictionary values and returns the cleaned up dictionary

    **Key Arguments:**
        - ``log`` -- logger
        - ``dictionary`` -- dictionary to be cleaned

    Return:
        - ``dictionary`` -- cleaned dictionary
    """
    ################ > IMPORTS ################

    ################ > VARIABLE SETTINGS ######

    ################ >ACTION(S) ################
    # STRIP LEADING AND TRAILING WHITESPACE
    if(len(dictionary) != 0):
        for k in dictionary.keys():
            if isinstance(dictionary[k].value, basestring):
                try:
                    log.debug(
                        "attempting to strip whitespace from dictionary values")
                    dictionary[k].value = dictionary[k].value.strip()
                except Exception as e:
                    log.error(
                        "could not strip whitespace from dictionary values - failed with this error %s: " % (str(e),))
                    return -1

    return dictionary


## LAST MODIFIED : January 25, 2013
## CREATED : January 25, 2013
## AUTHOR : DRYX
def get_current_mjd():
    """Get the current datetime as MJD

    **Key Arguments:**
        - ``None``

    **Return:**
        - ``MJD`` -- Current datetime as MJD
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    from datetime import datetime
    import time
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ################ > VARIABLE SETTINGS ######

    ################ >ACTION(S) ################
    mjd = None

    now = datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")

    try:
        year, month, day = now[0:10].split('-')
        hours, minutes, seconds = now[11:19].split(':')
        t = (int(year), int(month), int(day), int(
            hours), int(minutes), int(seconds), 0, 0, 0)
        unixtime = int(time.mktime(t))
        mjd = unixtime / 86400.0 - 2400000.5 + 2440587.5
    except ValueError as e:
        mjd = None
        print "String is not in SQL Date format."

    return mjd


## LAST MODIFIED : May 22, 2013
## CREATED : May 22, 2013
## AUTHOR : DRYX
def add_directories_to_path(
        directoryPath,
        log):
    """add a directories to the system path

    **Key Arguments:**
        - ``directoryPath`` -- the path to the directory containing the directories you want to add to the system path
        - ``log`` -- logger

    **Return:**
        - None
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import sys
    import os
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ################ >ACTION(S) ################
    for d in os.listdir(directoryPath):
        fullPath = os.path.join(directoryPath, d)
        if os.path.isdir(os.path.join(directoryPath, d)):
            sys.path.append(fullPath)

    return


## LAST MODIFIED : May 22, 2013
## CREATED : May 22, 2013
## AUTHOR : DRYX
def recusively_add_directories_to_path(
        directoryPath,
        log):
    """add contents of a directory **recusively** to the system path

    **Key Arguments:**
           - ``directoryPath`` -- the path to the directory containing the directories you want to recusively add to the system path

    **Return:**
        - None
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import sys
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ################ >ACTION(S) ################
    # ADD TOP LEVEL DIRS TO PATH
    add_directories_to_path(directoryPath)
    parentDirectoryList = [directoryPath,]

    while len(parentDirectoryList) != 0:
        # print "\n\n len(parentDirectoryList): %s" %
        # (len(parentDirectoryList),)
        childDirList = []
        for parentDir in parentDirectoryList:
            thisDirList = os.listdir(parentDir)
            # print "\n\n thisDirList: %s" % (thisDirList,)
            for d in thisDirList:
                fullPath = os.path.join(parentDir, d)
                if os.path.isdir(fullPath):
                    _add_directories_to_path(fullPath)
                    aDirList = os.listdir(fullPath)
                    childDirList.append(fullPath)
                # print '\n\nchildDirList %s' % (childDirList,)
        parentDirectoryList = childDirList

    return


## LAST MODIFIED : June 21, 2013
## CREATED : June 21, 2013
## AUTHOR : DRYX
def get_python_module_partials(
        pathToModuleFile,
        log):
    """Get the names of the _partials imported into dryx python modules.

    **Key Arguments:**
        - ``pathToModuleFile`` -- the path to the python module we wish to extract the _partial names for
        - ``log`` -- logger

    **Return:**
        - ``partialsDictionary`` -- a dictionary of the _partial names imported into the dryx python module, and a list of their functions

    **Todo**
    - [ ] when complete, clean get_python_module_partials function & add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    from modulefinder import ModuleFinder
    import re
    import os
    import sys
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log.info('starting the ``get_python_module_partials`` function')
    ## VARIABLES ##
    partialsDictionary = {}

    finder = ModuleFinder()
    finder.run_script(pathToModuleFile)

    baseName = os.path.basename(pathToModuleFile).replace(".py", "")

    if baseName == "__init__":
        pathToModuleFile = pathToModuleFile.replace("__init__.py","")
        baseName = os.path.basename(pathToModuleFile)

    reBaseName = re.compile(r"%s" % (baseName,))

    for name, mod in finder.modules.iteritems():
        if reBaseName.search(name):
            importList = []
            for key in mod.globalnames.keys():
                # if ("/Library/Frameworks/Python.framework/" in mod.__file__ or "macports" in mod.__file__) and "site-packages" not in mod.__file__:
                if "/Users/" not in mod.__file__:
                    # print "skipping %s" % (mod.__file__,)
                    continue
                importList.append(key)

            if len(importList):
                # print mod.__file__, importList
                partialsDictionary[name] = importList

    log.info('completed the ``get_python_module_partials`` function')
    return partialsDictionary


## LAST MODIFIED : July 29, 2013
## CREATED : July 29, 2013
## AUTHOR : DRYX
def get_recursive_list_of_directory_contents(
        log,
        baseFolderPath,
        whatToList="all"
    ):
    """list directory contents recursively.

    Options to list only files or only directories.

    **Key Arguments:**
        - ``log`` -- logger
        - ``baseFolderPath`` -- path to the base folder to list contained files and folders recursively
        - ``whatToList`` -- list files only, durectories only or all [ "files" | "dirs" | "all" ]

    **Return:**
        - ``matchedPathList`` -- the matched paths
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import os
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log.info('starting the ``get_recursive_list_of_directory_contents`` function')

    ## VARIABLES ##
    matchedPathList = []
    parentDirectoryList = [baseFolderPath,]

    count = 0
    while os.listdir(baseFolderPath) and count < 20:
        count += 1

        while len(parentDirectoryList) != 0:
            childDirList = []
            for parentDir in parentDirectoryList:
                thisDirList = os.listdir(parentDir)
                for d in thisDirList:
                    fullPath = os.path.join(parentDir, d)

                    if whatToList is "all":
                        matched = True
                    elif whatToList is "dirs":
                        matched = os.path.isdir(fullPath)
                    elif whatToList is "files":
                        matched = os.path.isfile(fullPath)
                    else:
                        log.error('cound not list files in %s, `whatToList` variable incorrect: [ "files" | "dirs" | "all" ]' % (baseFolderPath,))
                        sys.exit(0)

                    if matched:
                        matchedPathList.append(fullPath)

                    ## UPDATE DIRECTORY LISTING
                    if os.path.isdir(fullPath):
                        childDirList.append(fullPath)

                parentDirectoryList = childDirList

    log.info('completed the ``get_recursive_list_of_directory_contents`` function')
    return matchedPathList


## LAST MODIFIED : August 17, 2013
## CREATED : August 17, 2013
## AUTHOR : DRYX
def get_help_for_python_module(
        pathToModuleFile,
        log):
    """print the help for python module

    **Key Arguments:**
        - ``pathToModuleFile`` -- the path to the python module
        - ``log`` -- logger

    **Return:**
        - None

    **Todo**
        - [ ] when complete, clean get_help_for_python_module function
        - [ ] when complete add logging
        - [ ] when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log.info('starting the ``get_help_for_python_module`` function')
    ## VARIABLES ##

    basename = os.path.basename(pathToModuleFile).replace(".py")
    print basename

    log.info('completed the ``get_help_for_python_module`` function')
    return None

if __name__ == '__main__':
    main()
