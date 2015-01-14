#!/usr/bin/env python
# encoding: utf-8
"""
setup_main_clutil.py
====================
:Summary:
    Toolset to setup the main function for a cl-util

:Author:
    David Young

:Date Created:
    April 16, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu

###################################################################
# CLASSES                                                         #
###################################################################


class setup_main_clutil():

    """
    common setup methods & attributes of the main function in cl-util

    **Key Arguments:**
        - ``dbConn`` -- mysql database connection

    **Todo**
        - @review: when complete, clean setup_main_clutil class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Variable Data Atrributes

    # Override Variable Data Atrributes

    # Initialisation

    def __init__(
            self,
            arguments,
            docString,
            logLevel="DEBUG",
            options_first=False
    ):
        self.arguments = arguments
        self.docString = docString
        self.logLevel = logLevel
        # x-self-arg-tmpx

        ## ACTIONS BASED ON WHICH ARGUMENTS ARE RECIEVED ##
        # PRINT COMMAND-LINE USAGE IF NO ARGUMENTS PASSED
        if arguments == None:
            arguments = docopt(docString, options_first=options_first)
        self.arguments = arguments

        # UNPACK SETTINGS
        if "<settingsFile>" in arguments and arguments["<settingsFile>"]:
            import yaml
            stream = file(arguments["<settingsFile>"], 'r')
            settings = yaml.load(stream)
            stream.close()
        elif "<pathToSettingsFile>" in arguments and arguments["<pathToSettingsFile>"]:
            import yaml
            stream = file(arguments["<pathToSettingsFile>"], 'r')
            settings = yaml.load(stream)
            stream.close()
        elif "--settingsFile" in arguments and arguments["--settingsFile"]:
            import yaml
            stream = file(arguments["--settingsFile"], 'r')
            settings = yaml.load(stream)
            stream.close()
        elif "pathToSettingsFile" in arguments and arguments["pathToSettingsFile"]:
            import yaml
            stream = file(arguments["pathToSettingsFile"], 'r')
            settings = yaml.load(stream)
            stream.close()
        elif "settingsFile" in arguments and arguments["settingsFile"]:
            import yaml
            stream = file(arguments["settingsFile"], 'r')
            settings = yaml.load(stream)
            stream.close()

        # SETUP LOGGER -- DEFAULT TO CONSOLE LOGGER IF NONE PROVIDED IN SETTINGS
        if 'settings' in locals() and "logging settings" in settings:
            if "<settingsFile>" in arguments:
                log = dl.setup_dryx_logging(
                    yaml_file=arguments["<settingsFile>"]
                )
            elif "<pathToSettingsFile>" in arguments:
                log = dl.setup_dryx_logging(
                    yaml_file=arguments["<pathToSettingsFile>"]
                )
            elif "--settingsFile" in arguments:
                log = dl.setup_dryx_logging(
                    yaml_file=arguments["--settingsFile"]
                )
            elif "pathToSettingsFile" in arguments:
                log = dl.setup_dryx_logging(
                    yaml_file=arguments["pathToSettingsFile"]
                )

            elif "settingsFile" in arguments:
                log = dl.setup_dryx_logging(
                    yaml_file=arguments["settingsFile"]
                )

        elif "--logger" not in arguments or arguments["--logger"] is None:
            log = dl.console_logger(
                level=self.logLevel
            )
            log.debug('logger setup')

        self.log = log

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
            dbConn.autocommit(True)
            log.debug('dbConn: %s' % (dbConn,))

        self.dbConn = dbConn

        if not 'settings' in locals():
            settings = False
        self.settings = settings

        return None

    # Method Attributes
    # use the tab-trigger below for new method
    def setup(
            self):
        """setup the attributes and return

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean setup method
            - @review: when complete add logging
        """
        return self.arguments, self.settings, self.log, self.dbConn

    # use the tab-trigger below for new method
    # method-tmpx

    # Override Method Attributes
    # method-override-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
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
