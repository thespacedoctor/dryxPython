#!/usr/bin/python
# -*- coding: utf-8 -*-
""" _dryxTBS_navigation
==================================
:Summary:
    Navigation component partial for dryxTwitterBootstrap module

:Author:
    David Young

:Date Created:
    March 15, 2013

:dryx syntax:
    - ``xxx`` = come back here and do some more work
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script please email me: d.r.young@qub.ac.uk """


###################################################################
# CLASSES                                                         #
###################################################################
###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
## SNIPPET CREATED
## LAST MODIFIED : March 15, 2013
## CREATED : March 15, 2013
## AUTHOR : DRYX
def responsive_navigation_bar(
    shade='dark',
    brand=False,
    outsideNavList=False,
    insideNavList=False,
    htmlId=False,
    onPhone=True,
    onTablet=True,
    onDesktop=True,
    ):
    """ Create a twitter bootstrap responsive nav-bar component

    **Key Arguments:**
        - ``shade`` -- if dark then colors are inverted [ False | 'dark' ]
        - ``brand`` -- the website brand [ image | text ]
        - ``outsideNavList`` -- nav-list to be contained outside collapsible content
        - ``insideNavList`` -- nav-list to be contained inside collapsible content
        - ``htmlId`` --
        - ``onPhone`` -- does this container get displayed on a phone sized screen
        - ``onTablet`` -- does this container get displayed on a tablet sized screen
        - ``onDesktop`` -- does this container get displayed on a desktop sized screen

    **Return:**
        - ``navBar`` -- """

    if 'dark' in shade:
        shade = 'navbar-inverse'
    else:
        shade = ''
    if not brand:
        brand = ''
    else:
        brand = """<a class="brand" href="#">%s</a>""" % (brand, )
    if not outsideNavList:
        outsideNavList = ''
    if insideNavList:
        insideNavList = \
            """
            <div class="nav-collapse collapse">
                %s
            </div>
        """ \
            % (insideNavList, )
    else:
        insideNavList = ''
    if htmlId:
        htmlId = """id="%s" """ % (htmlId, )
    else:
        htmlId = ''
    if onPhone:
        onPhone = ''
    else:
        onPhone = 'hidden-phone'
    if onTablet:
        onTablet = ''
    else:
        onTablet = 'hidden-tablet'
    if onDesktop:
        onDesktop = ''
    else:
        onDesktop = 'hidden-desktop'
    navBar = \
        """
        <div class="navbar %s %s %s %s" %s>
            <div class="navbar-inner">
                <div class="container">
                    <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </a>
                    %s
                    %s
                    %s
                </div>
            </div>
         </div>
    """ \
        % (
        shade,
        onPhone,
        onTablet,
        onDesktop,
        htmlId,
        brand,
        outsideNavList,
        insideNavList,
        )
    return navBar


## SNIPPET CREATED
## LAST MODIFIED : March 15, 2013
## CREATED : March 15, 2013
## AUTHOR : DRYX
def nav_list(
    itemList=[],
    pull=False,
    onPhone=True,
    onTablet=True,
    onDesktop=True,
    ):
    """Create an html list of navigation items from the required python list

    **Key Arguments:**
        - ``itemList`` -- items to be included in the navigation list
        - ``pull`` -- float the nav-list [ False | 'right' | 'left' ]
        - ``onPhone`` -- does this container get displayed on a phone sized screen
        - ``onTablet`` -- does this container get displayed on a tablet sized screen
        - ``onDesktop`` -- does this container get displayed on a desktop sized screen

    **Return:**
        - navList """

    if pull:
        pull = """pull-%s""" % (pull, )
    else:
        pull = ''
    if onPhone:
        onPhone = ''
    else:
        onPhone = 'hidden-phone'
    if onTablet:
        onTablet = ''
    else:
        onTablet = 'hidden-tablet'
    if onDesktop:
        onDesktop = ''
    else:
        onDesktop = 'hidden-desktop'
    navList = """<ul class="nav %s %s %s %s">""" % (
        pull,
        onPhone,
        onTablet,
        onDesktop,
        )
    for item in itemList:
        navList += """
            <li>
                %s
            </li>""" % (item, )
    navList += """</ul>"""
    return navList





