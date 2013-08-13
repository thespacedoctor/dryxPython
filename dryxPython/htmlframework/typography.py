#!/usr/local/bin/python
# encoding: utf-8
"""
_dryxTBS_elements
=============================
:Summary:
    Basic HTML elements partial of the dryxTwitterBootstrap

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
## LAST MODIFIED : April 11, 2013
## CREATED : April 11, 2013
## AUTHOR : DRYX
def p(
        content="",
        lead=False,
        textAlign=False,
        color=False,
        navBar=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True):
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
    falseList = [lead,textAlign,]
    for i in range(len(falseList)):
            if not falseList[i]:
                falseList[i] = ""
    [lead,textAlign,] = falseList

    if lead is True:
        lead = "lead"

    if color is False:
        color = ""
    elif color == "muted":
        color = "muted"
    else:
        color = "text-" + color

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
        <p class="%s %s %s %s %s %s %s">%s</p>
    """ % (lead, onPhone, onTablet, onDesktop, textAlign, color, navBar, content)

    return p

## LAST MODIFIED : 20130508
## CREATED : 20130508
## AUTHOR : DRYX
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
        <%s>
            %s
        </%s>""" % (style, text, style)

    return emphasizeText


## LAST MODIFIED : April 13, 2013
## CREATED : April 13, 2013
## AUTHOR : DRYX
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

    abbr = """<abbr title="%s" class="initialism">%s</abbr>""" % (abbreviation, fullWord)

    return abbr


## LAST MODIFIED : April 13, 2013
## CREATED : April 13, 2013
## AUTHOR : DRYX
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
    if not name:
        name = "<strong><strong>%s</strong><br>" % (name,)
    if not addressLine1:
        addressLine1 = "%s<br>" % (addressLine1,)
    if not addressLine2:
        addressLine2 = "%s<br>" % (addressLine2,)
    if not addressLine3:
        addressLine3 = "%s<br>" % (addressLine3,)
    if not phone:
        phone = """<abbr title="Phone">p:</abbr> %s<br>""" % (phone,)
    if not email:
        email = """<abbr title="email">e:</abbr> <a href="mailto:#">%s</a><br>""" % (email,)
    if not twitterHandle:
        twitterHandle = """<abbr title="twitter handle">t:</abbr> %s<br>""" % (twitterHandle,)

    address = """
        <address>
            %s
            %s
            %s
            %s
            %s
            %s
            %s
        </address>
    """ % (name, addressLine1, addressLine2, addressLine3, phone, email, twitterHandle)

    return address


## LAST MODIFIED : April 13, 2013
## CREATED : April 13, 2013
## AUTHOR : DRYX
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
        source = """<small><cite title="%s">%s</cite></small>""" % (source, source)
    else:
        source = ""

    if pullRight:
        pullRight = """class="pull-right" """
    else:
        pullRight = ""

    blockquote = """
        <blockquote %s>
            <p>%s</p>
            %s
        </blockquote>""" % (pullRight, content, source)

    return blockquote


## LAST MODIFIED : April 13, 2013
## CREATED : April 13, 2013
## AUTHOR : DRYX
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
        mediaList=False
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

    **Return:**
        - ul
    """
    role = False
    falseList = [unstyled, inline, dropDownMenu, role, navStyle, navPull, navDirection, breadcrumb, pager, thumbnails, mediaList]

    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""

    [unstyled, inline, dropDownMenu, role, navStyle, navPull, navDirection, breadcrumb, pager, thumbnails, mediaList] = falseList

    thisList = ""
    for item in itemList:
        thisList += """<li>%s<li>\n""" % (item,)

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
        thisNavStyle += " nav-%s" % (navStyle,)

    if navPull:
        navPull = "pull-%s" % (navPull,)

    if navDirection == "stacked":
        navDirection = "nav-stacked"

    if breadcrumb is True:
        breadcrumb = "breadcrumb"

    if pager is True:
        pager = "pager"

    if thumbnails is True:
        thumbnails = "thumbnails"

    if mediaList is True:
        mediaList = "media-list"

    ul = """
        <ul class="%s %s %s %s %s %s %s %s %s %s %s">
            %s
        </ul>
    """ % (unstyled, inline, dropDownMenu, role, navPull, thisNavStyle, navDirection, breadcrumb, pager, thumbnails, mediaList, thisList,)

    return ul


