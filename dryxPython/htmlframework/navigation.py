#!/usr/bin/python
# -*- coding: utf-8 -*-
""" navigation.py
==================================
:Summary:
    Navigation for TBS htmlframework

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
# SNIPPET CREATED
# LAST MODIFIED : March 15, 2013
# CREATED : March 15, 2013
# AUTHOR : DRYX
def responsive_navigation_bar(
    shade='dark',
    brand=False,
    brandLink="#",
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

    if not shade:
        shade = ''
    else:
        shade = 'navbar-inverse'
    if not brand:
        brand = ''
    else:
        brand = """<a class="brand" href="%(brandLink)s">%(brand)s</a>""" % locals(
        )

    if not outsideNavList:
        outsideNavList = ''

    thisList = ""
    if insideNavList:
        insideNavList = """<div class="nav-collapse collapse"><ul class="nav pull-right">%(insideNavList)s</ul></div>""" % locals(
        )
    else:
        insideNavList = ''

    if htmlId:
        htmlId = """id="%(htmlId)s" """ % locals()
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
    navBar = """<div class="navbar %(shade)s %(onPhone)s %(onTablet)s %(onDesktop)s" %(htmlId)s>
    <div class="navbar-inner">
        <div class="container">
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </a>
            %(brand)s%(outsideNavList)s%(insideNavList)s
        </div>
    </div>
 </div>""" % locals()
    return navBar


# SNIPPET CREATED
# LAST MODIFIED : March 15, 2013
# CREATED : March 15, 2013
# AUTHOR : DRYX
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
        pull = """pull-%(pull)s""" % locals()
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

    navList = """<ul class="nav %(pull)s %(onPhone)s %(onTablet)s %(onDesktop)s">""" % locals(
    )

    for item in itemList:
        navList = """%(navList)s
            <li>
                %(item)s
            </li>""" % locals()
    navList = """%(navList)s</ul>""" % locals()
    return navList


# LAST MODIFIED : March 15, 2013
# CREATED : March 15, 2013
# AUTHOR : DRYX
def searchbox(
    size='medium',
    htmlId="",
    placeHolder=False,
    button=False,
    buttonSize='small',
    buttonColor='grey',
    navBar=False,
    pull=False,
    actionScript="#"
):
    """Create a Search box

    **Key Arguments:**
        - ``size`` -- size = mini | small | medium | large | xlarge | xxlarge
        - ``htmlId`` -- the html id of the search bar
        - ``placeholder`` -- placeholder text
        - ``button`` -- do you want a search button?
        - ``buttonSize``
        - ``buttonColor``
        - ``actionScript`` -- the script used to action the search text

    **Return:**
        - ``markup`` -- markup for the searchbar """

    if button:
        button = """<button type="submit" class="btn-%(buttonSize)s btn-%(buttonColor)s">Search</button>""" % locals(
        )
    else:
        button = ''
    if placeHolder:
        placeHolder = """placeholder="%(placeHolder)s" """ % locals()
    else:
        placeHolder = ''
    if navBar:
        navBar = 'navbar-search'
    else:
        navBar = ''
    if pull:
        pull = """pull-%(pull)s""" % locals()
    else:
        pull = ''

    markup = \
        """
    <form class="form-search pull-right" action="%(actionScript)s">
      <input id="%(htmlId)s" name="%(htmlId)s" type="text" class="input-%(size)s search-query %(navBar)s %(pull)s" %(placeHolder)s >
      %(button)s
    </form>
    """ % locals()
    return markup


# LAST MODIFIED : April 29, 2013
# CREATED : April 29, 2013
# AUTHOR : DRYX

def tabbableNavigation(
        contentDictionary={},  # { name : content }
        fadeIn=True,
        direction='top',
        htmlClass=False,
        htmlId=False,
        uniqueNavigationId=False
):
    """ Generate a tabbable Navigation

    **Key Arguments:**
        - ``contentDictionary`` -- the content dictionary { name : content }
        - ``fadeIn`` -- make tabs fade in
        - ``direction`` -- the position of the tabs [ above | below | left | right ]
        - ``uniqueNavigationId`` -- a unique id for this navigation block if more than one on page

    **Return:**
        - ``tabbableNavigation`` -- the tabbableNavigation """

    if fadeIn is True:
        fadeIn = 'fade'
    else:
        fadeIn = ''
    titleList = ''
    contentList = ''
    count = 0

    if htmlClass is False:
        htmlClass = ""

    if htmlId is False:
        htmlId = ""
    else:
        htmlId = """id="%(htmlId)s" """ % locals()

    if uniqueNavigationId is False:
        uniqueNavigationId = ""
    elif isinstance(uniqueNavigationId, int):
        uniqueNavigationId = """id%(uniqueNavigationId)s""" % locals()

    for k, v in contentDictionary.iteritems():
        if count == 0:
            titleList = """%(titleList)s<li class="active"><a href="#tab%(uniqueNavigationId)s%(count)s" data-toggle="tab">%(k)s</a></li>""" % locals(
            )
            contentList = \
                """%(contentList)s
                <div class="tab-pane active %(fadeIn)s" id="tab%(uniqueNavigationId)s%(count)s">
                    <p>%(v)s</p>
                </div>""" \
                % locals()
        else:
            titleList = """%(titleList)s<li><a href="#tab%(uniqueNavigationId)s%(count)s" data-toggle="tab">%(k)s</a></li>""" % locals(
            )
            contentList = \
                """%(contentList)s
                <div class="tab-pane %(fadeIn)s" id="tab%(uniqueNavigationId)s%(count)s">
                    <p>%(v)s</p>
                </div>""" \
                % locals()
        count += 1
    tabbableNavigation = \
        """
        <div class="tabbable %(htmlClass)s" %(htmlId)s>
            <ul class="nav nav-tabs">
                %(titleList)s
            </ul>
            <div class="tab-content">
                %(contentList)s
            </div>
        </div>""" \
        % locals()
    if direction != 'top':
        tabbableNavigation = \
            """
            <div class="tabbable tabs-%(direction)s %(htmlClass)s" %(htmlId)s>
                <div class="tab-content">
                    %(contentList)s
                </div>
                <ul class="nav nav-tabs">
                    %(titleList)s
                </ul>
            </div>""" \
            % locals()
    return tabbableNavigation


# LAST MODIFIED : April 30, 2013
# CREATED : April 30, 2013
# AUTHOR : DRYX

def navBar(
    brand='',
    contentList=[],
    contentListPull=False,
    dividers=False,
    forms=False,
    fixedOrStatic=False,
    location='top',
    responsive=False,
    dark=False,
    transparent=False,
    htmlClass=False
):
    """ Generate a navBar - TBS style

    **Key Arguments:**
        - ``brand`` -- the website brand [ image | text ]
        - ``contentList`` -- the content list of li and dropdowns
        - ``contentListPull`` -- False, right, left
        - ``fixedOrStatic`` -- Fix the navbar to the top or bottom of the viewport, or create a static full-width navbar that scrolls away with the page [ False | fixed | static ]
        - ``location`` -- location of the navigation bar if fixed or static
        - ``dark`` -- Modify the look of the navbar by making it dark
        - ``transparent`` -- make the bar see-through

    **Return:**
        - ``navBar`` -- the navBar """

    if brand is not False:
        brand = u"""<a class="brand" href="#">%(brand)s</a>""" % locals()
    else:
        brand = u""
    toggleButton = ""
    falseList = [dividers, fixedOrStatic, toggleButton, dark]
    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""
    [dividers, fixedOrStatic, toggleButton, dark] = falseList
    if dividers:
        dividers = u"""<li class="divider-vertical"></li>"""
    titleList = ''
    # contentList = ''
    count = 0

    if htmlClass is False:
        htmlClass = ""

    if contentListPull is not False:
        contentListPull = u"pull-%(contentListPull)s" % locals()

    for item in contentList:
        item = u"""<li>%(item)s</li>""" % locals()
        titleList = u"""%(titleList)s %(item)s %(dividers)s""" % locals()

    titleList = u"""
    <ul class="nav %(contentListPull)s" id="  ">
        %(titleList)s
    </ul>
    """ % locals()

    formList = ""
    if forms:
        formList = forms

    if fixedOrStatic:
        fixedOrStatic = u'navbar-%(fixedOrStatic)s-%(location)s' % locals()
    if responsive:
        toggleButton = \
            u"""
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </a>
        """
        titleList = u"""
            <div class="nav-collapse collapse">
                %(titleList)s
            </div>""" \
            % locals()
    if dark is True:
        dark = "navbar-inverse"
    else:
        dark = ""

    if transparent is True:
        transparent = u"navbar-transparent"
    else:
        transparent = ""

    navBar = \
        u"""
        <div class="navbar %(fixedOrStatic)s %(dark)s %(transparent)s %(htmlClass)s">
          <div class="navbar-inner">
            %(brand)s
            %(titleList)s
            %(formList)s
          </div>
        </div>
        """ % locals()
    return navBar


# LAST MODIFIED : 20130508
# CREATED : 20130508
# AUTHOR : DRYX
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
        size = "pagination-%(size)s" % locals()
    if align == "left":
        align = ""
    else:
        align = "pagination-%(align)s" % locals()

    pagination = """
        <div class="pagination %(size)s %(align)s" id="  ">
            <ul>
            %(listItems)s
            </ul>
        </div>""" % locals()

    return pagination


# LAST MODIFIED : July 22, 2013
# CREATED : July 22, 2013
# AUTHOR : DRYX
def is_navStyle_active(
        log,
        thisPageName,
        thisPageId):
    """is navStyle active

    **Key Arguments:**
        - ``log`` -- logger
        - ``thisPageName`` -- the thisPageName of the page
        - ``thisPageId`` -- the Id of this page

    **Return:**
        - ``navStyle`` -- boolean, true if the navStyle should be active, i.e. the link is to the currently viewed page

    **Todo**
    - [ ] when complete, clean is_navStyle_active function & add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log.info('starting the ``is_navStyle_active`` function')
    ## VARIABLES ##

    if thisPageName == thisPageId:
        navStyle = "active"
    else:
        navStyle = False

    log.info('completed the ``is_navStyle_active`` function')
    return navStyle

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################
###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
