#!/usr/local/bin/python
# encoding: utf-8
"""
declination_sexegesimal_to_decimal.py
=====================================
:Summary:
    Convert declination from sexegesimal to decimal degrees - can accept all sorts of sexegesimal formats (spaces, colons)

:Author:
    David Young

:Date Created:
    January 17, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    dat_declination_sexegesimal_to_decimal --dec=<"dec-sexegesimal">

    -h, --help    show this help message
    -v, --version show version
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu


def main(arguments=None):
    """
    The main function used when ``declination_sexegesimal_to_decimal.py`` is run as a single script from the cl, or when installed as a cl command
    """
    ########## IMPORTS ##########
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ## ACTIONS BASED ON WHICH ARGUMENTS ARE RECIEVED ##
    ## PRINT COMMAND-LINE USAGE IF NO ARGUMENTS PASSED
    if arguments == None:
        arguments = docopt(__doc__)

    ## UNPACK SETTINGS
    if "--settingsFile" in arguments and arguments["--settingsFile"]:
        import yaml
        stream = file(arguments["--settingsFile"], 'r')
        settings = yaml.load(stream)
        stream.close()
    ## SETUP LOGGER -- DEFAULT TO CONSOLE LOGGER IF NONE PROVIDED IN SETTINGS
    if 'settings' in locals() and "logging settings" in settings:
        log = dl.setup_dryx_logging(
            yaml_file=arguments["--settingsFile"]
        )
    elif "--logger" not in arguments or arguments["--logger"] is None:
        log = dl.console_logger(
            level="WARNING"
        )
        log.debug('logger setup')

    # unpack remaining cl arguments using `exec` to setup the variable names
    # automatically
    for arg, val in arguments.iteritems():
        varname = arg.replace("--", "")
        if isinstance(val, str):
            exec(varname + " = '%s'" % (val,))
        else:
            exec(varname + " = %s" % (val,))
        if arg == "--dbConn":
            dbConn = val
        log.debug('%s = %s' % (varname, val,))

    dec = declination_sexegesimal_to_decimal(
        log=log,
        dec=dec,
    )

    print dec

    return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
## LAST MODIFIED : January 17, 2014
## CREATED : January 17, 2014
## AUTHOR : DRYX


def declination_sexegesimal_to_decimal(
    log,
    dec
):
    """declination_sexegesimal_to_decimal

    **Key Arguments:**
        # copy usage method(s) here and select the following snippet from the command palette:
        - ``log`` -- the logger
        - ``dec`` -- declination in sexegesimal

    **Return:**
        - ``decimalDegrees``

    **Todo**
        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import re
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ## remove surrounding whitespace
    dec = str(dec).strip()

    # Look for a minus sign.  Note that -00 is the same as 00.
    regex = re.compile(
        '^([\+\-]?(\d|[0-8]\d))\D+([0-5]\d)\D+([0-5]\d(\.\d+)?)$')
    decMatch = regex.match(dec)

    if decMatch:
        degrees = decMatch.group(1)
        minutes = decMatch.group(3)
        seconds = decMatch.group(4)

        if degrees[0] == '-':
            sgn = -1
        else:
            sgn = 1

        degrees = abs(float(degrees))
        minutes = float(minutes)
        seconds = float(seconds)

        decimalDegrees = (degrees + (minutes / 60.0)
                          + (seconds / 3600.0)) * sgn

    else:
        raise IOError(
            "could not convert dec to decimal degrees, could not parse sexegesimal input")

    return decimalDegrees

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
