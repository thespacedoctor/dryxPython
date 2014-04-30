#!/usr/bin/env python
# encoding: utf-8
"""
imageWell.py
=============
:Summary:
    Class to generate a well of images

:Author:
    David Young

:Date Created:
    April 29, 2014

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
import math
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil
from ..__init__ import *
from imagingModal import imagingModal


###################################################################
# CLASSES                                                         #
###################################################################


class imageWell():

    """
    Framework for a bootstrap style well containing thumbnail images that can be clicked on to reveal a modal of more imformation

    **Key Arguments:**
        - ``log`` -- logger
        - ``title`` -- Title of Image Well
        - ``description`` -- Description of the content of the image well
        - ``imageDisplay`` -- [ rounded | circle | polaroid | False ]

    **Todo**
        - @review: when complete, clean imageWell class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    ## Variable Data Atrributes
    imageSpan = 2
    rowLength = 0
    imageColumns = []

    ## Override Variable Data Atrributes

    ## Initialisation
    def __init__(
            self,
            log,
            title="Title of Image Well",
            description="Description of the content of the image well",
            imageDisplay="rounded"
    ):
        self.log = log
        self.description = description
        self.title = title
        self.description = description
        self.imageDisplay = imageDisplay

        return None

    ## Method Attributes
    def get(self):
        """get the image well
    
        **Key Arguments:**
            # -
    
        **Return:**
            - None
    
        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')
        ## TEST THE ARGUMENTS

        ## VARIABLES ##
        self.title = pageHeader(
            headline=self.title,
            tagline=self.description
        )

        numImages = len(self.imageColumns)
        colPerRow = int(math.floor(12 / self.imageSpan))
        numRows = int(math.ceil(float(numImages) / float(colPerRow)))

        theseRows = ""
        for r in range(int(numRows)):
            startC = r * colPerRow
            endC = startC + colPerRow
            columns = " ".join(self.imageColumns[startC:endC])
            thisRow = grid_row(
                responsive=True,
                columns=columns,
                htmlId=False,
                htmlClass=False,
                onPhone=True,
                onTablet=True,
                onDesktop=True
            )
            theseRows = """%(theseRows)s %(thisRow)s""" % locals()

        content = grid_row(
            responsive=True,
            columns=theseRows,
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        imageWell = well(
            wellText=self.title + content,
            wellSize='large',  # [ "default" | "large" | "small" ]
            htmlId=False,
            htmlClass="imagewell"
        )

        imageWellRow = grid_row(
            responsive=True,
            columns=imageWell,
            htmlId=False,
            htmlClass="imagewell-row",
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        self.log.info('completed the ``get`` method')
        return  """%(imageWellRow)s""" % locals()

    # use the tab-trigger below for new method
    def appendImage(
            self,
            imagePath,
            imageTitle,
            modalHeaderContent="",
            modalFooterContent=""):
        """appendImage
    
        **Key Arguments:**
            - ``imagePath`` -- path to the image to add to the well
            - ``imageTitle`` -- text to tag the image with
            - ``modalHeaderContent`` -- the heading for the modal
            - ``modalFooterContent`` -- the footer (usually buttons)
    
        **Return:**
            - None
    
        **Todo**
            - @review: when complete, clean appendImage method
            - @review: when complete add logging
        """
        self.log.info('starting the ``appendImage`` method')
        ## TEST THE ARGUMENTS

        ## VARIABLES ##

        thisImage = imagingModal(
            log=self.log,
            imagePath=imagePath,
            display=self.imageDisplay,
            modalHeaderContent=modalHeaderContent,
            modalFooterContent=modalFooterContent,)
        thisImage = thisImage.get()

        ## add text color
        imageTitle = coloredText(
            text=imageTitle,
            color="lightgrey",
            size=3,  # 1-10
            pull="left",  # "left" | "right"
        )

        imageTitle = row_adjustable(
            span=12,
            offset=self.imageSpan - 1,
            content=imageTitle,
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        content = "%(thisImage)s<br>%(imageTitle)s" % locals()

        column = grid_column(
            span=self.imageSpan,  # 1-12
            offset=0,  # 1-12
            content=content,
        )

        self.imageColumns.append(column)

        self.log.info('completed the ``appendImage`` method')
        return None

    # use the tab-trigger below for new method
    # method-tmpx

    ## Override Method Attributes
    # method-override-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################

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