# xxxxxxxxxxxxxx do more work on below and create snippets xxxxxxxxxxxxxxx



# xxx-replace
## LAST MODIFIED : December 11, 2012
## CREATED : December 11, 2012
## AUTHOR : DRYX
def get_nav_block(attributeDict):
  """Create a basic ``<nav>`` code block

  **Variable Attributes:**
    - ``attributeDict`` -- dictionary of the following keywords:
    - ``htmlClass`` -- the html element class
    - ``htmlId`` -- the html element id
    - ``blockContent`` -- actual content to be placed in html code block
    - ``jsEvents`` -- inline javascript event
    - ``extraAttr`` -- extra inline css attributes and/or handles

  **Returns:**
    - ``block`` -- the html block

  attributeDict template:
    attributeDict = dict(
                          htmlClass=___,
                          htmlId=___,
                          jsEvents=___,
                          extraAttr=___,
                          blockContent=___
                        )
  """
  ################ > IMPORTS ################

  ################ > VARIABLE SETTINGS ######
  block = "<div "   # THE HTML BLOCK
  d = attributeDict

  ################ >ACTION(S) ################
  ## SET THE ATTRIBUTES
  if d.has_key("htmlClass"):
    block += """class="%s" """ % (d["htmlClass"],)
  if d.has_key("htmlId"):
    block += """id="%s" """ % (d["htmlId"],)
  if d.has_key("jsEvents"):
    block += """%s """ % (d["jsEvents"],)
  if d.has_key("extraAttr"):
    block += """%s """ % (d["extraAttr"],)
  block += "><nav><ul>"

  ## SET THE CONTENT
  if d.has_key("blockContent"):
    block += str(d["blockContent"])

  ## CLOSE THE BLOCK
  if d.has_key("htmlId"):
    block += "</ul></nav></div><!--- /#%s --->" % (d["htmlId"],)
  else:
    block += "</ul></nav></div>"

  return block







## LAST MODIFIED : March 15, 2013
## CREATED : March 15, 2013
## AUTHOR : DRYX

def searchbox(
    size='medium',
    placeHolder=False,
    button=False,
    buttonSize='small',
    buttonColor='grey',
    navBar=False,
    pull=False,
    ):
    """Create a Search box

    **Key Arguments:**
        - ``size`` -- size = mini | small | medium | large | xlarge | xxlarge
        - ``placeholder`` -- placeholder text
        - ``button`` -- do you want a search button?
        - ``buttonSize``
        - ``buttonColor``

    **Return:**
        - ``markup`` -- markup for the searchbar """

    if button:
        button = """<button type="submit" class="btn-%s btn-%s">Search</button>""" % (buttonSize, buttonColor)
    else:
        button = ''
    if placeHolder:
        placeHolder = """placeholder="%s" """ % (placeHolder, )
    else:
        placeHolder = ''
    if navBar:
        navBar = 'navbar-search'
    else:
        navBar = ''
    if pull:
        pull = """pull-%s""" % (pull, )
    else:
        pull = ''
    markup = \
        """
    <form class="form-search pull-right">
      <input type="text" class="input-%s search-query %s %s" %s>
      %s
    </form>
    """ \
        % (
        size,
        navBar,
        pull,
        placeHolder,
        button,
        )
    return markup


## LAST MODIFIED : April 29, 2013
## CREATED : April 29, 2013
## AUTHOR : DRYX

