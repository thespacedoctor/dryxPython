#!/usr/local/bin/python
# encoding: utf-8
"""
plotting
===============
:Summary:
    Module of plotting functions

:Author:
    David Young

:Date Created:
    April 16, 2013

:dryx syntax:
    - ``xxx`` = come back here and do some more work
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script please email me: d.r.young@qub.ac.uk
"""
################# GLOBAL IMPORTS ####################
# from _project_setup import *

######################################################
# MAIN LOOP - USED FOR DEBUGGING OR WHEN SCRIPTING   #
######################################################
def main():
    """
    The main function used when ``plotting`` run as a single script from the cl
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import dryxPython.commonutils as cu

    dbConn, log = settings(
        dbConn=False,
        log=True)

    ## START LOGGING ##
    startTime = cu.get_now_sql_datetime()
    log.info('--- STARTING TO RUN THE plotting AT %s' % (startTime,))

    ## WRITE CODE HERE

    if dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = cu.get_now_sql_datetime()
    runningTime = cu.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE plotting AT %s (RUNTIME: %s) --' % (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
## LAST MODIFIED : April 15, 2013
## CREATED : April 15, 2013
## AUTHOR : DRYX
def plot_polynomial(
        log,
        title,
        polynomialDict,
        orginalDataDictionary=False,
        pathToOutputPlotsFolder="~/Desktop",
        xRange=False,
        xlabel=False,
        ylabel=False,
        xAxisLimits=False,
        yAxisLimits=False,
        yAxisInvert=False,
        prependNum=False,
        legend=False):
    """Plot a dictionary of numpy lightcurves polynomials

    **Key Arguments:**
        - ``log`` -- logger
        - ``title`` -- title for the plot
        - ``polynomialDict`` -- dictionary of polynomials { label01 : poly01, label02 : poly02 }
        - ``orginalDataDictionary`` -- the orginal data points {name: [x, y]}
        - ``pathToOutputPlotsFolder`` -- path the the output folder to save plot to
        - ``xRange`` -- the x-range for the polynomial [xmin, xmax, interval]
        - ``xlabel`` -- xlabel
        - ``ylabel`` -- ylabel
        - ``xAxisLimits`` -- the x-limits for the axes [xmin, xmax]
        - ``yAxisLimits`` -- the y-limits for the axes [ymin, ymax]
        - ``yAxisInvert`` -- invert the y-axis? Useful for lightcurves
        - ``prependNum`` -- prepend this number to the output filename
        - ``legend`` -- plot a legend?

    **Return:**
        - None
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import sys
    ## THIRD PARTY ##
    import matplotlib.pyplot as plt
    import numpy as np
    ## LOCAL APPLICATION ##

    ################ >ACTION(S) ################
    colors = {
        'green' : '#859900',
        'blue' : '#268bd2',
        'red' : '#dc322f',
        'gray' : '#D2D1D1',
        'orange' : '#cb4b16',
        'violet' : '#6c71c4',
        'cyan' : '#2aa198',
        'magenta' : '#d33682',
        'yellow' : '#b58900'
    }

    if not xRange:
        log.error('please provide an x-range')
        sys.exit(1)

    ax = plt.subplot(111)

    if len(xRange) == 2:
        xRange.append(1)

    x = np.arange(xRange[0], xRange[1], xRange[2])
    if xAxisLimits:
        ax.set_xlim(xAxisLimits[0], xAxisLimits[1])
    else:
        overShoot = (xRange[1] - xRange[0])/10.
        ax.set_xlim(xRange[0] - overShoot, xRange[1] + overShoot)
    if yAxisLimits:
        ax.set_ylim(yAxisLimits[0], yAxisLimits[1])

    theseColors = [ colors['blue'], colors['green'], colors['red'], colors['violet'] ]

    count = 0
    if orginalDataDictionary:
        for name, data in orginalDataDictionary.iteritems():
            ax.plot(data[0], data[1], '.', label=name, color=theseColors[count])
            count += 1
            if count == 4:
                count = 0

    count = 0
    for snType, poly in polynomialDict.iteritems():
        log.debug('x: %s' % (x,))
        ax.plot(x, poly(x), label='%s' % (snType,), color=theseColors[count])
        count += 1
        if count == 4:
            count = 0

    # Shink current axis by 20%
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    # Put a legend to the right of the current axis
    if legend:
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size':8})
    ax.titlesize = 'medium'   # fontsize of the axes title
    ax.labelsize = 'medium'  # fontsize of the x any y labels

    if xlabel:
        plt.xlabel(xlabel, fontsize='small')
    if ylabel:
        plt.ylabel(ylabel, fontsize='small')
    if title:
        plt.title(title, fontsize='small', verticalalignment = 'bottom', linespacing = 0.2)

    if yAxisInvert:
        ax.invert_yaxis()

    # fileName = pathToOutputPlotsFolder + title.replace(" ", "_") + ".ps"
    # plt.savefig(fileName)
    if prependNum:
        title = "%02d_%s" % (prependNum, title)
    thisTitle = title.replace(" ", "_")
    thisTitle = thisTitle.replace("-", "_")
    fileName = pathToOutputPlotsFolder + thisTitle + ".png"
    imageLink = """
![%s_plot](%s)

""" % (thisTitle, fileName)
    plt.savefig(fileName)
    plt.clf()  # clear figure

    return imageLink


