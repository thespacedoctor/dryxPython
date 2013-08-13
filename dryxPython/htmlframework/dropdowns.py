#!/usr/local/bin/python
# encoding: utf-8
"""
_dryxTBS_dropdowns
=================================
:Summary:
    Dropdown menus partial for the dryxTwitterBootstrap module

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
###################################################################
# xxx-replace
## LAST MODIFIED : December 17, 2012
## CREATED : December 17, 2012
## AUTHOR : DRYX
def get_dropdown_menu_for(dbConn, log, menuName, title, linkList):
  """Generate a dropdown menu with the provided list of links.

  **Key Arguments:**
    - ``dbConn`` -- mysql database connection
    - ``log`` -- logger
    - ``menuName`` -- the name of the menu
    - ``title`` -- the title of the menu
    - ``linkList`` -- a list of links that the menu should display

  **Return:**
    - ``menu`` -- the dropdown menu
  """
  ################ > IMPORTS ################
  import ordereddict as c # REMOVE WHEN PYTHON 2.7 INSTALLED ON PSDB
  #import collections as c

  ################ > VARIABLE SETTINGS ######
  gh = lambda x: get_html_block(x)

  ################ >ACTION(S) ################
  ## BUTTONS
  buttonDict = {}
  i=0
  for item in linkList:
    key = ('%05i' % i)
    buttonDict[key] = dict(
                            tag="div",
                            htmlClass=menuName+'MenuButton',
                            blockContent=item
                          )
    i += 1

  blockDict = {}
  blockDict[menuName+'Hover'] = gh(
                                    dict (
                                          tag="div",
                                          htmlClass='dropDownMenu',
                                          htmlId=menuName+'Hover',
                                          blockContent = title
                                    )
                                  )

  obuttonDict = c.OrderedDict(sorted(buttonDict.items()))

  blockContent = blockDict[menuName+'Hover']
  for k, v in obuttonDict.iteritems():
    blockContent += gh(v)

  blockDict[menuName+'SubItems'] = gh(
                                        dict (
                                              tag="div",
                                              htmlClass='dropDownMenu',
                                              htmlId=menuName+'SubItems',
                                              blockContent=blockContent
                                        )
                                      )

  blockDict[menuName+'Menu'] = gh(
                                    dict (
                                          tag="div",
                                          htmlClass='dropDownMenu',
                                          blockContent=blockContent,
                                          htmlId=menuName+'Menu'
                                    )
                                  )

  return blockDict[menuName+'Menu']

# xxx-replace
## LAST MODIFIED : December 12, 2012
## CREATED : December 12, 2012
## AUTHOR : DRYX
def get_option_list(optionList):
  """Create a dropdown option list

    **Key Arguments:**
        - ``optionList`` -- list of items to appear in option list
        - ``attributeDict`` -- dictionary of the following keywords:
        - ``htmlClass`` -- the html element class
        - ``htmlId`` -- the html element id
        - ``blockContent`` -- actual content to be placed in html code block
        - ``jsEvents`` -- inline javascript events
        - ``extraAttr`` -- extra inline css attributes and/or handles
        - ``name`` -- an extra hook (much like "id")
        - ``type`` -- HTML input types = color, date, datetime, datetime-local, email, month, number, range, search, tel, time, url, week
        - ``placeholder`` -- text to be displayed by default in the input box
        - ``required`` -- make input required (boolean)
        - ``autofocus`` -- make this the auofocus element of the form (i.e. place cursor here)
        - ``maxlength`` -- maximum character length for the form

    **Returns:**
        - ``block`` -- the HTML code block
  """
  ################ > IMPORTS ################

  ################ > VARIABLE SETTINGS ######
  block = ""

  ################ >ACTION(S) ################
  for option in optionList:
    htmlId = option.replace(' ','')
    block += get_html_block(
                              dict(
                                tag="option",
                                htmlId=htmlId,
                                value=option,
                                blockContent=option
                              )
                            )
  return block


## LAST MODIFIED : March 8, 2013
## CREATED : March 8, 2013
## AUTHOR : DRYX
def dropdown(
        buttonSize="default",
        color="grey",
        menuTitle="#",
        splitButton=False,
        linkList=[],
        separatedLinkList=False,
        pull=False,
        direction="down",
        onPhone=True,
        onTablet=True,
        onDesktop=True):
    """get a toggleable, contextual menu for displaying lists of links. Made interactive with the dropdown JavaScript plugin. You need to wrap the dropdown's trigger and the dropdown menu within .dropdown, or another element that declares position: relative;

    - ``buttonSize`` -- size of button [ mini | small | default | large ]
    - ``buttonColor`` -- [ default | sucess | error | warning | info ]
    - ``menuTitle`` -- the title of the menu
    - ``splitButton`` -- split the button into a separate action button and a dropdown
    - ``linkList`` -- a list of (linked) items items that the menu should display
    - ``separatedLinkList`` -- a list of (linked) items items that the menu should display below divider
    - ``pull`` -- [ false | right | left ] (e.g Add ``right`` to a ``.dropdown-menu`` to right align the dropdown menu.)
    - ``direction`` -- drop [ down | up ]
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
    # Add .dropdown-submenu to any li in an existing dropdown menu for automatic styling.
    thisLinkList = ""
    for link in linkList:
        thisLinkList += """%s""" % (link, )

    thisSeparatedLinkList = ""
    if separatedLinkList:
        thisSeparatedLinkList = """<li class="divider"></li>"""
        for link in separatedLinkList:
            thisSeparatedLinkList += """%s""" % (link, )

    thisLinkList = thisLinkList + thisSeparatedLinkList

    if buttonSize == "default":
        buttonSize = ""
    else:
        buttonSize = "btn-%s" % (buttonSize,)

    if direction == "up":
        direction = "dropup"
    else:
        direction = ""

    if splitButton:
        dropdownButton = """
            <button class="btn %s %s">%s</button>
            <button class="btn %s %s dropdown-toggle" data-toggle="dropdown">
                <span class="caret"></span>
            </button>""" % (buttonSize, buttonColor, menuTitle, buttonSize, buttonColor)
    else:
        dropdownButton = """
            <a class="btn %s %s dropdown-toggle" data-toggle="dropdown" href="#">
              %s
              <span class="caret"></span>
            </a>""" % (buttonSize, buttonColor, menuTitle,)

    if pull:
        pull = """pull-%s""" % (pull,)
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
        <div class="btn-group %s %s %s %s" id="" %s>
            %s
            <ul class="dropdown-menu">
                <!-- dropdown menu links -->
                %s
          </ul>
        </div>""" % (pull, onPhone, onTablet, onDesktop, direction, dropdownButton, thisLinkList)

    return dropdown

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()


###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
