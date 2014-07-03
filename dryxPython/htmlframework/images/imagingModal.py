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
from .. import modals
from . import image

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
        - ``stampWidth`` -- 180
        - ``modalImageWidth`` -- 400
        - ``downloadFilename`` -- False
    """
    ## Initialisation

    def __init__(
            self,
            log,
            dbConn=False,
            imagePath=False,
            display=False,
            modalHeaderContent="",
            modalFooterContent="",
            modalFooterButtons=[],
            stampWidth=180,
            modalImageWidth=400,
            downloadFilename=False
    ):
        self.log = log
        self.dbConn = dbConn
        self.imagePath = imagePath
        self.display = display
        self.modalHeaderContent = modalHeaderContent
        self.modalFooterContent = modalFooterContent
        self.randomNum = np.random.randint(300000000)
        self.stampWidth = stampWidth
        self.modalImageWidth = modalImageWidth
        self.downloadFilename = downloadFilename
        self.modalFooterButtons = modalFooterButtons
        # x-self-arg-tmpx
        return None

    def close(self):
        del self
        return None

    ## Variable Data Atrributes

    ## Override Variable Data Atrributes

    ## Method Attributes
    def get(self):
        """get the object
    
        **Return:**
            - ``imageModal``
        """
        self.log.info('starting the ``get`` method')

        ## create imaging modal and associated image and return them
        thisImage = self._create_image(width=self.stampWidth)
        thisModal = self._create_modal()

        self.log.info('completed the ``get arse`` method')
        return thisImage + thisModal

    def _create_image(
            self,
            width=False):
        """create the html for the image

         - ``width`` -- image width
    
        **Return:**
            - ``thisImage`` -- the image created
        """
        self.log.info('starting the ``create_image`` method')

        ## add placeholder as default image
        if not self.imagePath:
            self.imagePath = 'holder.js/200x200/auto/industrial/text:placeholder'

        ## create html code for the image
        thisImage = image(
            src=self.imagePath,  # [ industrial | gray | social ]
            href=False,
            display=self.display,  # [ rounded | circle | polaroid | False ]
            pull=False,  # [ "left" | "right" | "center" | False ]
            htmlClass=False,
            width=width,
            thumbnail=True
        )

        ## link the image to the associated modal with a random number tag
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
        """
        self.log.info('starting the ``create_modal`` method')

        ## grab the associated image and place in a wrapper row
        thisImage = self._create_image(width=self.modalImageWidth)
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

        ## generate the download button for the modal footer
        fileUrl = self.imagePath

        thisPopover = popover(
            tooltip=True,
            placement="bottom",  # [ top | bottom | left | right ]
            trigger="hover",  # [ False | click | hover | focus | manual ]
            title="download image",
            content=False,
            delay=200
        )

        if self.downloadFilename:
            downloadFilename = self.downloadFilename
            downloadFilename = "&fileName=%(downloadFilename)s" % locals()
            downloadFileButton = button(
                buttonText="""<i class="icon-file-pdf"></i>""",
                # [ default | primary | info | success | warning | danger | inverse | link ]
                buttonStyle='primary',
                buttonSize='small',  # [ large | default | small | mini ]
                htmlId=False,
                href="/marshall/scripts/python/download_file.py?url=%(fileUrl)s%(downloadFilename)s" % locals(),
                pull=False,  # right, left, center
                submit=False,
                block=False,
                disable=False,
                dataToggle=False,  # [ modal ]
                popover=thisPopover
            )
        else:
            downloadFileButton = ""

        buttonList = [downloadFileButton]
        buttonList.extend(self.modalFooterButtons)

        thisButtonGroup = buttonGroup(
            buttonList=buttonList,
            format='default'  # [ default | toolbar | vertical ]
        )

        ## create the modal with the correct trigger tag
        randNum = self.randomNum
        imageModal = modals.modal(
            modalHeaderContent=self.modalHeaderContent,
            modalBodyContent=thisImage,
            modalFooterContent=self.modalFooterContent + thisButtonGroup,
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
