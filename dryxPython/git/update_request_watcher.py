#!/usr/bin/env python
# encoding: utf-8
"""
update_request_watcher.py
=========================
:Summary:
    Update the git repo with a request in the _update_requests_ directory of your git repos folder

:Author:
    David Young

:Date Created:
    June 24, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    git_update_request_watcher -p <pathToGitRepos>

    -h, --help    show this help message
    -v, --version show version
    -p, --path    absolute path to the `git_repo` folder
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil


def main(arguments=None):
    """
    The main function used when ``update_request_watcher.py`` is run as a single script from the cl, or when installed as a cl command
    """
    su = setup_main_clutil(
        arguments=arguments,
        docString=__doc__,
        logLevel="WARNING"
    )
    arguments, settings, log, dbConn = su.setup()

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

    ## START LOGGING ##
    startTime = dcu.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE update_request_watcher.py AT %s' %
        (startTime,))

    # find all update request files in "/_updates_required_" folder
    basePath = pathToGitRepos + "/_updates_required_"
    for d in os.listdir(basePath):
        if os.path.isfile(os.path.join(basePath, d)):
            if "gitupdates" in d:
                thisRepo = d.replace(".gitupdates", "")

                # check local git-repo requiring an update actually exists --
                # trigger pull if it does
                pathToRepo = pathToGitRepos + "/" + thisRepo
                if not os.path.exists(pathToRepo):
                    message = "the path to the Folder folder %s does not exist on this machine" % (
                        pathToRepo,)
                    log.warning(message)
                else:
                    dcu.update_git_repos.update_git_repos(
                        log=log,
                        gitProjectRoot=pathToRepo,
                        branchToUpdate="master",
                        installClUtils=True
                    )

                # finally delete the update request file
                os.remove(os.path.join(basePath, d))

    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE update_request_watcher.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################
# xt-class-module-worker-tmpx
# xt-class-tmpx


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