## LAST MODIFIED : April 29, 2013
## CREATED : April 29, 2013
## AUTHOR : DRYX
def li(
        content="",
        span=False,
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=False,
        navDropDown=False,
        pager=False):
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
    falseList = [disabled, submenuClass, submenuTitle, navStyle, navDropDown, pager, span]
    for i in range(len(falseList)):
            if not falseList[i]:
                falseList[i] = ""
    [disabled, submenuClass, submenuTitle, navStyle, navDropDown, pager, span] =falseList

    if disabled:
        disabled = """disabled"""

    if submenuTitle is True:
        submenuClass = "dropdown-submenu"
        submenuTitle = """<a tabindex="-1" href="#">%s</a>""" % (submenuTitle,)

    if navStyle == "active":
        pass
    elif navStyle:
        navStyle = "nav-%s" % (navStyle,)

    if navDropDown:
        navDropDown = """dropdown"""

    if span:
        span = "span%s" % (span,)

    li = """
        <li class="%s %s %s %s %s" id="  ">
            %s
            %s
        </li>""" % (span, disabled, submenuClass, navStyle, submenuTitle, pager, navDropDown, content,)

    if divider is True:
        li = """<li class="divider"></li>"""

    return li


## LAST MODIFIED : April 29, 2013
## CREATED : April 29, 2013
## AUTHOR : DRYX
def a(
        content="",
        href=False,
        tableIndex=False,
        triggerStyle=False):
    """Generate an anchor - TBS style

    **Key Arguments:**
        - ``content`` -- the content
        - ``href`` -- the href link for the anchor
        - ``tableIndex`` -- table index for the dropdown menus [ False | -1 ]
        - ``triggerStyle`` -- link to be used as a dropDown or tab trigger? [ False | "dropdown" | "tab" ]


    **Return:**
        - ``a`` -- the a
    """
    triggerClass = ""
    dropdownCaret = ""

    falseList = [href, triggerClass, triggerStyle, tableIndex, dropdownCaret]
    for i in range(len(falseList)):
            if not falseList[i]:
                falseList[i] = ""
    [href, triggerClass, triggerStyle, tableIndex, dropdownCaret] = falseList

    if tableIndex is True:
        tableIndex = """tableIndex = "%s" """ % (tableIndex,)

    if triggerStyle == "dropdown":
        triggerClass = "dropdown-toggle"
        triggerToggle = """data-toggle="dropdown" """
        dropdownCaret = """<b class="caret"></b> """
    elif triggerStyle == "tab":
        triggerToggle = """data-toggle="tab" """
    else:
        triggerToggle = ""

    a = """
        <a %s href="%s" class="%s  " id="  " %s>
            %s
            %s
        </a>""" % (tableIndex, href, triggerClass, triggerToggle, content, dropdownCaret)

    return a


## LAST MODIFIED : April 13, 2013
## CREATED : April 13, 2013
## AUTHOR : DRYX
def ol(itemList=[]):
    """An ordered list

    **Key Arguments:**
        - ``itemList`` -- a list of items to be included in the ordered list

    **Return:**
        - ol
    """
    thisList = ""
    for item in itemList:
        thisList += """<li>%s<li>\n""" % (item,)

    ol = """
        <ol>
            %s
        </ol>
    """ % (thisList,)

    return ol


## LAST MODIFIED : April 13, 2013
## CREATED : April 13, 2013
## AUTHOR : DRYX
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
        termList += """
            <dt>%s</dt>
            <dd>%s</dd>
        """ % (k, v)

    if sideBySide:
        sideBySide = "dl-horizontal"
    else:
        sideBySide = ""

    descriptionLists = """
        <dl class="%s">
            %s
        </dl>
    """ % (sideBySide, termList,)

    return descriptionLists

## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def code(
        content="",
        inline=True,
        scroll=False):
    """Generate a code section

    **Key Arguments:**
        - ``content`` -- the content of the code block
        - ``inline`` -- inline or block?
        - ``scroll`` -- give the block a scroll bar on y-axis?

    **Return:**
        - ``code`` -- the code section
    """
    if scroll:
        scroll = "pre-scrollable"
    else:
        scroll = ""

    if inline:
        code = """<code>%s</code>""" % (content,)
    else:
        code = """
            <pre class="%s">
                %s
            </pre>""" % (scroll, content,)

    return code


## LAST MODIFIED : 20130508
## CREATED : 20130508
## AUTHOR : DRYX
def heroUnit(
        headline="",
        tagline="",
        buttonStyle="primary",
        buttonText=""
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
            <h1>%s</h1>
            <p>%s</p>
            <p>
                <a href="%s" class="btn btn-%s btn-large">
                  %s
                </a>
            </p>
        </div>""" % (headline, tagline, buttonHref, buttonStyle, buttonText,)

    return heroUnit


## LAST MODIFIED : 20130508
## CREATED : 20130508
## AUTHOR : DRYX
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
            <h1>%s <small>%s</small></h1>
        </div>""" % (content,)

    return pageHeader

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()


###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
