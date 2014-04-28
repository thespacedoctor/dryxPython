#!/usr/bin/env python
# encoding: utf-8
"""
utKit.py
========
:Summary:
    A unit-testing kit to simplify my unit-tests

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
import logging
import logging.config
import MySQLdb as ms
import yaml
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu

###################################################################
# CLASSES                                                         #
###################################################################


class utKit():

    """
    My unit-testing kit

    **Key Arguments:**


    **Todo**
        - @review: when complete, clean utKit class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    ## Variable Data Atrributes

    # SETUP LOGGING
    loggerConfig = """
    version: 1
    formatters:
        file_style:
            format: '* %(asctime)s - %(name)s - %(levelname)s (%(filename)s > %(funcName)s > %(lineno)d) - %(message)s  '
            datefmt: '%Y/%m/%d %H:%M:%S'
        console_style:
            format: '* %(asctime)s - %(levelname)s: %(filename)s:%(funcName)s:%(lineno)d > %(message)s'
            datefmt: '%H:%M:%S'
        html_style:
            format: '<div id="row" class="%(levelname)s"><span class="date">%(asctime)s</span>   <span class="label">file:</span><span class="filename">%(filename)s</span>   <span class="label">method:</span><span class="funcName">%(funcName)s</span>   <span class="label">line#:</span><span class="lineno">%(lineno)d</span> <span class="pathname">%(pathname)s</span>  <div class="right"><span class="message">%(message)s</span><span class="levelname">%(levelname)s</span></div></div>'
            datefmt: '%Y-%m-%d <span class= "time">%H:%M <span class= "seconds">%Ss</span></span>'
    handlers:
        console:
            class: logging.StreamHandler
            level: DEBUG
            formatter: console_style
            stream: ext://sys.stdout
    root:
        level: DEBUG
        handlers: [console]"""

    dbConfig = """
    version: 1
    db: pessto_marshall_sandbox
    host: localhost
    user: root
    password: root
    """

    ## Initialisation
    def __init__(
            self,
            moduleDirectory
    ):
        self.moduleDirectory = moduleDirectory
        # x-self-arg-tmpx

        # SETUP PATHS TO COMMON DIRECTORIES FOR TEST DATA
        self.pathToInputDir = moduleDirectory + "/input/"
        self.pathToOutputDir = moduleDirectory + "/output/"

        return

    ## Method Attributes
    def setupModule(
            self):
        """The setupModule method

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean setupModule method
            - @review: when complete add logging
        """
        ## TEST THE ARGUMENTS

        ## VARIABLES ##
        logging.config.dictConfig(yaml.load(self.loggerConfig))
        log = logging.getLogger(__name__)
        connDict = yaml.load(self.dbConfig)
        dbConn = ms.connect(
            host=connDict['host'],
            user=connDict['user'],
            passwd=connDict['password'],
            db=connDict['db'],
        )

        return log, dbConn, self.pathToInputDir, self.pathToOutputDir

    # use the tab-trigger below for new method
    def tearDownModule(
            self):
        """The tearDownModule method
    
        **Key Arguments:**
            # -
    
        **Return:**
            - None
    
        **Todo**
            - @review: when complete, clean tearDownModule method
            - @review: when complete add logging
        """

        return None

    # use the tab-trigger below for new method
    # method-tmpx

    ## Override Method Attributes
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
