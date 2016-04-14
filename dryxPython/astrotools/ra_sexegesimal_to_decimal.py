#!/usr/local/bin/python
# encoding: utf-8
"""
*convert ra from sexegesimal (in any format) to decimal degrees*

:Author:
    David Young

:Date Created:
    January 17, 2014

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    dat_ra_sexegesimal_to_decimal --ra=<ra-sexegesimal>

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
    *The main function used when ``ra_sexegesimal_to_decimal.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    ########## IMPORTS ##########
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ## ACTIONS BASED ON WHICH ARGUMENTS ARE RECIEVED ##
    # PRINT COMMAND-LINE USAGE IF NO ARGUMENTS PASSED
    if arguments == None:
        arguments = docopt(__doc__)

    # SETUP LOGGER -- DEFAULT TO CONSOLE LOGGER IF NONE PROVIDED IN SETTINGS
    if "--logger" not in arguments or arguments["--logger"] is None:
        log = dl.console_logger(
            level="WARNING"
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

    ra = ra_sexegesimal_to_decimal(
        ra=ra,
    )

    print ra

    return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : January 17, 2014
# CREATED : January 17, 2014
# AUTHOR : DRYX


def ra_sexegesimal_to_decimal(
    ra
):
    """
    *ra_sexegesimal_to_decimal*

    **Key Arguments:**
        - ``ra`` -- ra in sexegesimal

    **Return:**
        - ``decimalDegrees``

    .. todo::

        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import re
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    # remove surrounding whitespace
    ra = str(ra).strip()

    regex = re.compile(
        '^(\+?(\d|[0-1]\d|2[0-3]))\D+([0-5]\d)\D+([0-6]?\d(\.\d+)?)$')
    raMatch = regex.match(ra)

    if raMatch:
        degrees = raMatch.group(1)
        minutes = raMatch.group(3)
        seconds = raMatch.group(4)

        degrees = abs(float(degrees)) * 15.0
        minutes = float(minutes) * 15.0
        seconds = float(seconds) * 15.0

        decimalDegrees = (degrees + (minutes / 60.0)
                          + (seconds / 3600.0))

    else:
        raise IOError(
            "could not convert ra to decimal degrees, could not parse sexegesimal input. Original value was `%(ra)s`" % locals())

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
