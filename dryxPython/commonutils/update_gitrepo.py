#!/usr/local/bin/python
# encoding: utf-8
"""
update_gitrepo.py
=================
:Summary:
    Update a git repo via python

:Author:
    David Young

:Date Created:
    November 19, 2013

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
from dryxPython import logs as dl

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################


def update_gitrepo(
    log,
    gitProjectRoot="",
    branchToUpdate="master"
):
    """update_gitrepo

    **Key Arguments:**
        # copy usage method(s) here and select the following snippet from the command palette:
        - ``log`` -- the logger
        - ``gitProjectRoot`` -- path to the git project
        - ``branchToUpdate`` -- the git branch you wish to update (or 'all' to update all branches)

    **Return:**
        - None

    **Todo**
        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    from subprocess import call
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    os.chdir(gitProjectRoot)
    call(["git", "pull", "origin", branchToUpdate])

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
