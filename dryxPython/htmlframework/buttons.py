#!/usr/bin/python
# encoding: utf-8
"""
_dryxTBS_buttons
===============================
:Summary:
    Buttons partial for the dryxTwitterBootstrap module

:Author:
    David Young

:Date Created:
    April 25, 2013

:dryx syntax:
    - ``xxx`` = come back here and do some more work
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script please email me: d.r.young@qub.ac.uk
"""

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
## LAST MODIFIED : April 25, 2013
## CREATED : April 25, 2013
## AUTHOR : DRYX


def button(
        buttonText="",
        buttonStyle="default",
        buttonSize="default",
        htmlId=False,
        htmlClass=False,
        href=False,
        pull=False,
        submit=False,
        block=False,
        disable=False,
        dataToggle=False,
        popover=False,
        postInBackground=False,
        notification=False,
        close=False,
        formId=False):
    """Generate a button - TBS style

    **Key Arguments:**
        - ``buttonText`` -- the text to display on the button
        - ``buttonStyle`` -- the style of the button required [ default | primary | info | success | warning | danger | inverse | link ]
        - ``buttonSize`` -- the size of the button required [ large | small | mini ]
        - ``htmlId`` -- the htmlId for the button
        - ``href`` -- link the button to another location?
        - ``pull`` -- left, right or center
        - ``submit`` -- set to true if a form button [ true | false ]
        - ``block`` -- create block level buttons—those that span the full width of a parent [ True | False ]
        - ``disable`` -- this class is only for aesthetic; you must use custom JavaScript to disable links here
        - ``dataToggle`` -- for use with js to launch, for example, a modal
        - ``popover`` -- add a popover element for this button

    **Return:**
        - ``button`` -- the button
    """
    if buttonStyle == "default":
        buttonStyle = ""
    else:
        buttonStyle = "btn-%(buttonStyle)s" % locals()

    if htmlClass is False:
        htmlClass = ""

    if buttonSize == "default":
        buttonSize = ""
    else:
        buttonSize = "btn-%(buttonSize)s" % locals()

    if notification is False:
        notification = ""
    else:
        notification = """notification="%(notification)s" """ % locals()

    if block is True:
        block = "btn-block"
    else:
        block = ""

    if postInBackground is True:
        postInBackground = "postInBackground"
    else:
        postInBackground = ""

    if disable is True:
        disable = "disabled"
    else:
        disable = ""

    if submit is True:
        ttype = "submit"
    else:
        ttype = "button"

    if formId is False:
        formId = ""
    else:
        formId = """formId="%(formId)s" """ % locals()

    if close is False:
        close = ""
        dismiss = ""
    else:
        close = "close"
        dismiss = 'data-dismiss="modal"'

    if not dataToggle:
        dataToggle = ""
    else:
        dataToggle = """data-toggle="%(dataToggle)s" """ % locals()

    if href:
        elementOpen = """a href="%(href)s" type="%(ttype)s" """ % locals()
        elementClose = """a"""
    else:
        elementOpen = """button type="%(ttype)s" """ % locals()
        elementClose = """button"""

    if htmlId == False:
        htmlId = ""

    if pull == False:
        pull = ""
    else:
        pull = "pull-%(pull)s" % locals()

    if popover is False:
        popover = ""

    if len(dataToggle):
        popover = popover.replace("data-toggle", "rel")

    button = """<%(elementOpen)s class="%(htmlClass)s btn %(close)s %(buttonStyle)s %(buttonSize)s %(block)s %(disable)s %(pull)s %(postInBackground)s" %(popover)s id="%(htmlId)s" %(formId)s %(dataToggle)s %(dismiss)s %(notification)s>%(buttonText)s</%(elementClose)s>""" % locals()

    return button


## LAST MODIFIED : April 29, 2013
## CREATED : April 29, 2013
## AUTHOR : DRYX
def buttonGroup(
        buttonList=[],
        format="default",
        pull=False):
    """Generate a buttonGroup - TBS style

    **Key Arguments:**
        - ``buttonList`` -- a list of buttons
        - ``format`` -- format of the button [ default | toolbar | vertical ]

    **Return:**
        - ``buttonGroup`` -- the buttonGroup
    """
    thisButtonList = ""
    count = 1
    for button in buttonList:
        thisButtonList = "%(thisButtonList)s %(button)s" % locals()
        count += 1

    if pull is not False:
        pull = "pull-%(pull)s" % locals()
    else:
        pull = ""

    if format == "vertical":
        vertical = "btn-group-vertical"
    else:
        vertical = ""

    toolbar = ""
    if format == "toolbar":
        toolbar = "btn-toolbar"

    buttonGroup = """
        <div class="btn-group %(vertical)s %(toolbar)s %(pull)s"  id="  ">
            %(thisButtonList)s
        </div>""" % locals()

    return buttonGroup


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
