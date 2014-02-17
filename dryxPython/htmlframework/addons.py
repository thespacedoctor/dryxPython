#!/usr/bin/python
# -*- coding: utf-8 -*-

""" addons.py
===============================
:Summary:

:Author:
    David Young

:Date Created:
    20130508

:dryx syntax:
    - ``xxx`` = come back here and do some more work
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this code please email me: d.r.young@qub.ac.uk """

# from . import *

###################################################################
# CLASSES                                                         #
###################################################################
###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
## LAST MODIFIED : 20130508
## CREATED : 20130508
## AUTHOR : DRYX


def mediaObject(
    displayType='div',
    img='',
    headlineText='',
    otherContent=False,
    nestedMediaObjects=False,
):
    """ Generate an abstract object style for building various types of components (like blog comments, Tweets, etc) that feature a left- or right-aligned image alongside textual content.

    **Key Arguments:**
        - ``displayType`` -- the display style of the media object [ "div" | "li" ]
        - ``img`` -- the image to include
        - ``headlineText`` -- the headline text for the object
        - ``otherContent`` -- other content to be displayed inside the media object
        - ``nestedMediaObjects`` -- nested media objects to be appended

    **Return:**
        - ``media`` -- the media object """

    falseList = [nestedMediaObjects]

    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""

    [nestedMediaObjects] = falseList

    if not otherContent:
        otherContent = ""

    mediaObject = \
        """
        <%(displayType)s class="media" id="  ">
            %(img)s
            <div class="media-body">
                <h4 class="media-heading">%(headlineText)s</h4>
                %(otherContent)s
                <!-- Nested media object -->
                %(nestedMediaObjects)s
            </div>
        </%(displayType)s>""" \
        % locals()
    return mediaObject


## LAST MODIFIED : 20130508
## CREATED : 20130508
## AUTHOR : DRYX

def well(
        wellText='',
        wellSize='default'):
    """Get well. Use the well as a simple effect on an element to give it an inset effect.

    **Key Arguments:**
        - ``wellText`` -- the text to be displayed in the well
        - ``wellSize`` -- the size of the well [ "default" | "large" | "small" ]

    **Return:**
        - ``well`` -- the well """

    if wellSize == 'default':
        wellSize = ''
    else:
        wellSize = 'well-%(wellSize)s' % locals()
    well = """
        <div class="well %(wellSize)s" id="  ">
            %(wellText)s
        </div>""" % locals()
    return well


## LAST MODIFIED : 20130508
## CREATED : 20130508
## AUTHOR : DRYX

def closeIcon():
    """Get close icon. The generic close icon for dismissing content like modals and alerts.

    **Key Arguments:**

    **Return:**
        - ``closeIcon`` -- the closeIcon """

    closeIcon = """<button class="close">&times;</button>"""
    return closeIcon


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################
###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
