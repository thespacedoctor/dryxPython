# #!/usr/bin/env python
# encoding: utf-8
"""
imagingModal.py
===============
:Summary:
    An image and modal -- click on the image to present the modal of the larger image with download options

:Author:
    David Young

:Date Created:
    April 30, 2014

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
import numpy as np
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil
from ..__init__ import *

###################################################################
# CLASSES                                                         #
###################################################################


class imagingModal():

    """
    An image and modal -- click on the image to present the modal of the larger image with download options

    **Key Arguments:**
        - ``dbConn`` -- mysql database connection
        - ``log`` -- logger
        - ``display`` -- [ rounded | circle | polaroid | False ]
        - ``imagePath`` -- path to the image to be displayed
        - ``modalHeaderContent`` -- the heading for the modal
        - ``modalFooterContent`` -- the footer (usually buttons)

    **Todo**
        - @review: when complete, clean imagingModal class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    ## Variable Data Atrributes

    ## Override Variable Data Atrributes

    ## Initialisation
    def __init__(
            self,
            log,
            dbConn=False,
            imagePath=False,
            display=False,
            modalHeaderContent="",
            modalFooterContent="",
    ):
        self.log = log
        self.dbConn = dbConn
        self.imagePath = imagePath
        self.display = display
        self.modalHeaderContent = modalHeaderContent
        self.modalFooterContent = modalFooterContent
        self.randomNum = np.random.randint(300000000)
        # x-self-arg-tmpx
        return None

    ## Method Attributes
    def get(self):
        """get the object
    
        **Return:**
            - ``imageModal``
    
        **Todo**
            - @review: when complete, clean this method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')
        ## TEST THE ARGUMENTS

        thisImage = self._create_image()
        thisModal = self._create_modal()

        ## VARIABLES ##

        self.log.info('completed the ``get`` method')
        return thisImage + thisModal

    def _create_image(
            self):
        """create the html for the image
    
        **Return:**
            - None
    
        **Todo**
            - @review: when complete, clean create_image method
            - @review: when complete add logging
        """
        self.log.info('starting the ``create_image`` method')

        if not self.imagePath:
            self.imagePath = 'holder.js/200x200/auto/industrial/text:placeholder'

        thisImage = image(
            src=self.imagePath,  # [ industrial | gray | social ]
            href=False,
            display=self.display,  # [ rounded | circle | polaroid | False ]
            pull=False,  # [ "left" | "right" | "center" | False ]
            htmlClass=False,
            width=False,
            thumbnail=True
        )

        randNum = self.randomNum

        thisImage = a(
            content=thisImage,
            href="#modal%(randNum)s" % locals(),
            tableIndex=False,
            triggerStyle="modal",  # [ False | "dropdown" | "tab" ]
            htmlClass=False,
            postInBackground=False,
        )

        self.log.info('completed the ``create_image`` method')
        return thisImage

    def _create_modal(
            self):
        """create modal
    
        **Key Arguments:**
            # -
    
        **Return:**
            - ``imageModal`` -- the image modal
    
        **Todo**
            - @review: when complete, clean create_modal method
            - @review: when complete add logging
        """
        self.log.info('starting the ``create_modal`` method')

        thisImage = self._create_image()
        thisImage = row_adjustable(
            span=10,
            offset=1,
            content=thisImage,
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        fileUrl = self.imagePath
        basename = os.path.basename(self.imagePath)
        downloadFileButton = button(
            buttonText="""<i class="icon-file-pdf"></i>""",
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='primary',
            buttonSize='small',  # [ large | default | small | mini ]
            htmlId=False,
            href="/marshall/scripts/python/download_file.py?url=%(fileUrl)s" % locals(),
            pull=False,  # right, left, center
            submit=False,
            block=False,
            disable=False,
            dataToggle=False,  # [ modal ]
            popover=False
        )

        randNum = self.randomNum
        imageModal = modal(
            modalHeaderContent=self.modalHeaderContent,
            modalBodyContent=thisImage,
            modalFooterContent=self.modalFooterContent + downloadFileButton,
            htmlId="modal%(randNum)s" % locals(),
            centerContent=True,
            htmlClass=False
        )

        self.log.info('completed the ``create_modal`` method')
        return imageModal

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
