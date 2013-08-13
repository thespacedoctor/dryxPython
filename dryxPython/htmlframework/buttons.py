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
# xxx-replace
## LAST MODIFIED : March 12, 2013
## CREATED : March 12, 2013
## AUTHOR : DRYX
def get_button(size="large",
                block=False,
                color="blue",
                text="button",
                htmlId=False,
                htmlClass=False,
                extraAttr=False,
                disabled=False):
    """The button method (bases on the twitter bootstrap buttons)

    **Key Arguments:**
        - ``size`` - button size - mini, small, default, large
        - ``block`` - block button?
        - ``color`` - color
        - ``text`` - button text
        - ``htmlId`` -- the name of the button
        - ``htmlClass`` -- the class of the button
        - ``disabled`` -- disable the button if true (flatten & unclickable)

    **Return:**
        - ``button``
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ################ > VARIABLE SETTINGS ######
    size = "btn-%s" % (size,)
    if block:
        block = "btn-block"
    else:
        block = ""
    if htmlId:
        htmlId = """id="%s" """ % (htmlId,)
    else:
        htmlId = ""
    if not htmlClass: htmlClass = ""
    if not extraAttr:
        extraAttr = ""
    if disabled:
        disabled = "disabled"
    else:
        disabled = ""

    color = "btn-%s" % (color,)

    ################ >ACTION(S) ################
    button = """
        <button class="btn %s %s %s %s %s" %s %s type="button">
        %s
        </button>""" % (size, block, color, htmlClass, disabled, htmlId, extraAttr, text)

    return button

# xxx-replace
## LAST MODIFIED : March 12, 2013
## CREATED : March 12, 2013
## AUTHOR : DRYX
# def get_linked_button(size="large",
#                 block=False,
#                 color="blue",
#                 text="button",
#                 href="#",
#                 htmlId=False,
#                 htmlClass=False,
#                 extraAttr=False,
#                 disabled=False):
#     """The button method (bases on the twitter bootstrap buttons)

#     **Key Arguments:**
#         - ``size`` - button size - mini, small, default, large
#         - ``block`` - block button?
#         - ``color`` - color
#         - ``text`` - button text
#         - ``href`` - the link
#         - ``htmlId`` -- the name of the button
#         - ``htmlClass`` -- the class of the button

#     **Return:**
#         - ``link_button``
#     """
#     ################ > IMPORTS ################
#     ## STANDARD LIB ##
#     ## THIRD PARTY ##
#     ## LOCAL APPLICATION ##

#     ################ > VARIABLE SETTINGS ######
#     size = "btn-%s" % (size,)
#     if block:
#         block = "btn-block"
#     else:
#         block = ""
#     if htmlId:
#         htmlId = """id="%s" """ % (htmlId,)
#     else:
#         htmlId = ""
#     if not htmlClass: htmlClass = ""
#     if not extraAttr:
#         extraAttr = ""
#     if disabled:
#         disabled = "disabled"
#     else:
#         disabled = ""

#     color = "btn-%s" % (color,)


#     ################ >ACTION(S) ################
#     link_button = """
#         <a href="%s" class="btn %s %s %s %s %s" %s %s>%s</a>""" % (href, size, block, color, htmlClass, disabled, htmlId, extraAttr, text)

#     return link_button


## LAST MODIFIED : April 25, 2013
## CREATED : April 25, 2013
## AUTHOR : DRYX
def button(
        buttonText="",
        buttonStyle="default",
        buttonSize="default",
        href=False,
        submit=False,
        block=False,
        disable=False):
    """Generate a button - TBS style

    **Key Arguments:**
        - ``buttonText`` -- the text to display on the button
        - ``buttonStyle`` -- the style of the button required [ default | primary | info | success | warning | danger | inverse | link ]
        - ``buttonSize`` -- the size of the button required [ large | small | mini ]
        - ``href`` -- link the button to another location?
        - ``submit`` -- set to true if a form button [ true | false ]
        - ``block`` -- create block level buttons—those that span the full width of a parent [ True | False ]
        - ``disable`` -- this class is only for aesthetic; you must use custom JavaScript to disable links here

    **Return:**
        - ``button`` -- the button
    """
    if buttonStyle == "default":
        buttonStyle = ""
    else:
        buttonStyle = "btn-%s" % (buttonStyle,)

    if buttonSize == "default":
        buttonSize = ""
    else:
        buttonSize = "btn-%s" % (buttonSize,)

    if block is True:
        block = "btn-block"
    else:
        block = ""

    if disable is True:
        disable = "disable"
    else:
        disable = ""

    if submit is True:
        submit = """type="submit" """
    else:
        submit = ""

    if href:
        elementOpen = """a href="%s" """ % (href,)
        elementClose = """a"""
    else:
        elementOpen = """button type="button" """
        elementClose = """button"""

    button = """
        <%s class="btn %s %s %s %s" id="  " %s >
            %s
        </%s>""" % (elementOpen, buttonStyle, buttonSize, block, disable, submit, buttonText, elementClose)

    return button


## LAST MODIFIED : April 29, 2013
## CREATED : April 29, 2013
## AUTHOR : DRYX
def buttonGroup(
        buttonList="",
        format="default"):
    """Generate a buttonGroup - TBS style

    **Key Arguments:**
        - ``buttonList`` -- a list of buttons
        - ``format`` -- format of the button [ default | toolbar | vertical ]

    **Return:**
        - ``buttonGroup`` -- the buttonGroup
    """
    thisButtonList = ""
    for button in buttonList:
        thisButtonList += button

    if format is "vertical":
        vertical = "btn-group-vertical"
    else:
        vertical = ""

    buttonGroup = """
        <div class="btn-group %s" id="  ">
            %s
        </div>""" % (vertical, buttonList,)

    if format == "toolbar":
        buttonGroup = """
        <div class="btn-toolbar">
            %s
        </div>""" % (buttonGroup,)

    return buttonGroup


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