## LAST MODIFIED : April 15, 2013
## CREATED : April 15, 2013
## AUTHOR : DRYX
def plot_polar(
        log,
        title,
        dataDictionary,
        pathToOutputPlotsFolder="~/Desktop",
        dataRange=False,
        ylabel=False,
        radius=False,
        circumference=True,
        circleTicksRange=(0, 360, 60),
        circleTicksLabels=".",
        prependNum=False):
    """Plot a dictionary of numpy lightcurves polynomials

    **Key Arguments:**
        - ``log`` -- logger
        - ``title`` -- title for the plot
        - ``dataDictionary`` -- dictionary of data to plot { label01 : dataArray01, label02 : dataArray02 }
        - ``pathToOutputPlotsFolder`` -- path the the output folder to save plot to
        - ``dataRange`` -- the range for the data [min, max]
        - ``ylabel`` -- ylabel
        - ``radius`` -- the max radius of the plot
        - ``circumference`` -- draw the circumference of the plot?
        - ``circleTicksRange``
        - ``circleTicksLabels``
        - ``prependNum`` -- prepend this number to the output filename

    **Return:**
        - None
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import sys
    ## THIRD PARTY ##
    import matplotlib.pyplot as plt
    import numpy as np
    ## LOCAL APPLICATION ##

    ################ >ACTION(S) ################
    colors = [
        {'green' : '#859900'},
        {'blue' : '#268bd2'},
        {'red' : '#dc322f'},
        {'gray' : '#D2D1D1'},
        {'orange' : '#cb4b16'},
        {'violet' : '#6c71c4'},
        {'cyan' : '#2aa198'},
        {'magenta' : '#d33682'},
        {'yellow' : '#b58900'}
    ]

    # FORCE SQUARE FIGURE AND SQUARE AXES LOOKS BETTER FOR POLAR
    fig = plt.figure(
        num=None,
        figsize=(8,8),
        dpi=None,
        facecolor=None,
        edgecolor=None,
        frameon=True)

    ax = fig.add_axes(
        [0.1, 0.1, 0.8, 0.8],
        polar=True,
        frameon=circumference)

    ax.set_ylim(0, radius)
    # ax.get_xaxis().set_visible(circumference)

    if circleTicksRange:
        circleTicks = np.arange(circleTicksRange[0], circleTicksRange[1], circleTicksRange[2])
    tickLabels = []
    for tick in circleTicks:
        tickLabels.append(".")

    plt.xticks(2*np.pi*circleTicks/360., tickLabels)

    count = 0
    for k, v in dataDictionary.iteritems():
        if count <= len(colors):
            colorDict = colors[count]
            count += 1
        else:
            count = 0
            colorDict = colors[count]

        thetaList = []
        twoPi = 2.*np.pi
        for i in range(len(v)):
            thetaList.append(twoPi*np.random.rand())
        thetaArray = np.array(thetaList)

        x = thetaArray
        y = v

        plt.scatter(
            x,
            y,
            label=k,
            s=50,
            c=colorDict.values(),
            marker='o',
            cmap=None,
            norm=None,
            vmin=None,
            vmax=None,
            alpha=0.5,
            linewidths=None,
            edgecolor='#657b83',
            verts=None,
            hold=True)

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(0.7, -0.1), prop={'size':8})
    plt.grid(True)
    plt.title(title)
    if prependNum:
        title = "%02d_%s" % (prependNum, title)
    thisTitle = title.replace(" ", "_")
    thisTitle = thisTitle.replace("-", "_")
    fileName = pathToOutputPlotsFolder + thisTitle + ".png"
    imageLink = """
![%s_plot](%s)

""" % (thisTitle, fileName)
    plt.savefig(fileName)
    plt.clf()  # clear figure

    return imageLink



###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()


###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
