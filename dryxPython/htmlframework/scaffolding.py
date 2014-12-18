#!/usr/bin/python
# -*- coding: utf-8 -*-
""" scaffolding.py
=============================
:Summary:
    Layout / scaffolding module for TBS htmlframework

:Author:
    David Young

:Date Created:
    March 27, 2013

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
# LAST MODIFIED : April 11, 2013
# CREATED : April 11, 2013
# AUTHOR : DRYX
def htmlDocument(
        contentType=False,
        content='',
        attachmentSaveAsName=False):
    """The doctype and html tags

    **Key Arguments:**
        - ``content`` -- the head and body of the html page
        - ``attachmentSaveAsName`` -- save file as this name instead of opening in browser

    **Return:**
        - ``contentType`` -- the content type [ "text/html" ]
        - ``doctype`` -- the HTML5 doctype
    """

    if attachmentSaveAsName is not False:
        contentType = """Content-Disposition: attachment; filename=%(attachmentSaveAsName)s""" % locals(
        )
    elif not contentType:
        contentType = ""
    else:
        contentType = "Content-type: %(contentType)s" % locals()

    content = content.strip()

    if "text/plain" in contentType or "text/csv" in contentType or attachmentSaveAsName is not False:
        htmlDocument = \
            """%(contentType)s\n
