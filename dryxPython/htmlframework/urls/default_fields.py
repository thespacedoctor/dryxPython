#!/usr/bin/env python
# encoding: utf-8
"""
default_fields.py
=================
:Summary:
    Pass a dictionary of the default url fields and their default values to be added to locals() of the calling module

:Author:
    David Young

:Date Created:
    May 28, 2014

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
# PUBLIC FUNCTIONS                                                #
###################################################################
## LAST MODIFIED : May 28, 2014
## CREATED : May 28, 2014
## AUTHOR : DRYX


def default_fields():
    """default feilds

    **Return:**
        - ``fieldDict`` -- a dictionary of { fieldName, defaultValue }

    **Todo**
        - @review: when complete, clean default_fields function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    fieldDict = {
        "sortBy": False,
        "sortDesc": False,
        "pageName": False,
        "pageId": False,
        "tagName": False,
        "settingsFile": 1
    }
    return fieldDict

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
