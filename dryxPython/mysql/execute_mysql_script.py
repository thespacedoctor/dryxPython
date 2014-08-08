#!/usr/local/bin/python
# encoding: utf-8
"""
execute_mysql_script.py
=======================
:Summary:
    Provide the path to a mysql script and execute it from python modules

:Author:
    David Young

:Date Created:
    October 29, 2013

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    - [ ] when complete pull all general functions and classes into dryxPython

Usage:
    dms_execute_mysql_script --settingsFile=<pathToSettingsFile> --pathToMysqlScript=<pathToMysqlScript> [force]
    dms_execute_mysql_script --host=<host> --user=<user> --passwd=<passwd> --dbName=<dbName> --pathToMysqlScript=<pathToMysqlScript> [force]

    -h, --help    show this help message
    -v, --version show version
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu


def main(arguments=None):
    """
    The main function used when ``execute_mysql_script.py`` is run as a single script from the cl, or when installed as a cl command
    """
    ########## IMPORTS ##########
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ## ACTIONS BASED ON WHICH ARGUMENTS ARE RECIEVED ##
    # PRINT COMMAND-LINE USAGE IF NO ARGUMENTS PASSED
    if arguments == None:
        arguments = docopt(__doc__)

    # UNPACK SETTINGS
    if "--settingsFile" in arguments and arguments["--settingsFile"]:
        import yaml
        stream = file(arguments["--settingsFile"], 'r')
        settings = yaml.load(stream)
        stream.close()
    # SETUP LOGGER -- DEFAULT TO CONSOLE LOGGER IF NONE PROVIDED IN SETTINGS
    if 'settings' in locals() and "logging settings" in settings:
        log = dl.setup_dryx_logging(
            yaml_file=arguments["--settingsFile"]
        )
        # log.error('log: %s' % (log,))
    elif "--logger" not in arguments or arguments["--logger"] is None:
        log = dl.console_logger(
            level="DEBUG"
        )
        log.debug('logger setup')

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

    # Check for the force option
    if "force" not in locals() or force is not True:
        force = False

    # SETUP A DATABASE CONNECTION BASED ON WHAT ARGUMENTS HAVE BEEN PASSED
    dbConn = False
    if 'settings' in locals() and "database settings" in settings:
        host = settings["database settings"]["host"]
        user = settings["database settings"]["user"]
        passwd = settings["database settings"]["password"]
        dbName = settings["database settings"]["db"]
        dbConn = True
    elif "host" in locals() and "dbName" in locals():
        # SETUP DB CONNECTION
        dbConn = True
        host = arguments["--host"]
        user = arguments["--user"]
        passwd = arguments["--passwd"]
        dbName = arguments["--dbName"]
    if dbConn:
        import MySQLdb as ms
        dbConn = ms.connect(
            host=host,
            user=user,
            passwd=passwd,
            db=dbName,
            use_unicode=True,
            charset='utf8'
        )
        log.debug('dbConn: %s' % (dbConn,))

    ## START LOGGING ##
    startTime = dcu.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE execute_mysql_script.py AT %s' %
        (startTime,))

    # call the worker function
    execute_mysql_script(
        log=log,
        user=user,
        passwd=passwd,
        db=dbName,
        host=host,
        pathToMysqlScript=pathToMysqlScript,
        force=force
    )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE execute_mysql_script.py AT %s (RUNTIME: %s) --' %
        (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : October 29, 2013
# CREATED : October 29, 2013
# AUTHOR : DRYX


def execute_mysql_script(
    log,
    user,
    passwd,
    db,
    host,
    pathToMysqlScript,
    force=False
):
    """execute_mysql_script

    **Key Arguments:**
        - ``log`` -- the logger
        - ``user`` -- the database user
        - ``passwd`` -- the database password
        - ``db`` -- the database name
        - ``host`` -- the database hostname
        - ``pathToMysqlScript`` -- pathToMysqlScript
        - ``force`` -- add the force flag to the mysql execution command?

    **Return:**
        - None

    **Todo**
        - [ ] when complete, clean worker function and add comments
        - [ ] when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    from subprocess import Popen, PIPE
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    # make note of the current directory before switching to the script
    # directory
    pwd = os.getcwd()
    scriptDir = os.path.dirname(pathToMysqlScript)
    log.debug('scriptDir: %s' % (scriptDir,))
    os.chdir(scriptDir)
    basename = os.path.basename(pathToMysqlScript)
    log.debug('basename: %s' % (basename,))
    log.debug('force: %s' % (force,))

    if force:
        force = " -f"
    else:
        force = ""

    # run the script and wait to complete
    cmd = "mysql -u %s --password=%s %s -h %s%s < %s" % (
        user, passwd, db, host, force, basename)
    process = Popen(cmd,
                    stdout=PIPE, stdin=PIPE, shell=True)
    output = process.communicate()[0]
    process.wait()

    # change back to original directory
    os.chdir(pwd)

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
