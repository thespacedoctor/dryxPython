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


###################################################################
# CLASSES                                                         #
###################################################################
###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : 20130508
# CREATED : 20130508
# AUTHOR : DRYX


def mediaObject(
    displayType='div',
    imagePath='',
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

    thisImage = images.image(
        src=imagePath,  # [ industrial | gray | social ]
        href=False,
        display="polaroid",  # [ rounded | circle | polaroid | False ]
        pull="left",  # [ "left" | "right" | "center" | False ]
        htmlClass=False,
        width=False
    )

    thisImage = """<img src="%(imagePath)s" class="pull-left" style="width: 128px;">""" % locals(
    )

    thisImage = images.image(
        src=imagePath,
        href=imagePath,
        display="polaroid",  # [ rounded | circle | polaroid ]
        pull="left",  # [ "left" | "right" | "center" ]
        htmlClass=False,
        htmlId=False,
        thumbnail=True,
        width=150,
        height=False,
    )

    mediaObject = \
        """
        <%(displayType)s class="media" id="  ">
            %(thisImage)s
            <div class="media-body">
                <h4 class="media-heading">%(headlineText)s</h4>
                %(otherContent)s
                <!-- Nested media object -->
                %(nestedMediaObjects)s
            </div>
        </%(displayType)s>""" \
        % locals()
    return mediaObject


# LAST MODIFIED : 20130508
# CREATED : 20130508
# AUTHOR : DRYX

def well(
        wellText='',
        wellSize='default',
        htmlId=False,
        htmlClass=False):
    """Get well. Use the well as a simple effect on an element to give it an inset effect.

    **Key Arguments:**
        - ``wellText`` -- the text to be displayed in the well
        - ``wellSize`` -- the size of the well [ "default" | "large" | "small" ]

    **Return:**
        - ``well`` -- the well """

    if htmlId is False:
        htmlId = ""
    else:
        htmlId = """id="%(htmlId)s" """ % locals()

    if htmlClass is False:
        htmlClass = ""

    if wellSize == 'default':
        wellSize = ''
    else:
        wellSize = 'well-%(wellSize)s' % locals()
    well = """
        <div class="well %(wellSize)s %(htmlClass)s" %(htmlId)s>
            %(wellText)s
        </div>""" % locals()
    return well


# LAST MODIFIED : 20130508
# CREATED : 20130508
# AUTHOR : DRYX

def closeIcon():
    """Get close icon. The generic close icon for dismissing content like modals and alerts.

    **Key Arguments:**

    **Return:**
        - ``closeIcon`` -- the closeIcon """

    closeIcon = """<button class="close">&times;</button>"""
    return closeIcon

# LAST MODIFIED : February 25, 2014
# CREATED : February 25, 2014
# AUTHOR : DRYX


def popover(
        tooltip=False,
        placement=False,
        trigger=False,
        title=False,
        content=False,
        delay=200,
        after=False):
    """popover to provide helper text or some secondary info about an element

    **Key Arguments:**
        - ``tooltip`` -- use tooltip instead of popover
        - ``placement`` -- direction popover expands into [ top | bottom | left | right ]
        - ``trigger`` -- the trigger for the popover [ False | click | hover | focus | manual ]
        - ``title`` -- the popover title
        - ``content`` -- the popover content
        - ``delay`` -- delay in ms
        - ``after`` -- place the div required by the 


    **Return:**
        - ``popover`` - the popover helper text to be added to an element

    **Todo**
        - [ ] when complete, clean popover function
        - [ ] when complete add logging
        - [ ] when complete, decide whether to abstract function to another module
    """

    if tooltip is False:
        tooltip = "popover"
        # title = """data-original-title="%(title)s" """ % locals()
    else:
        tooltip = "tooltip"
        content = False

    popover = """rel="%(tooltip)s" data-container="body" data-placement="%(placement)s" """ % locals()
    if trigger is not False:
        popover = """%(popover)s data-trigger="%(trigger)s" """ % locals()
    if title is not False:
        popover = """%(popover)s data-original-title="%(title)s" """ % locals()
    if content is not False:
        popover = """%(popover)s data-content="%(content)s" """ % locals()
    if delay is not False:
        popover = """%(popover)s data-delay="%(delay)s" """ % locals()

    return popover


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################
###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################


from . import images
