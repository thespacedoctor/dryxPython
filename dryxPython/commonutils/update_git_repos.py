#!/usr/local/bin/python
# encoding: utf-8
"""
*Update the pessto marshall git repos on the VM machines*

:Author:
    David Young

:Date Created:
    November 19, 2013

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    dcu_update_git_repos --settingsFile=<pathToSettingsFile>

    -h, --help    show this help message
    -v, --version show version
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from subprocess import Popen, PIPE, STDOUT
from docopt import docopt
from dryxPython import logs as dl


def main(arguments=None):
    """
    *The main function used when ``update_git_repos.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    ########## IMPORTS ##########
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import dryxPython.commonutils as dcu

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

    ## START LOGGING ##
    startTime = dcu.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE git_update_script.py AT %s' %
        (startTime,))

    # call the worker function
    # x-if-settings-or-database-credientials
    if "git repos" in settings:
        for repo in settings["git repos"]:
            log.debug('repo["path"]: %s' % (repo["path"],))
            log.debug('repo["branchToUpdate"]: %s' % (repo["branchToUpdate"],))
            update_git_repos(
                log=log,
                gitProjectRoot=repo["path"],
                branchToUpdate=repo["branchToUpdate"]
            )

    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE git_update_script.py AT %s (RUNTIME: %s) --' %
        (endTime, runningTime, ))

    return


def update_git_repos(
    log,
    gitProjectRoot="",
    branchToUpdate="master",
    installClUtils=False
):
    """
    *update_git_repos*

    **Key Arguments:**
        # copy usage method(s) here and select the following snippet from the command palette:
        - ``log`` -- the logger
        - ``gitProjectRoot`` -- path to the git project
        - ``branchToUpdate`` -- the git branch you wish to update (or 'all' to update all branches)

    **Return:**
        - None

    .. todo::

        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    from subprocess import call

    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    os.chdir(gitProjectRoot)
    call(["git", "checkout", branchToUpdate])
    # call(["git", "add", "."])
    # call(["git", "commit", "-am",
    #      "'auto commit from python git repo updater script before pull from origin'"])
    call(["git", "pull", "origin", branchToUpdate])
    # call(["git", "push", "origin", branchToUpdate])

    if installClUtils:
        # if setup.py exists in repo, then install as development package --
        # with any cl-utils
        exists = os.path.exists("%(gitProjectRoot)s/setup.py" % locals())
        if exists:
            log.debug('about to install cl-utils')
            pwd = os.getcwd()
            os.chdir(gitProjectRoot)
            cmd = """python setup.py develop""" % locals()
            p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
            output = p.communicate()[0]
            log.debug('output: %(output)s' % locals())
            print output
            os.chdir(pwd)

    return None


if __name__ == '__main__':
    main()

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