def tabbableNavigation(
    contentDictionary={},
    fadeIn=True,
    direction='top',
    ):
    """ Generate a tabbable Navigation

    **Key Arguments:**
        - ``contentDictionary`` -- the content dictionary { name : content }
        - ``fadeIn`` -- make tabs fade in
        - ``direction`` -- the position of the tabs [ above | below | left | right ]

    **Return:**
        - ``tabbableNavigation`` -- the tabbableNavigation """

    if fadeIn is True:
        fadeIn = 'fade'
    else:
        fadeIn = ''
    titleList = ''
    contentList = ''
    count = 0
    for (k, v) in contentDictionary.iteritems():
        if count == 0:
            titleList += """<li class="active"><a href="#tab%s" data-toggle="tab">%s</a></li>""" % (count, k)
            contentList += \
                """
                <div class="tab-pane active %s" id="tab%s">
                    <p>%s</p>
                </div>""" \
                % (fadeIn, count, v)
        else:
            titleList += """<li><a href="#tab%s" data-toggle="tab">%s</a></li>""" % (count, k)
            contentList += \
                """
                <div class="tab-pane %s" id="tab%s">
                    <p>%s</p>
                </div>""" \
                % (fadeIn, count, v)
        count += 1
    tabbableNavigation = \
        """
        <div class="tabbable" id="  ">
            <ul class="nav nav-tabs">
                %s
            </ul>
            <div class="tab-content">
                %s
            </div>
        </div>""" \
        % (titleList, contentList)
    if direction != 'top':
        tabbableNavigation = \
            """
            <div class="tabbable tabs-%s" id="  ">
                <div class="tab-content">
                    %s
                </div>
                <ul class="nav nav-tabs">
                    %s
                </ul>
            </div>""" \
            % (direction, contentList, titleList)
    return tabbableNavigation


## LAST MODIFIED : April 30, 2013
## CREATED : April 30, 2013
## AUTHOR : DRYX

def navBar(
    brand='',
    contentDictionary={},
    dividers=False,
    fixedOrStatic=False,
    location='top',
    responsive=False,
    dark=False
    ):
    """ Generate a navBar - TBS style

    **Key Arguments:**
        - ``brand`` -- the website brand [ image | text ]
        - ``contentDictionary`` -- the content dictionary { text : href }
        - ``fixedOrStatic`` -- Fix the navbar to the top or bottom of the viewport, or create a static full-width navbar that scrolls away with the page [ False | fixed | static ]
        - ``location`` -- location of the navigation bar if fixed or static
        - ``dark`` -- Modify the look of the navbar by making it dark

    **Return:**
        - ``navBar`` -- the navBar """

    brand = """<a class="brand" href="#">%s</a>""" % (brand, )
    toggleButton = ""
    falseList = [dividers, fixedOrStatic, toggleButton, dark]
    for i in range(len(falseList)):
            if not falseList[i]:
                falseList[i] = ""
    [dividers, fixedOrStatic, toggleButton, dark] = falseList
    if dividers:
        dividers = """<li class="divider-vertical"></li>"""
    titleList = ''
    contentList = ''
    count = 0
    for (k, v) in contentDictionary.iteritems():
        if count == 0:
            titleList += """<li class="active"><a href="%s">%s</a></li>%s""" % (v, k, dividers)
        else:
            titleList += """<li><a href="%s">%s</a></li>%s""" % (v, k, dividers)
        count += 1
    titleList = """
    <ul class="nav" id="  ">
        %s
    </ul>
    """ % (titleList, )
    if fixedOrStatic:
        fixedOrStatic = 'navbar-%s-%s' % (fixedOrStatic, location)
    if responsive:
        toggleButton = \
            """
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </a>
        """
        titleList = """
            <div class="nav-collapse collapse">
                %s
            </div>""" \
            % (titleList, )
    if dark is True:
        dark = "navbar-inverse"
    else:
        dark = ""
    navBar = \
        """
        <div class="navbar %s %s">
          <div class="navbar-inner">
            %s
            %s
          </div>
        </div>
        """ \
        % (fixedOrStatic, dark, brand, titleList)
    return navBar


## LAST MODIFIED : 20130508
## CREATED : 20130508
## AUTHOR : DRYX
def pagination(
        listItems="",
        size="default",
        align="left"):
    """Generate pagination - TBS style. Simple pagination inspired by Rdio, great for apps and search results.

    **Key Arguments:**
        - ``listItems`` -- the numbered items to be listed within the <ul> of the pagination block
        - ``size`` -- additional pagination block sizes [ "mini" | "small" | "default" | "large" ]
        - ``align`` -- change the alignment of pagination links [ "left" | "center" | "right" ]

    **Return:**
        - ``pagination`` -- the pagination
    """
    if size == "default":
        size = ""
    else:
        size = "pagination-%s" % (size,)

    if align == "left":
        align = ""
    else:
        align = "pagination-%s" % (align,)

    pagination = """
        <div class="pagination" id="  ">
            <ul>
            %s
            </ul>
        </div>""" % (content,)

    return pagination

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################
###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
