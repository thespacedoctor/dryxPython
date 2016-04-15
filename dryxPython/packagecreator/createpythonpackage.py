#!/usr/local/bin/python
# encoding: utf-8
"""
*Create the structure required by a python package*

:Author:
    David Young

:Date Created:
    October 23, 2013

.. todo::
    
    - [ ] when complete pull all general functions and classes into dryxPython

Usage:
    dpc-createpythonpackage --packageName=<packageName> --location=<"/path/to/package/parent/folder">
    dpc-createpythonpackage --subPackageName=<subPackageName> --pathToHostDirectory=<"/path/to/host/directory">
    dpc-createpythonpackage --moduleName=<moduleName> --pathToHostDirectory=<"/path/to/host/directory">

    -h, --help    show this help message
    -v, --version show version
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import shutil
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu


def main(arguments=None):
    """
    *The main function used when ``createpythonpackage.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    ########## IMPORTS ##########
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ## ACTIONS BASED ON WHICH ARGUMENTS ARE RECIEVED ##
    # PRINT COMMAND-LINE USAGE IF NO ARGUMENTS PASSED
    if arguments == None:
        arguments = docopt(__doc__)

    # x-unpackge-settings-in-main-function
    # SETUP LOGGER -- DEFAULT TO CONSOLE LOGGER IF NONE PROVIDED IN SETTINGS
    if 'settings' in locals() and "logging settings" in settings:
        log = dl.setup_dryx_logging(
            yaml_file=arguments["--settingsFile"]
        )
    elif "--logger" not in arguments or arguments["--logger"] is None:
        log = dl.console_logger(
            level="WARNING"
        )
        log.debug('logger setup')
    # x-setup-database-connection-in-main-function

    # unpack remaining cl arguments using `exec` to setup the variable names
    # automatically
    for arg, val in arguments.iteritems():
        varname = arg.replace("--", "")
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
        '--- STARTING TO RUN THE createpythonpackage.py AT %s' %
        (startTime,))

    log.debug('locals(): %s' % (locals(),))

    # call the worker function
    if "packageName" in locals() and packageName and "location" in locals():
        createpythonpackage(
            log=log,
            packageName=packageName,
            location=location,
        )
    elif "subPackageName" in locals() and subPackageName:
        createpythonsubpackage(
            log=log,
            subPackageName=subPackageName,
            pathToHostDirectory=pathToHostDirectory,
        )
    elif "moduleName" in locals() and moduleName:
        createpythonmodule(
            log=log,
            moduleName=moduleName,
            pathToHostDirectory=pathToHostDirectory,
        )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE createpythonpackage.py AT %s (RUNTIME: %s) --' %
        (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : October 23, 2013
# CREATED : October 23, 2013
# AUTHOR : DRYX


def createpythonpackage(
        log,
        packageName,
        location,
):
    """
    *createpythonpackage*

    **Key Arguments:**
        - ``log`` -- logger
        - ``packageName`` - packageName
        - ``location`` - location

    **Return:**
        - None

    .. todo::

        - when complete, clean worker function and add comments
        - when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import shutil
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import dryxPython.commonutils as dcu

    # locate the boilerplate folder structure
    moduleDirectory = os.path.dirname(__file__)
    boilerplatePath = moduleDirectory + "/helper_files/package_boilerplate"
    log.debug('boilerplatePath: %s' % (boilerplatePath,))

    location = "%s/%s" % (location, packageName)
    location = os.path.abspath(location)
    log.debug('location: %s' % (location,))

    if os.path.exists(location):
        message = "%s\nthe path to this folder already exists. Please delete it or provide a different package name." % (
            location,)
        log.error(message)
        return

    shutil.copytree(boilerplatePath, location)
    try:
        log.debug("attempting to rename file %s to %s" %
                  (location + "/xxpackagenamexx", location + "/" + packageName))
        os.rename(location + "/xxpackagenamexx", location + "/" + packageName)
    except Exception as e:
        log.error(
            "could not rename file %s to %s - failed with this error: %s " %
            (location + "/xxpackagenamexx", location + "/" + packageName, str(e),))
        return -1

    directoryContents = dcu.get_recursive_list_of_directory_contents(
        log,
        baseFolderPath=location,
        whatToList='files'  # [ 'files' | 'dirs' | 'all' ]
    )

    for ffile in directoryContents:
        log.debug('ffile: %s' % (ffile,))
        pathToReadFile = ffile
        try:
            log.debug("attempting to open the file %s" % (pathToReadFile,))
            readFile = open(pathToReadFile, 'r')
            thisData = readFile.read()
            readFile.close()
        except IOError as e:
            message = 'could not open the file %s' % (pathToReadFile,)
            log.critical(message)
            raise IOError(message)

        thisData = thisData.replace("xxpackagenamexx", packageName)

        pathToWriteFile = ffile
        try:
            log.debug("attempting to open the file %s" % (pathToWriteFile,))
            writeFile = open(pathToWriteFile, 'w')
        except IOError as e:
            message = 'could not open the file %s' % (pathToWriteFile,)
            log.critical(message)
            raise IOError(message)

        writeFile.write(thisData)
        writeFile.close()

    # CREATE A GIT REPO
    create_git_repo(
        log,
        pathToProjectRoot=location
    )

    return None

# LAST MODIFIED : October 25, 2013
# CREATED : October 25, 2013
# AUTHOR : DRYX


def createpythonsubpackage(
        log,
        subPackageName,
        pathToHostDirectory,
):
    """
    *createpythonsubpackage*

    **Key Arguments:**
        - ``log`` -- logger
        - ``subPackageName`` - name of the module to create
        - ``pathToHostDirectory`` - path to the package/subpackage required to host the module

    **Return:**
        - None

    .. todo::

        - @review: when complete, clean createpythonsubpackage function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import shutil
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log.info('starting the ``createpythonsubpackage`` function')

    moduleDirectory = os.path.dirname(__file__)
    boilerplatePath = moduleDirectory + "/helper_files/subpackage_boilerplate"

    location = "%s/%s" % (pathToHostDirectory, subPackageName)
    location = os.path.abspath(location)

    if os.path.exists(location):
        message = "%s\nthe path to this subpackage already exists. Please delete it or provide a different subpackage name." % (
            location,)
        log.error(message)
        return

    shutil.copytree(boilerplatePath, location)

    append_import_to_init_file(
        log=log,
        pathToHostDirectory=pathToHostDirectory,
        moduleName=subPackageName,
        fromImport=False
    )

    log.info('completed the ``createpythonsubpackage`` function')
    return None

# LAST MODIFIED : October 25, 2013
# CREATED : October 25, 2013
# AUTHOR : DRYX


def createpythonmodule(
        log,
        moduleName,
        pathToHostDirectory,
):
    """
    *Create a python module and its test module shawdow within a package or subpackage folder*

    **Key Arguments:**
        - ``log`` -- logger
        - ``moduleName`` - moduleName
        - ``pathToHostDirectory`` - pathToHostDirectory

    **Return:**
        - None

    .. todo::

        - @review: when complete, clean createpythonmodule function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import shutil
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log.info('starting the ``createpythonmodule`` function')
    # TEST THE ARGUMENTS

    moduleDirectory = os.path.dirname(__file__)
    boilerplatePath = moduleDirectory + "/helper_files/module_boilerplate.py"

    location = "%s/%s" % (pathToHostDirectory, moduleName + ".py")
    location = os.path.abspath(location)

    if os.path.exists(location):
        message = "%s\nthe path to this module already exists. Please delete it or provide a different module name." % (
            location,)
        log.error(message)
        return
    shutil.copy(boilerplatePath, location)

    # now for the test directory
    location = "%s/%s" % (pathToHostDirectory, "tests")
    location = os.path.abspath(location)

    if not os.path.exists(location):
        testFolder = moduleDirectory + \
            "/helper_files/subpackage_boilerplate/tests"
        shutil.copytree(testFolder, location)

    # now the test module
    boilerplatePath = moduleDirectory + \
        "/helper_files/test_module_boilerplate.py"
    location = "%s/%s" % (
        pathToHostDirectory, "tests/test_" + moduleName + ".py")
    location = os.path.abspath(location)
    shutil.copy(boilerplatePath, location)

    append_import_to_init_file(
        log=log,
        pathToHostDirectory=pathToHostDirectory,
        moduleName=moduleName,
        fromImport=True
    )

    log.info('completed the ``createpythonmodule`` function')
    return None

# LAST MODIFIED : April 17, 2014
# CREATED : April 17, 2014
# AUTHOR : DRYX


def create_git_repo(
        log,
        pathToProjectRoot):
    """
    *create a first instance of a git repo with all the neccessary files*

    **Key Arguments:**
        - ``log`` -- logger
        - ``pathToProjectRoot`` -- path to the root of the project

    **Return:**
        - None

    .. todo::

        - @review: when complete, clean create_git_repo function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log.info('starting the ``create_git_repo`` function')
    # TEST THE ARGUMENTS
    os.chdir(pathToProjectRoot)

    moduleDirectory = os.path.dirname(__file__)
    gitignore = moduleDirectory + "/helper_files/git_files/gitignore"
    readme = moduleDirectory + "/helper_files/git_files/README.md"
    shutil.copy(gitignore, pathToProjectRoot + "/.gitignore")
    shutil.copy(readme, pathToProjectRoot)

    from subprocess import Popen, PIPE, STDOUT
    cmd = """git init && git add --all . && git commit -m "first commit" """ % locals()
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    ## VARIABLES ##
    log.info('completed the ``create_git_repo`` function')
    return None

# use the tab-trigger below for new function
# LAST MODIFIED : May 9, 2014
# CREATED : May 9, 2014
# AUTHOR : DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method


def append_import_to_init_file(
        log,
        pathToHostDirectory,
        moduleName,
        fromImport=False
):
    """
    *append import to init file*

    **Key Arguments:**
        - ``log`` -- logger
        - ``pathToHostDirectory`` -- path to the directory hosting the __init__ file
        - ``moduleName`` -- name of the module to import
        - ``fromImport`` -- import class/function from module?

    **Return:**
        - None

    .. todo::

        - @review: when complete, clean append_import_to_init_file function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``append_import_to_init_file`` function')
    # Add the module to the __init__ file e.g. `import moduleNmae`
    pathToReadFile = pathToHostDirectory + "/__init__.py"
    try:
        with open(pathToReadFile):
            pass
    except IOError:
        pathToWriteFile = pathToReadFile
        writeFile = open(pathToWriteFile, 'w')
        writeFile.close()
    try:
        log.debug("attempting to open the file %s" % (pathToReadFile,))
        readFile = open(pathToReadFile, 'r')
        thisData = readFile.read()
        readFile.close()
    except IOError as e:
        message = 'could not open the file %s' % (pathToReadFile,)
        log.critical(message)
        raise IOError(message)

    if fromImport:
        thisData = "%(thisData)s\nfrom %(moduleName)s import %(moduleName)s" % locals(
        )
    else:
        thisData = "%(thisData)s\nimport %(moduleName)s" % locals(
        )
    pathToWriteFile = pathToReadFile
    try:
        log.debug("attempting to open the file %s" % (pathToWriteFile,))
        writeFile = open(pathToWriteFile, 'w')
        writeFile.write(thisData)
    except IOError as e:
        message = 'could not open the file %s' % (pathToWriteFile,)
        log.critical(message)
        raise IOError(message)
    writeFile.close()

    log.info('completed the ``append_import_to_init_file`` function')
    return None

# use the tab-trigger below for new function
# x-def-with-logger
##################################################################
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
