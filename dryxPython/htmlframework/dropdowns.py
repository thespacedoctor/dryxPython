#!/usr/local/bin/python
# encoding: utf-8
"""
dropdowns.py
=================================
:Summary:
    Dropdown for TBS htmlframework

:Author:
    David Young

:Date Created:
    March 15, 2013

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
##################################################################


## LAST MODIFIED : March 8, 2013
## CREATED : March 8, 2013
## AUTHOR : DRYX
def dropdown(
        buttonSize="default",
        buttonColor="default",
        menuTitle="#",
        splitButton=False,
        splitButtonHref=False,
        linkList=[],
        separatedLinkList=False,
        pull=False,
        htmlId=False,
        htmlClass=False,
        direction="down",
        popover=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True):
    """get a toggleable, contextual menu for displaying lists of links. Made interactive with the dropdown JavaScript plugin. You need to wrap the dropdown's trigger and the dropdown menu within .dropdown, or another element that declares position: relative;

    - ``buttonSize`` -- size of button [ mini | small | default | large ]
    - ``buttonColor`` -- [ default | sucess | error | warning | info ]
    - ``menuTitle`` -- the title of the menu
    - ``splitButton`` -- split the button into a separate action button and a dropdown
    - ``splitButtonHref`` -- link for the split button
    - ``linkList`` -- a list of (linked) items items that the menu should display
    - ``separatedLinkList`` -- a list of (linked) items items that the menu should display below divider
    - ``pull`` -- [ false | right | left ] (e.g Add ``right`` to a ``.dropdown-menu`` to right align the dropdown menu.)
    - ``direction`` -- drop [ down | up ]
    - ``popover`` -- add a popover for this dropdown
    - ``onPhone`` -- does this container get displayed on a phone sized screen
    - ``onTablet`` -- does this container get displayed on a tablet sized screen
    - ``onDesktop`` -- does this container get displayed on a desktop sized screen

      **Return:**
        - ``dropdown`` -- the dropdown menu
    """
    # Twitter Bootstrap notes
    # ------------------------
    # Add .pull-right to a .dropdown-menu to right align the dropdown menu.
    # Add .disabled to a <li> in the dropdown to disable the link.
    # Add .dropdown-submenu to any li in an existing dropdown menu for
    # automatic styling.
    thisLinkList = ""
    for link in linkList:
        link = link.replace('<a ', '<a tabindex="-1"')
        thisLinkList = """%(thisLinkList)s %(link)s""" % locals()

    thisSeparatedLinkList = ""
    if separatedLinkList:
        thisSeparatedLinkList = """<li class="divider"></li>"""
        for link in separatedLinkList:
            thisSeparatedLinkList = """%(thisSeparatedLinkList)s %(link)s""" % locals(
            )

    thisLinkList = "%(thisLinkList)s %(thisSeparatedLinkList)s" % locals()

    if buttonSize == "default":
        buttonSize = ""
    else:
        buttonSize = "btn-%(buttonSize)s" % locals()

    buttonColor = "btn-%(buttonColor)s" % locals()

    if htmlId is False:
        htmlId = ""
    else:
        htmlId = """id="%(htmlId)s" """ % locals()

    if htmlClass is False:
        htmlClass = ""

    if direction == "up":
        direction = "dropup"
    else:
        direction = ""

    if popover is False:
        popover = ""

    if splitButton:
        content = """class="btn %(buttonSize)s %(buttonColor)s" %(popover)s>%(menuTitle)s""" % locals(
        )
        if splitButtonHref is not False:
            topButton = """<a href="%(splitButtonHref)s" %(content)s</a>""" % locals()
        else:
            topButton = """<button %(content)s</button>""" % locals()

        dropdownButton = """
            %(topButton)s
            <button class="btn %(buttonSize)s %(buttonColor)s dropdown-toggle" data-toggle="dropdown">
                <span class="caret"></span>
            </button>""" % locals()
        popover = ""
    else:
        dropdownButton = """
            <button class="btn %(buttonSize)s %(buttonColor)s dropdown-toggle" %(popover)s data-toggle="dropdown" href="#">
              %(menuTitle)s
              <span class="caret"></span>
            </button>""" % locals()

    if pull:
        pull = """pull-%(pull)s""" % locals()
    else:
        pull = ""

    if onPhone:
        onPhone = ""
    else:
        onPhone = "hidden-phone"
    if onTablet:
        onTablet = ""
    else:
        onTablet = "hidden-tablet"
    if onDesktop:
        onDesktop = ""
    else:
        onDesktop = "hidden-desktop"

    dropdown = """
        <div class="btn-group %(pull)s %(onPhone)s %(onTablet)s %(onDesktop)s %(direction)s %(htmlClass)s" %(htmlId)s>
            %(dropdownButton)s
            <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu">
                <!-- dropdown menu links -->
                %(thisLinkList)s
          </ul>
        </div>""" % locals()

    return dropdown

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()


###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
