#!/usr/local/bin/python
# encoding: utf-8
"""
typography.py
=============================
:Summary:
    Basic text elements for TBS htmlframework
:Author:
    David Young

:Date Created:
    April 11, 2013

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
# LAST MODIFIED : April 11, 2013
# CREATED : April 11, 2013
# AUTHOR : DRYX


def p(
        content="",
        lead=False,
        textAlign=False,
        color=False,
        navBar=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
        htmlId=False,
        htmlClass=False):
    """Get a Paragraph element

    **Key Arguments:**
        - ``content`` -- content of the paragraph
        - ``lead`` -- is this a lead paragraph?
        - ``textAlign`` -- how to align paragraph text [ left | center | right ]
        - ``color`` -- colored text for emphasis [ muted | warning | info | error | success ]
        - ``navBar`` -- is this <p> for a navbar?
        - ``onPhone`` -- does this container get displayed on a phone sized screen
        - ``onTablet`` -- does this container get displayed on a tablet sized screen
        - ``onDesktop`` -- does this container get displayed on a desktop sized screen

    **Return:**
        - ``p`` -- the html paragraph element
    """
    falseList = [lead, textAlign, ]
    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""
    [lead, textAlign, ] = falseList

    if htmlId is not False:
        htmlId = """id="%(htmlId)s" """ % locals()
    else:
        htmlId = ""

    if htmlClass is False:
        htmlClass = ""

    if textAlign:
        textAlign = "text-%(textAlign)s" % locals()
    else:
        textAlign = ""

    if lead is True:
        lead = "lead"

    if color is False:
        color = ""
    elif color == "muted":
        color = "muted"
    else:
        color = """text-%(color)s""" % locals()

    if navBar is True:
        navBar = "navbar-text"
    else:
        navBar = ""

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

    p = """
        <p class="%(lead)s %(onPhone)s %(onTablet)s %(onDesktop)s %(textAlign)s %(color)s %(navBar)s %(htmlClass)s" %(htmlId)s>%(content)s</p>
    """ % locals()

    return p

# LAST MODIFIED : 20130508
# CREATED : 20130508
# AUTHOR : DRYX


def emphasizeText(
        style="em",
        text=""):
    """Get HTML's default emphasis tags with lightweight styles.

    **Key Arguments:**
        - ``style`` -- the emphasis tag [ "small" | "strong" | "em" ]
        - ``text`` -- the text to emphasise

    **Return:**
        - ``emphasizeText`` -- the emphasized text
    """
    emphasizeText = """
        <%(style)s>
            %(text)s
        </%(style)s>""" % locals()

    return emphasizeText


# LAST MODIFIED : April 13, 2013
# CREATED : April 13, 2013
# AUTHOR : DRYX
def abbr(
        abbreviation="",
        fullWord=""):
    """Get HTML5 Abbreviation

    **Key Arguments:**
        - ``abbreviation`` -- the abbreviation
        - ``fullWord`` -- the full word

    **Return:**
        - abbr
    """

    abbr = """<abbr title="%(fullWord)s" class="initialism">%(abbreviation)s</abbr>""" % locals(
    )

    return abbr


# LAST MODIFIED : April 13, 2013
# CREATED : April 13, 2013
# AUTHOR : DRYX
def address(
        name=False,
        addressLine1=False,
        addressLine2=False,
        addressLine3=False,
        phone=False,
        email=False,
        twitterHandle=False):
    """Get The HTML5 address element

    **Key Arguments:**
        - ``name`` -- name of person
        - ``addressLine1`` -- first line of the address
        - ``addressLine2`` -- second line of the address
        - ``addressLine3`` -- third line of the address
        - ``phone`` -- telephone number
        - ``email`` -- email address
        - ``twitterHandle`` -- twitter handle

    **Return:**
        - address
    """

    falseList = [name, addressLine1, addressLine2,
                 addressLine3, phone, email, twitterHandle]
    for item in falseList:
        if not item:
            item = ""

    if name:
        name = "<strong>%(name)s</strong><br>" % locals()
    else:
        name = ""

    if addressLine1:
        addressLine1 = "%(addressLine1)s<br>" % locals()
    else:
        addressLine1 = ""
    if addressLine2:
        addressLine2 = "%(addressLine2)s<br>" % locals()
    else:
        addressLine2 = ""
    if addressLine3:
        addressLine3 = "%(addressLine3)s<br>" % locals()
    else:
        addressLine3 = ""
    if phone:
        phone = """<abbr title="Phone">p:</abbr> %(phone)s<br>""" % locals()
    else:
        phone = ""
    if email:
        email = """<abbr title="email">e:</abbr> <a href="mailto:#">%(email)s</a><br>""" % locals(
        )
    else:
        email = ""
    if twitterHandle:
        twitterHandle = """<abbr title="twitter handle">t:</abbr> %(twitterHandle)s<br>""" % locals(
        )
    else:
        twitterHandle = ""

    address = """
        <address>
            %(name)s
            %(addressLine1)s
            %(addressLine2)s
            %(addressLine3)s
            %(phone)s
            %(email)s
            %(twitterHandle)s
        </address>
    """ % locals()

    return address


# LAST MODIFIED : April 13, 2013
# CREATED : April 13, 2013
# AUTHOR : DRYX
def blockquote(
        content="",
        source=False,
        pullRight=False):
    """Get HTML5 Blockquote

    **Key Arguments:**
        - ``content`` -- content to be quoted
        - ``source`` -- source of quote

    **Return:**
        - None
    """
    if source:
        source = """<small><cite title="%(source)s">%(source)s</cite></small>""" % locals(
        )
    else:
        source = ""

    if pullRight:
        pullRight = """class="pull-right" """
    else:
        pullRight = ""

    blockquote = """
        <blockquote %(pullRight)s>
            <p>%(content)s</p>
            %(source)s
        </blockquote>""" % locals()

    return blockquote


# LAST MODIFIED : April 13, 2013
# CREATED : April 13, 2013
# AUTHOR : DRYX
def ul(
        itemList=[],
        unstyled=False,
        inline=False,
        dropDownMenu=False,
        navStyle=False,
        navPull=False,
        navDirection="horizontal",
        breadcrumb=False,
        pager=False,
        thumbnails=False,
        mediaList=False,
        htmlId=False
):
    """Get An unordered list -- can be used for navigation, stacked tab and pill

    **Key Arguments:**
        - ``itemList`` -- a list of items to be included in the unordered list
        - ``unstyled`` -- is the list to be unstyled (first children only)
        - ``inline`` -- place all list items on a single line with inline-block and some light padding.
        - ``dropDownMenu`` -- is this ul to be used in a dropdown menu? [ false | true ]
        - ``navStyle`` -- set the navigation style if used for tabs & pills etc [ nav | tabs | pills | list ]
        - ``navPull`` -- set the alignment of the navigation links [ false | left | right ]
        - ``navDirection`` -- set the direction of the navigation [ 'default' | 'stacked' ]
        - ``breadcrumb`` -- display breadcrumb across muliple pages? [ False | True ]
        - ``pager`` -- use <ul> for a pager
        - ``thumbnails`` -- use the <ul> for a thumnail block?
        - ``mediaList`` -- use the <ul> for a media object list?
        - ``htmlId`` -- the html id of the ul

    **Return:**
        - ul
    """
    role = False
    falseList = [unstyled, inline, dropDownMenu, role, navStyle,
                 navPull, navDirection, breadcrumb, pager, thumbnails, mediaList]

    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""

    [unstyled, inline, dropDownMenu, role, navStyle, navPull,
        navDirection, breadcrumb, pager, thumbnails, mediaList] = falseList

    thisList = ""
    for i, item in enumerate(itemList):
        if "<li" in item:
            thisList = """%(thisList)s %(item)s""" % locals()
        else:
            thisList = """%(thisList)s <li>%(item)s</li>""" % locals()
        if i + 1 != len(itemList) and breadcrumb:
            thisList = thisList[:-5] + \
                """    <span class="divider">/</span></li>""" % locals()

    if unstyled:
        unstyled = "unstyled"

    if inline:
        inline = "inline"

    if dropDownMenu is True:
        dropDownMenu = "dropdown-menu"
        role = "menu"

    navStyleList = ["tabs", "pills", "list"]
    if navStyle:
        thisNavStyle = "nav"
    if navStyle in navStyleList:
        thisNavStyle = "%(thisNavStyle)s nav-%(navStyle)s" % locals()
    else:
        thisNavStyle = ""

    if navPull:
        navPull = "pull-%(navPull)s" % locals()

    if navDirection == "stacked":
        navDirection = "nav-stacked"
    elif navDirection == "horizontal":
        navDirection = ""
    else:
        navDirection = ""

    if breadcrumb is True:
        breadcrumb = "breadcrumb"

    if pager is True:
        pager = "pager"

    if thumbnails is True:
        thumbnails = "thumbnails"

    if mediaList is True:
        mediaList = "media-list"

    if not htmlId:
        htmlId = ""
    else:
        htmlId = 'id="%(htmlId)s"' % locals()

    ul = """<ul class="%(unstyled)s %(inline)s %(dropDownMenu)s %(role)s %(navPull)s %(thisNavStyle)s %(navDirection)s %(breadcrumb)s %(pager)s %(thumbnails)s %(mediaList)s" %(htmlId)s>%(thisList)s</ul>""" % locals(
    )

    return ul


# LAST MODIFIED : April 29, 2013
# CREATED : April 29, 2013
# AUTHOR : DRYX
def li(
        content="",
        span=False,
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=False,
        navDropDown=False,
        pager=False,
        pull=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
        indent=False):
    """Generate a li - TBS style

    **Key Arguments:**
        - ``content`` -- the content (if a subMenu for dropdown this should be <ul>)
        - ``span`` -- the column span [ False | 1-12 ]
        - ``disabled`` -- add the disabled attribute on an grey out this list item. Note you can optionally swap anchors for spans to remove click functionality.
        - ``submenuTitle`` -- if a submenu (<ul>) is to be included as content, use this as the title.
        - ``divider`` -- if true this list item shall be a line
        - ``navStyle`` -- how is the navigation element to be displayed? [ active | header ]
        - ``navDropDown`` -- true if the list item is to be used as a dropdown in navigation
        - ``pager`` -- use the <li> within a pager navigation? [ False | "previous" | "next" ]

    **Return:**
        - ``li`` -- the li
    """
    submenuClass = False
    falseList = [disabled, submenuClass,
                 submenuTitle, navStyle, navDropDown, pager, span]
    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""
    [disabled, submenuClass, submenuTitle,
        navStyle, navDropDown, pager, span] = falseList

    if pull:
        pull = "pull-%(pull)s" % locals()
    else:
        pull = ""

    if disabled:
        disabled = """disabled"""

    if submenuTitle:
        submenuClass = "dropdown-submenu"
        submenuTitle = """<a tabindex="-1" href="#">%(submenuTitle)s</a>""" % locals(
        )

    if navStyle == "active":
        if "href" in content:
            content = content.replace('class="', 'class="active ')
    elif navStyle:
        navStyle = "nav-%(navStyle)s" % locals()

    if navDropDown:
        navDropDown = """dropdown"""

    if span:
        span = "span%(span)s" % locals()

    if indent:
        indent = """style="padding-left: 1em" """
    else:
        indent = ""

    phoneClass = ""
    tabletClass = ""
    desktopClass = ""
    if onPhone:
        if onTablet:
            if not onDesktop:
                desktopClass = "hidden-desktop"
        else:
            if not onDesktop:
                phoneClass = "visible-phone"
            else:
                tabletClass = "hidden-tablet"
    else:
        if onTablet:
            if not onDesktop:
                tabletClass = "visible-tablet"
            else:
                phoneClass = "hidden-phone"
        else:
            desktopClass = "visible-desktop"

    li = """<li class="%(disabled)s %(phoneClass)s %(tabletClass)s %(desktopClass)s %(submenuClass)s %(navStyle)s %(pager)s %(span)s %(navDropDown)s %(pull)s" %(indent)s id="  ">%(submenuTitle)s%(content)s</li>""" % locals(
    )

    if divider is True:
        li = """<li class="divider"></li>"""

    return li


# LAST MODIFIED : April 29, 2013
# CREATED : April 29, 2013
# AUTHOR : DRYX
def a(
        content="",
        href=False,
        tableIndex=False,
        thumbnail=False,
        pull=False,
        triggerStyle=False,
        htmlClass=False,
        htmlId=False,
        notification=False,
        postInBackground=False,
        openInNewTab=False,
        popover=False):
    """Generate an anchor - TBS style

    **Key Arguments:**
        - ``content`` -- the content
        - ``href`` -- the href link for the anchor
        - ``tableIndex`` -- table index for the dropdown menus [ False | -1 ]
        - ``pull`` -- direction to float the link (esp if image)
        - ``triggerStyle`` -- link to be used as a dropDown or tab trigger? [ False | "dropdown" | "tab" | "thumbnail" ]
        - ``htmlClass`` -- the class of the link
        - ``htmlId`` -- the html id of the anchor
        - ``postInBackground`` -- post to the href in the background, to fire data off to a cgi script to action without leaving page
        - ``notification`` -- a notification to be displayed on webpage
        - ``openInNewTab`` -- open the link in a new tab?

    **Return:**
        - ``a`` -- the a
    """
    triggerClass = ""
    dropdownCaret = ""

    falseList = [href, triggerClass,
                 triggerStyle, tableIndex, dropdownCaret, pull]
    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""
    [href, triggerClass, triggerStyle,
        tableIndex, dropdownCaret, pull] = falseList

    if popover is False:
        popover = ""

    if openInNewTab is not False:
        openInNewTab = """target="_blank" """
    else:
        openInNewTab = ""

    if not htmlId:
        htmlId = ""
    else:
        htmlId = 'id="%(htmlId)s"' % locals()

    if notification is False:
        notification = ""
    else:
        notification = """notification="%(notification)s" """ % locals()

    if tableIndex is True:
        tableIndex = """tableIndex = "%(tableIndex)s" """ % locals()

    if thumbnail:
        thumbnail = "thumbnail"
    else:
        thumbnail = ""

    if htmlClass is False:
        htmlClass = ""

    if pull:
        pull = "pull-%(pull)s" % locals()

    if postInBackground is True:
        postInBackground = "postInBackground"
    else:
        postInBackground = ""

    if triggerStyle == "dropdown":
        triggerClass = "dropdown-toggle"
        triggerToggle = """data-toggle="dropdown" """
        dropdownCaret = """<b class="caret"></b> """
    elif triggerStyle in ["tab", "modal"]:
        triggerToggle = """data-toggle="%(triggerStyle)s" """ % locals()
    else:
        triggerToggle = ""

    a = """<a %(tableIndex)s href="%(href)s" %(popover)s class="%(triggerClass)s %(thumbnail)s %(pull)s %(htmlClass)s %(postInBackground)s"  %(openInNewTab)s %(htmlId)s %(triggerToggle)s %(notification)s>%(content)s%(dropdownCaret)s</a>""" % locals()

    return a


# LAST MODIFIED : April 13, 2013
# CREATED : April 13, 2013
# AUTHOR : DRYX
def ol(itemList=[]):
    """An ordered list

    **Key Arguments:**
        - ``itemList`` -- a list of items to be included in the ordered list

    **Return:**
        - ol
    """
    thisList = ""
    for item in itemList:
        if "<li" in item[:5]:
            thisList = """%(thisList)s\n%(item)s""" % locals()
        else:
            thisList = """%(thisList)s <li>%(item)s</li>\n""" % locals()

    ol = """
        <ol>
            %(thisList)s
        </ol>
    """ % locals()

    return ol


# LAST MODIFIED : April 13, 2013
# CREATED : April 13, 2013
# AUTHOR : DRYX
def descriptionLists(
        orderedDictionary={},
        sideBySide=False):
    """A list of definitions.

    **Key Arguments:**
        - ``orderedDictionary`` -- the ordered dictionary of the terms and their definitions
        - ``sideBySide`` -- Make terms and descriptions in <dl> line up side-by-side.

    **Return:**
        - None
    """

    termList = ""
    for k, v in orderedDictionary.iteritems():
        termList = """%(termList)s
            <dt>%(k)s</dt>
            <dd>%(v)s</dd>
        """ % locals()

    if sideBySide:
        sideBySide = "dl-horizontal"
    else:
        sideBySide = ""

    descriptionLists = """
        <dl class="%(sideBySide)s">
            %(termList)s
        </dl>
    """ % locals()

    return descriptionLists


# LAST MODIFIED : 20130508
# CREATED : 20130508
# AUTHOR : DRYX
def heroUnit(
        headline="",
        tagline="",
        buttonStyle="primary",
        buttonText="",
        buttonHref="#"
):
    """Generate a heroUnit - TBS style

    **Key Arguments:**
        - ``headline`` -- the headline text
        - ``tagline`` -- the tagline text for below the headline
        - ``buttonStyle`` -- the style of the button to be used
        - ``buttonText`` -- the text for the button
        - ``buttonHref`` -- the anchor link for the button

    **Return:**
        - ``heroUnit`` -- the heroUnit
    """
    heroUnit = """
        <div class="hero-unit" id="  ">
            <h1>%(headline)s</h1>
            <p>%(tagline)s</p>
            <p>
                <a href="%(buttonHref)s" class="btn btn-%(buttonStyle)s btn-large">
                  %(buttonText)s
                </a>
            </p>
        </div>""" % locals()

    return heroUnit


# LAST MODIFIED : 20130508
# CREATED : 20130508
# AUTHOR : DRYX
def pageHeader(
        headline="",
        tagline=""):
    """Generate a pageHeader - TBS style

    **Key Arguments:**
        - ``headline`` -- the headline text
        - ``tagline`` -- the tagline text for below the headline

    **Return:**
        - ``pageHeader`` -- the pageHeader
    """
    pageHeader = """
        <div class="page-header" id="  ">
            <h1>%(headline)s<br><small>%(tagline)s</small></h1>
        </div>""" % locals()

    return pageHeader


# LAST MODIFIED : November 21, 2013
# CREATED : November 21, 2013
# AUTHOR : DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method
def coloredText(
        text="",
        color="red",
        htmlClass="",
        pull=False,
        size=False,
        addBackgroundColor=False):
    """Colour text a given colour

    **Key Arguments:**
        - ``text`` -- the text to color
        - ``color`` -- the color
        - ``htmlClass`` -- the class for the text
        - ``size`` -- the relative size of the text

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean coloredText function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    if pull is not False:
        pull = """pull-%(pull)s""" % locals()
    else:
        pull = ""

    if size is not False:
        size = """size-%(size)s""" % locals()
    else:
        size = ""

    if addBackgroundColor is not False:
        addBackgroundColor = "addBackground"
    else:
        addBackgroundColor = ""

    text = """<span class="colortext %(color)s %(addBackgroundColor)s %(htmlClass)s %(pull)s %(size)s">%(text)s</span>""" % locals(
    )

    return text

# use the tab-trigger below for new function
# x-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()


###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
########
