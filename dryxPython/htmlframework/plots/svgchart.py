#!/usr/bin/env python
# encoding: utf-8
"""
svgchart.py
===========
:Summary:
    Add an SVG chart placeholder to the HTML of your webpage

:Author:
    David Young

:Date Created:
    May 9, 2014

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
# CLASSES                                                         #
###################################################################
# x-class-module-worker-tmpx
# class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# x-worker-def
## LAST MODIFIED : May 9, 2014
## CREATED : May 9, 2014
## AUTHOR : DRYX
def svgchart(
    htmlClass=False,
    csvUrl="#",
    disable=False,
    htmlId=False,
    chartType=""
):
    """svgchart

    **Key Arguments:**
        - ``htmlClass`` -- the extra html classes required
        - ``disable`` -- disable the plot (can enable via javascript)
        - ``htmlId`` -- the html id if required
        - ``csvUrl`` -- url to a csv file/csv data
        - ``chartType`` -- the type of chart required (determines which javascript function to trigger)

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean svgchart function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    if not htmlClass:
        htmlClass = ""

    if htmlId:
        htmlId = """id="%(htmlId)s" """ % locals()
    else:
        htmlId = ""

    if disable:
        disable = "true"
    else:
        disable = "false"

    svg = """<svg class="chart %(htmlClass)s %(chartType)s" %(htmlId)s data-src="%(csvUrl)s" disable="%(disable)s"></svg>""" % locals()

    return svg

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
