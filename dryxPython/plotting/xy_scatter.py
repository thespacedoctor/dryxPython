#!/usr/bin/env python
# encoding: utf-8
"""
xy_scatter.py
=============
:Summary:
    Plot a test xy scatter plot from the cl

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

Usage:
    dp_xy_scatter --x=<list_or_list_of_lists> ... --y=<list_or_list_of_lists> ... [--axisLabels=<xlabel,ylabel>] [--dataLabels=<list_or_list_of_lists> ...] [--title=<title>] [--colors=<color_or_list_of_colors> ...]
    
    -h, --help    show this help message
    -v, --version show version
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython import convert as dc


def main(arguments=None):
    """
    The main function used when ``xy_scatter.py`` is run as a single script from the cl, or when installed as a cl command
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
        '--- STARTING TO RUN THE xy_scatter.py AT %s' %
        (startTime,))

    # if "axisLabels" not in globals():
    #     axisLabels = False
    # if "title" not in globals():
    #     title = False
    # if "dataLabels" not in globals():
    #     dataLabels = False

    # call the worker function
    xy_scatter(
        log=log,
        x=x,
        y=y,
        axisLabels=axisLabels,
        title=title,
        dataLabels=dataLabels,
        colors=colors
    )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE xy_scatter.py AT %s (RUNTIME: %s) --' %
        (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : April 3, 2014
# CREATED : April 3, 2014
# AUTHOR : DRYX


def xy_scatter(
        log,
        x,
        y,
        dataLabels=False,
        axisLabels=[False, False],
        title=False,
        colors=False,
        reverseYAxis=False,
        outputLocations={}
):
    """xy_scatter

    **Key Arguments:**
        - ``log`` -- the logger
        - ``x`` -- x values (list or list of lists)
        - ``y`` -- y values (list or list of lists)
        - ``axisLabels`` -- axis labels (optional)
        - ``dataLabels`` -- data labels for datasets (optional)
        - ``title`` -- the title for the plot (optional)
        - ``colors`` -- colors to plot (optional)
        - ``reverseYAxis`` -- reverse y-axis (eg for magnitudes)
        - ``outputLocations`` -- a directory of { outputDir: [format(s),], ... }

    **Return:**
        - None

    **Todo**
        @review: when complete, clean worker function and add comments
        @review: when complete add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    import matplotlib.pyplot as plt
    ## LOCAL APPLICATION ##

    if not colors:
        colors = ["#6c71c4", "#859900", "#dc322f", "#268bd2", "#b58900"]
    markers = ["o", "s", "^", "D", "h", "8"]
    if isinstance(colors, str):
        colors = [colors]

    log.debug('x1: %(x)s' % locals())
    log.debug('y1: %(y)s' % locals())
    newX = []
    newY = []
    newDataLabels = []

    if isinstance(x, str):
        x = [x]
        y = [y]

    if not dataLabels:
        dataLabels[:] = [False for i in x]

    log.debug('dataLabels: %(dataLabels)s' % locals())

    if isinstance(dataLabels, str):
        dataLabels = [dataLabels]

    for i in x:
        if not isinstance(i, list):
            i = dc.string_of_values_to_list.string_of_values_to_list(
                log,
                theString=i,
                delimiter=",",  # default = ,
                forceValuesTo=float  # default = False [ int | str | float ...]
            )
        newX.append(i)

    for i in y:
        if not isinstance(i, list):
            i = dc.string_of_values_to_list.string_of_values_to_list(
                log,
                theString=i,
                delimiter=",",  # default = ,
                forceValuesTo=float  # default = False [ int | str | float ...]
            )
        newY.append(i)

    colLength = len(colors)
    colCount = 0
    markLength = len(markers)
    markCount = 0
    for x, y, dataLabel in zip(newX, newY, dataLabels):
        c = colors[colCount]
        m = markers[markCount]
        colCount += 1
        if colCount == colLength:
            colCount = 0
            markCount += 1
            if markCount == markLength:
                markCount = 0
        if len(x) != len(y):
            log.error('x and y lists must be the same length')
            sys.exit(0)

        if dataLabel:
            plt.scatter(
                x=x,  # numpy array of x-points
                y=y,  # numpy array of y-points
                label=dataLabel,
                c=c,
                marker=m,
                alpha=0.7
            )
            legend = plt.legend(loc="lower right", framealpha=1.0)
            # Set the legend face color
            frame = legend.get_frame()
            frame.set_facecolor('#D2D1D1')
        else:
            plt.scatter(
                x=x,  # numpy array of x-points
                y=y,  # numpy array of y-points
                c=c,
                marker=m,
                alpha=0.5
            )

    if isinstance(axisLabels, str):
        axisLabels = dc.string_of_values_to_list.string_of_values_to_list(
            log,
            theString=axisLabels,
            delimiter=",",  # default = ,
            forceValuesTo=str  # default = False    [ int | str | float ...]
        )

    if axisLabels and axisLabels[0] is not False:
        plt.xlabel(axisLabels[0])
    if axisLabels and axisLabels[1] is not False:
        plt.ylabel(axisLabels[1])
    if title:
        plt.title(title)

    if reverseYAxis:
        ax = plt.gca()
        ax.invert_yaxis()

    if title:
        fileName = title.lower().replace(" ", "_").replace(
            "(", "").replace(")", "").replace(".", "")
    else:
        fileName = "tmp"
    print outputLocations
    for k, v in outputLocations.iteritems():
        if isinstance(v, str):
            v = [v]
        for i in v:
            filePath = "%(k)s/%(fileName)s.%(i)s" % locals()
            plt.savefig(filePath)
    if not len(outputLocations):
        filePath = "/tmp/%(fileName)s.png" % locals()
        plt.savefig(filePath)

    plt.close()
    # plt.show()
    return None

# use the tab-trigger below for new function
# x-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


# use the tab-trigger below for new function
# x-def-with-logger


############################################
# CODE TO BE DEPECIATED                    #
############################################

if __name__ == '__main__':
    main()

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
