#!/usr/bin/env python
# encoding: utf-8
"""
string_of_values_to_list.py
===========================
:Summary:
    Convert a delimited string of values to a list

:Author:
    David Young

:Date Created:
    April 3, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

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

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : April 3, 2014
# CREATED : April 3, 2014
# AUTHOR : DRYX


def string_of_values_to_list(
        log,
        theString,
        delimiter=",",
        forceValuesTo=False
):
    """string_of_values_to_list

    **Key Arguments:**
        # copy usage method(s) here and select the following snippet from the command palette:
        - ``log`` -- the logger
        - ``theString`` -- the delimited seperated string of values

    **Return:**
        - `theList` -- the list

    **Todo**
        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    if not isinstance(theString, str):
        log.error('%s is not a string - could not convert' % (theString,))

    if theString[0] == "[" and theString[-1:] == "]":
        theString = theString[1:-1]
    else:
        print theString[0], theString[-1:]

    # theList = map(int, theString.split(','))
    if forceValuesTo is False:
        theList = [s for s in theString.split(delimiter)]
    else:
        theList = map(forceValuesTo, theString.split(delimiter))
        log.debug('verify values force into correct format: %s' %
                  (isinstance(theList[0], forceValuesTo)))

    log.debug('theList: %(theList)s' % locals())
    log.debug('verify that theList is a list: %s' %
              (isinstance(theList, list),))

    return theList

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
