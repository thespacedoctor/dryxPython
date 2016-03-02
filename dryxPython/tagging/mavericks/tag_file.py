#!/usr/local/bin/python
# encoding: utf-8
"""
tag_file.py
===========
:Summary:
    Tag a given file with mavericks tag

:Author:
    David Young

:Date Created:
    February 25, 2014

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
# LAST MODIFIED : February 25, 2014
# CREATED : February 25, 2014
# AUTHOR : DRYX


def tag_file(
    log,
    pathToFile,
    mode="set",
    tagList=[]
):
    """tag_file

    **Key Arguments:**
        - ``log`` -- the logger
        - ``pathToFile`` -- path to file to manipulate tags
        - ``mode`` -- mode of operation [ add | set | remove ]
        - ``tagList`` -- the list of tags to add/remove/set to the file

    **Return:**
        - None

    **Todo**
        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    theseTags = ('","').join(tagList)
    theseTags = """ "%(theseTags)s" """ % locals()
    print theseTags
    print pathToFile

    pathToFile = pathToFile.replace("'", "\'")

    from subprocess import Popen, PIPE, STDOUT
    cmd = """/usr/local/bin/tag --set %(theseTags)s "%(pathToFile)s" """ % locals()
    print cmd
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

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