%(content)s
""" % locals()
    else:
        htmlDocument = \
            """%(contentType)s\n
            <!DOCTYPE html>
            <html lang="en">
                %(content)s
            </html>
        """ \
            % locals()
    return htmlDocument.strip()


# SNIPPET CREATED
# LAST MODIFIED : May 28, 2013
# CREATED : May 28, 2013
# AUTHOR : DRYX
def head(
    relativeUrlBase=False,
    mainCssFileName="main.css",
    pageTitle="",
    extras="",
    faviconLocation=False,
    assetsDirectory=False
):
    """Generate an html head element for your webpage

    **Key Arguments:**
        ``relativeUrlBase`` -- relative base url for js, css, image folders
        ``pageTitle`` -- well, the page title!
        ``mainCssFileName`` -- css file name
        ``extras`` -- any extra info to be included in the ``head`` element
        ``faviconLocation`` -- path to faviconLocation if not in document root

    **Return:**
        - ``head`` -- the head """

    if not relativeUrlBase:
        relativeUrlBase = ""

    cssUrl = """%(relativeUrlBase)s/assets/styles/css/%(mainCssFileName)s""" % locals()
    cssLink = """
        <link rel="stylesheet" href="%(cssUrl)s" type="text/css" />
    """ % locals()

    if faviconLocation is not False:
        faviconLocation = """
            <link rel="shortcut icon" href="%(faviconLocation)s" />
        """ % locals()
    else:
        faviconLocation = ""

    head = """
    <!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
    <!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
    <!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>%(pageTitle)s</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        %(cssLink)s
        %(extras)s
        %(faviconLocation)s
    </head>
    """ % locals()

    return head

# SNIPPET CREATED
# LAST MODIFIED : May 31, 2013
# CREATED : May 31, 2013
# AUTHOR : DRYX


def body(
        navBar=False,
        content="",
        htmlId="",
        extraAttr="",
        relativeUrlBase=False,
        responsive=True,
        googleAnalyticsCode=False,
        jsFileName="main.js"
):
    """Generate an HTML body

    **Key Arguments:**
        - ``navBar`` -- the top navigation bar
        - ``htmlId`` -- *id* attribute of the body
        - ``content`` -- body content built from smaller HTML code blocks
        - ``extraAttr`` -- an extra attributes to be added to the body definition
        - ``relativeUrlBase`` -- how to get back to the document root
        - ``responsive`` -- should the webpage be responsive to screen-size?
        - ``googleAnalyticsCode`` -- google analytics code for the website
        - ``jsFileName`` -- the name of the main javascript file

    **Return:**
        - ``body`` -- the body
    """
    if not navBar:
        navBar = ""

    if googleAnalyticsCode:
        googleAnalyticsCode = """
        <!-- Google Analytics -->
        <script>
            var _gaq=[['_setAccount','%(googleAnalyticsCode)s'],['_trackPageview']];
            (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
            g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
            s.parentNode.insertBefore(g,s)}(document,'script'));
        </script>
        """ % locals()
    else:
        googleAnalyticsCode = ""

    if relativeUrlBase is False:
        relativeUrlBase = ""

    container = _container(
        responsive=responsive,
        content=content,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
    )

    body = \
        """
      <body id="%(htmlId)s" %(extraAttr)s>
      <!--[if lt IE 7]>
        <p class="chromeframe">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">activate Google Chrome Frame</a> to improve your experience.</p>
      <![endif]-->
        %(navBar)s
        %(container)s
      <script src="%(relativeUrlBase)s/assets/js/%(jsFileName)s"></script>
      %(googleAnalyticsCode)s
      </body><!-- /#%(htmlId)s-->
      """ \
        % locals()

    return body

# SNIPPET CREATED
# LAST MODIFIED : March 27, 2013
# CREATED : March 27, 2013
# AUTHOR : DRYX


def grid_row(
    responsive=True,
    columns='',
    htmlId=False,
    htmlClass=False,
    onPhone=True,
    onTablet=True,
    onDesktop=True,
):
    """Create a row using the Twitter Bootstrap static layout grid.
    The static Bootstrap grid system utilizes 12 columns.

    **Key Arguments:**
        - ``responsive`` -- fluid layout if true, fixed if false
        - ``columns`` -- coulmns to be included in this row
        - ``htmlId`` -- the id of the row
        - ``htmlClass`` -- the class of the row
        - ``onPhone`` -- does this row get displayed on a phone sized screen
        - ``onTablet`` -- does this row get displayed on a tablet sized screen
        - ``onDesktop`` -- does this row get displayed on a desktop sized screen

    **Return:**
        - ``row`` -- the row """

    if responsive:
        responsive = '-fluid'
    else:
        responsive = ''
    if htmlId:
        htmlId = """id="%(htmlId)s" """ % locals()
    else:
        htmlId = ''
    if not htmlClass:
        htmlClass = ''
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
    row = """
        <div class="row%(responsive)s %(htmlClass)s %(onPhone)s %(onTablet)s %(onDesktop)s" %(htmlId)s>
            %(columns)s
        </div>
    """ % locals()
    return row


# LAST MODIFIED : March 27, 2013
# CREATED : March 27, 2013
# AUTHOR : DRYX
def grid_column(
    span=1,
    offset=0,
    content='',
    htmlId=False,
    htmlClass=False,
    pull=False,
    onPhone=True,
    onTablet=True,
    onDesktop=True,
    dataspy=False
):
    """ Get a column block for the Twiiter Bootstrap static layout grid.

    **Key Arguments:**
        - ``log`` -- logger
        - ``span`` -- the relative width of the column
        - ``offset`` -- increase the left margin of the column by this amount
        - ``htmlId`` -- the id of the column
        - ``htmlClass`` -- the class of the column
        - ``pull`` -- left, right, or center
        - ``onPhone`` -- does this column get displayed on a phone sized screen
        - ``onTablet`` -- does this column get displayed on a tablet sized screen
        - ``onDesktop`` -- does this column get displayed on a desktop sized screen

    **Return:**
        - ``column`` -- the column """

    if htmlId:
        htmlId = """id="%(htmlId)s" """ % locals()
    else:
        htmlId = ''
    if not htmlClass:
        htmlClass = ''

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

    if pull:
        pull = "pull-%(pull)s" % locals()
    else:
        pull = ""

    if dataspy is not False:
        dataspy = """data-spy="affix" data-offset-top="200" """
    else:
        dataspy = ""

    column = """
        <div %(dataspy)s class="span%(span)s offset%(offset)s %(htmlClass)s %(phoneClass)s %(tabletClass)s %(desktopClass)s %(pull)s" %(htmlId)s>
            %(content)s
        </div>
    """ % locals()
    return column


# LAST MODIFIED : April 30, 2014
# CREATED : April 30, 2014
# AUTHOR : DRYX
def row_adjustable(
    span=12,
    offset=0,
    content='',
    htmlId=False,
    htmlClass=False,
    onPhone=True,
    onTablet=True,
    onDesktop=True
):
    """row adjustable

    **Key Arguments:**
        - ``span`` -- the relative width of the column
        - ``offset`` -- increase the left margin of the column by this amount
        - ``htmlId`` -- the id of the column
        - ``htmlClass`` -- the class of the column
        - ``onPhone`` -- does this column get displayed on a phone sized screen
        - ``onTablet`` -- does this column get displayed on a tablet sized screen
        - ``onDesktop`` -- does this column get displayed on a desktop sized screen


    **Return:**
        - ``row`` -- the adjustable row

    **Todo**
        - @review: when complete, clean row_adjustable function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    # TEST THE ARGUMENTS

    ## VARIABLES ##
    column = grid_column(
        span=span,  # 1-12
        offset=offset,  # 1-12
        content=content
    )

    row = grid_row(
        responsive=True,
        columns=column,
        htmlId=htmlId,
        htmlClass=htmlClass,
        onPhone=onPhone,
        onTablet=onTablet,
        onDesktop=onDesktop
    )

    return row

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################
# SNIPPET CREATED
# LAST MODIFIED : March 27, 2013
# CREATED : March 27, 2013
# AUTHOR : DRYX


def _container(
    responsive=True,
    content='',
    htmlId=False,
    htmlClass=False,
    onPhone=True,
    onTablet=True,
    onDesktop=True,
):
    """ The over-all content container for the twitter bootstrap webpage

    **Key Arguments:**
        - ``responsive`` -- fluid layout if true, fixed if false
        - ``content`` -- html content of the container div
        - ``htmlId`` -- the id of the container
        - ``htmlClass`` -- the class of the container
        - ``onPhone`` -- does this container get displayed on a phone sized screen
        - ``onTablet`` -- does this container get displayed on a tablet sized screen
        - ``onDesktop`` -- does this container get displayed on a desktop sized screen

    **Return:**
        - None """

    if responsive:
        responsive = '-fluid'
    else:
        responsive = ''
    if htmlId:
        htmlId = """id="%(htmlId)s" """ % locals()
    else:
        htmlId = ''
    if not htmlClass:
        htmlClass = ''
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
    container = """
        <div class="container%(responsive)s %(htmlClass)s %(onPhone)s %(onTablet)s %(onDesktop)s" %(htmlId)s>
            %(content)s
        </div>
    """ % locals()
    return container

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
