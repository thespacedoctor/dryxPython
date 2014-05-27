#!/usr/bin/env python
# encoding: utf-8
"""
sortable_mysql_table.py
=======================
:Summary:
    A sortable, customisable HTML table 

:Author:
    David Young

:Date Created:
    May 27, 2014

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
from dryxPython.projectsetup import setup_main_clutil
# from ..__init__ import *

###################################################################
# CLASSES                                                         #
###################################################################


class sortable_mysql_table():

    """
    The worker class for the sortable_mysql_table module

    **Key Arguments:**
        - ``dbConn`` -- mysql database connection
        - ``log`` -- logger
        - ``basePageUrl`` -- the baseurl for the webpage
        - ``columnList`` -- a list of column objects for the table

    **Todo**
        - @review: when complete, clean sortable_mysql_table class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    ## Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
            self,
            log,
            dbConn=False,
            basePageUrl="",
            columnList=[]
    ):
        self.log = log
        self.dbConn = dbConn
        self.basePageUrl = basePageUrl
        self.columnList = columnList
        # xt-self-arg-tmpx
        return None

    def close(self):
        del self
        return None

    # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
    ## Variable Data Atrributes

    # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
    ## Override Variable Data Atrributes

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    ## Method Attributes
    def get(self):
        """get the object
    
        **Return:**
            - ``sortable_mysql_table``
    
        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        sortable_mysql_table = None

        self.log.info('completed the ``get`` method')
        return sortable_mysql_table
    # method-tmpx


    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    ## Override Method Attributes
    # method-override-tmpx

class column():

    """
    A column object for a sortable table

    **Key Arguments:**
        - ``log`` -- logger
        - ``mysqlName`` -- the name of the column in the database table

    **Todo**
        - @review: when complete, clean column class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # 1. @flagged: what are the unique attrributes for each object? Add them
    ## Initialisation

    def __init__(
            self,
            log,
            mysqlName,

    ):
        self.log = log
        self.mysqlName = mysqlName
        # xt-self-arg-tmpx

        self.displayName = self.mysqlName
        return None

    def close(self):
        del self
        return None

    # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
    ## Variable Data Atrributes
    
    reverseSort = False

    # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
    ## Override Variable Data Atrributes

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    ## Method Attributes
    # xt-get-method-tempx
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    ## Override Method Attributes
    # method-override-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# xt-worker-def
# use the tab-trigger below for new function
# xt-def-with-logger
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
