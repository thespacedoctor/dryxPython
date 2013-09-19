#!/usr/local/bin/python
# encoding: utf-8
"""
mmd.py
===========
:Summary:
    My MMD helpers

:Author:
    David Young

:Date Created:
    September 19, 2013

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete add cl commands
    @review: make internal function private
    @review: pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
## LAST MODIFIED : September 19, 2013
## CREATED : September 19, 2013
## AUTHOR : DRYX
def convert_to_html(
        log,
        pathToMMDFile,
        css="amblin"):
    """convert mmd file to html

    **Key Arguments:**

    **Return:**
        - ``pathToHtmlFile`` -- the path to the html file

    **Todo**
        - @review: when complete, clean convert_to_html function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    from subprocess import Popen, PIPE
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log.info('starting the ``convert_to_html`` function')
    ## TEST THE ARGUMENTS

    ## GRAB THE CSS ##
    cssFile = os.path.dirname(__file__) + "/assets/%s.css" % (css,)
    pathToReadFile = cssFile
    try:
        log.debug("attempting to open the file %s" % (pathToReadFile,))
        readFile = open(pathToReadFile, 'r')
        cssData = readFile.read()
    except IOError, e:
        message = 'could not open the file %s' % (pathToReadFile,)
        log.critical(message)
        raise IOError(message)
    readFile.close()


    pathToHtmlFile=pathToMMDFile
    for ext in [".md",".mmd",".markdown",".txt",".dat"]:
        pathToHtmlFile = pathToHtmlFile.replace(ext,".html")

    ## MAKE A HEADER IS WRITTEN
    pathToReadFile = pathToMMDFile
    try:
        log.debug("attempting to open the file %s" % (pathToReadFile,))
        readFile = open(pathToReadFile, 'r')
        thisData = readFile.read()
    except IOError, e:
        message = 'could not open the file %s' % (pathToReadFile,)
        log.critical(message)
        raise IOError(message)

    readFile.close()
    basename = os.path.basename(pathToMMDFile)
    filenameNoExtension = os.path.splitext(basename)[0]
    if ("Filename: `%s`" % (filenameNoExtension,)) not in thisData:
        thisData = "Filename: %s\n\n%s" % (filenameNoExtension,thisData)
        pathToWriteFile = pathToMMDFile
        try:
            log.debug("attempting to open the file %s" % (pathToWriteFile,))
            writeFile = open(pathToWriteFile, 'w')
        except IOError, e:
            message = 'could not open the file %s' % (pathToWriteFile,)
            log.critical(message)
            raise IOError(message)
        writeFile.write(thisData)
        writeFile.close()



    mmdBinary = os.path.dirname(__file__) + "/assets/mmd"

    process = Popen([mmdBinary, pathToMMDFile], stdout=PIPE)
    stdout, stderr = process.communicate()

    pathToReadFile = pathToHtmlFile
    try:
        log.debug("attempting to open the file %s" % (pathToReadFile,))
        readFile = open(pathToReadFile, 'r')
        thisData = readFile.read()
    except IOError, e:
        message = 'could not open the file %s' % (pathToReadFile,)
        log.critical(message)
        raise IOError(message)

    readFile.close()

    thisData = thisData.replace('<body>','<style>%s</style><body><div id="wrapper">' % (cssData,))
    thisData = thisData.replace('</body>','</div></body>')
    pathToWriteFile = pathToHtmlFile
    try:
        log.debug("attempting to open the file %s" % (pathToWriteFile,))
        writeFile = open(pathToWriteFile, 'w')
    except IOError, e:
        message = 'could not open the file %s' % (pathToWriteFile,)
        log.critical(message)
        raise IOError(message)
    writeFile.write(thisData)
    writeFile.close()

    log.info('completed the ``convert_to_html`` function')
    return pathToHtmlFile


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
