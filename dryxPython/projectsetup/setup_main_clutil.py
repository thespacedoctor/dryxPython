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
import yaml
from collections import OrderedDict
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
            options_first=False,
            projectName=False,
            orderedSettings=False
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
        stream = False
        if "<settingsFile>" in arguments and arguments["<settingsFile>"]:
            stream = file(arguments["<settingsFile>"], 'r')
        elif "<pathToSettingsFile>" in arguments and arguments["<pathToSettingsFile>"]:
            stream = file(arguments["<pathToSettingsFile>"], 'r')
        elif "--settingsFile" in arguments and arguments["--settingsFile"]:
            stream = file(arguments["--settingsFile"], 'r')
        elif "pathToSettingsFile" in arguments and arguments["pathToSettingsFile"]:
            stream = file(arguments["pathToSettingsFile"], 'r')
        elif "settingsFile" in arguments and arguments["settingsFile"]:
            stream = file(arguments["settingsFile"], 'r')
        elif ("settingsFile" in arguments and arguments["settingsFile"] == None) or ("<pathToSettingsFile>" in arguments and arguments["<pathToSettingsFile>"] == None):

            if projectName != False:
                os.getenv("HOME")
                projectDir = os.getenv(
                    "HOME") + "/.config/%(projectName)s" % locals()
                exists = os.path.exists(projectDir)
                if not exists:
                    dcu.dryx_mkdir(
                        log=None,
                        directoryPath=projectDir
                    )
                settingsFile = os.getenv(
                    "HOME") + "/.config/%(projectName)s/%(projectName)s.yaml" % locals()
                exists = os.path.exists(settingsFile)
                if not exists:
                    import codecs
                    writeFile = codecs.open(
                        settingsFile, encoding='utf-8', mode='w')

                import yaml
                astream = file(settingsFile, 'r')
                if orderedSettings:
                    this = ordered_load(astream, yaml.SafeLoader)
                else:
                    this = yaml.load(astream)
                if this:
                    settings = this
                    arguments["<settingsFile>"] = settingsFile
                else:
                    print "please add settings to file '%(settingsFile)s'" % locals()
                    sys.exit(0)
        else:
            pass

        if stream is not False:
            import yaml
            if orderedSettings:
                settings = ordered_load(stream, yaml.SafeLoader)
            else:
                settings = yaml.load(stream)

        # SETUP LOGGER -- DEFAULT TO CONSOLE LOGGER IF NONE PROVIDED IN
        # SETTINGS
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
                val = val.replace("'", "\\'")
                exec(varname + " = '%s'" % (val,))
            else:
                exec(varname + " = %s" % (val,))
            if arg == "--dbConn":
                dbConn = val
            log.debug('%s = %s' % (varname, val,))

        # SETUP A DATABASE CONNECTION BASED ON WHAT ARGUMENTS HAVE BEEN PASSED
        dbConn = False
        if 'settings' in locals() and "database settings" in settings and "host" in settings["database settings"]:
            host = settings["database settings"]["host"]
            user = settings["database settings"]["user"]
            passwd = settings["database settings"]["password"]
            dbName = settings["database settings"]["db"]
            dbConn = True
        elif "hostFlag" in locals() and "dbNameFlag" in locals():
            # SETUP DB CONNECTION
            dbConn = True
            host = arguments["--host"]
            user = arguments["--user"]
            passwd = arguments["--passwd"]
            dbName = arguments["--dbName"]
        else:
            pass
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
    # xt-class-method

    # Override Method Attributes
    # method-override-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)


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
