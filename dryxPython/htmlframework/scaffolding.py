#!/usr/bin/python
# -*- coding: utf-8 -*-
""" _dryxTBS_scaffolding.py
=============================
:Summary:
    Layout / scaffolding partial for the dryxTwitterBootstrap module

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
## SNIPPET CREATED
## LAST MODIFIED : April 11, 2013
## CREATED : April 11, 2013
## AUTHOR : DRYX
def htmlDocument(content=''):
    """The doctype and html tags

    **Key Arguments:**
        - ``content`` -- the head and body of the html page

    **Return:**
        - ``doctype`` -- the HTML5 doctype """

    htmlDocument = \
        """Content-Type: text/html\n
        <!DOCTYPE html>
        <html lang="en">
            %s
        </html>
    """ \
        % (content, )
    return htmlDocument


## SNIPPET CREATED
## LAST MODIFIED : May 28, 2013
## CREATED : May 28, 2013
## AUTHOR : DRYX
def head(
    relativeUrlBase='',
    mainCssFileName="main.css",
    pageTitle="",
    extras="",
    ):
    """Generate an html head element for your webpage

    **Key Arguments:**
        ``relativeUrlBase`` -- relative base url for js, css, image folders
        ``pageTitle`` -- well, the page title!
        ``mainCssFileName`` -- css file name
        ``extras`` -- any extra info to be included in the ``head`` element

    **Return:**
        - ``head`` -- the head """

    cssUrl = relativeUrlBase + '/assets/styles/css/' + mainCssFileName
    cssLink = """
        <link rel="stylesheet" href="%s" type="text/css" />
    """ % (cssUrl, )

    head = """
    <!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
    <!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
    <!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>%s</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        %s
        %s
    </head>
    """ % (pageTitle, cssLink, extras)

    return head

## SNIPPET CREATED
## LAST MODIFIED : May 31, 2013
## CREATED : May 31, 2013
## AUTHOR : DRYX
def body(
        navBar=False,
        content="",
        htmlId="",
        extraAttr="",
        relativeUrlBase="",
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
            var _gaq=[['_setAccount','%s'],['_trackPageview']];
            (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
            g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
            s.parentNode.insertBefore(g,s)}(document,'script'));
        </script>
        """ % (googleAnalyticsCode,)
    else:
        googleAnalyticsCode = ""

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
      <body id="%s" %s>
      <!--[if lt IE 7]>
        <p class="chromeframe">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">activate Google Chrome Frame</a> to improve your experience.</p>
      <![endif]-->
        %s
        %s
      <script src="%s/assets/js/%s"></script>
      %s
      </body><!-- /#%s-->
      """ \
        % (
        htmlId,
        extraAttr,
        navBar,
        container,
        relativeUrlBase,
        jsFileName,
        googleAnalyticsCode,
        htmlId,
        )

    return body

## SNIPPET CREATED
## LAST MODIFIED : March 27, 2013
## CREATED : March 27, 2013
## AUTHOR : DRYX
def row(
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
        htmlId = """id="%s" """ % (htmlId, )
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
        <div class="row%s %s %s %s %s" %s>
            %s
        </div>
    """ % (
        responsive,
        htmlClass,
        onPhone,
        onTablet,
        onDesktop,
        htmlId,
        columns,
        )
    return row
















# xxxxxxxxxxx-still needs work and snippets-xxxxxxxxxxxxxx






# xxx-replace
## LAST MODIFIED : December 17, 2012
## CREATED : December 17, 2012
## AUTHOR : DRYX

def get_simple_div(htmlId=None, blockContent=None):
    """ Generate a basic <div> with block-content

  ****Key Arguments:****
    - ``htmlId`` -- the html id attribute
    - ``blockContent`` -- content to be surrounded by html div tag

  **Return:**
    - ``div`` """

  # ############### > IMPORTS ################
  # ############### > VARIABLE SETTINGS ######
  # ############### >ACTION(S) ################
    div = get_html_block(dict(
        tag='div',
        htmlId=htmlId,
        blockContent=blockContent,
        ))
    return div


# xxx-replace
## LAST MODIFIED : December 12, 2012
## CREATED : December 12, 2012
## AUTHOR : DRYX

def get_javascript_block(jsPath):
    """ Create a javascript *<script>* html code block

  ****Key Arguments:****
    - ``jsPath`` -- path the js file

  **Return:**
    - ``block`` -- HTML code block """

  # ############### > IMPORTS ################
  # ############### > VARIABLE SETTINGS ######
  # ############### >ACTION(S) ################
    block = """<script src="%s" type="text/javascript" charset="utf-8"></script>""" % (jsPath, )
    return block


# xxx-replace
## LAST MODIFIED : December 11, 2012
## CREATED : December 11, 2012
## AUTHOR : DRYX

def get_html_block(attributeDict):
    """Get an HTML code block (tag) which in turn can be meshed together to build webpages.

    **Variable Attributes:**
      - ``attributeDict`` -- dictionary with the following keywords:
      - ``tag`` -- the html tag (a, div, span ...)
      - ``htmlClass`` -- the html element class
      - ``htmlId`` -- the html element id
      - ``href`` -- linked url
      - ``blockContent`` -- actual content to be placed in html code block
      - ``jsEvents`` -- inline javascript event
      - ``extraAttr`` -- extra incline css attributes and/or handles
      - ``src`` -- source for images
      - ``alt`` -- alternative text for images
      - ``action`` -- action used in forms
      - ``method`` -- method used in forms
      - ``type`` -- type of object

    **Returns:**
      - ``block`` -- the html block

    attributeDict template -- dict(tag=___,
                                    htmlClass:divVerticalKids/divHorizontalKids,
                                    htmlId=___,
                                    jsEvents=___,
                                    extraAttr=___,
                                    blockContent=___,
                                    href=___,
                                    src=___,
                                    alt=___,
                                    action=___,
                                    method=___,
                                    type=___
                                  ) """

  # ############### > IMPORTS ################
  # ############### > VARIABLE SETTINGS ######
    d = attributeDict
    block = '<%s ' % (d['tag'], )  # THE HTML BLOCK
  # ############### >ACTION(S) ################
  # # SET THE ATTRIBUTES
    if d.has_key('htmlClass'):
        block += """class="%s" """ % (d['htmlClass'], )
    if d.has_key('htmlId'):
        block += """id="%s" """ % (d['htmlId'], )
    if d.has_key('jsEvents'):
        block += """%s """ % (d['jsEvents'], )
    if d.has_key('extraAttr'):
        block += """%s """ % (d['extraAttr'], )
    if d.has_key('href'):
        block += """href="%s" """ % (d['href'], )
        if d['href'][0] not in ['.', '/'] and 'index.py' not in d['href']:
            block += """target="_blank" """  # OPEN EXTERNAL LINKS IN NEW TAB
    if d.has_key('src'):
        block += """src="%s" """ % (d['src'], )
    if d.has_key('alt'):
        block += """alt="%s" """ % (d['alt'], )
    if d.has_key('action'):
        block += """action="%s" """ % (d['action'], )
    if d.has_key('method'):
        block += """method="%s" """ % (d['method'], )
    if d.has_key('type'):
        block += """type="%s" """ % (d['type'], )
    block += '>'
  # # SET THE CONTENT
    if d.has_key('blockContent'):
        block += str(d['blockContent'])
  # # CLOSE THE BLOCK
    if d.has_key('htmlId'):
        block += '</%s><!--- /#%s --->' % (d['tag'], d['htmlId'])
    else:
        block += '</%s>' % (d['tag'], )
    return block



## LAST MODIFIED : March 27, 2013
## CREATED : March 27, 2013
## AUTHOR : DRYX

def grid_column(
    log,
    span=1,
    offset=0,
    content='',
    htmlId=False,
    htmlClass=False,
    onPhone=True,
    onTablet=True,
    onDesktop=True,
    ):
    """ Get a column block for the Twiiter Bootstrap static layout grid.

    **Key Arguments:**
        - ``log`` -- logger
        - ``span`` -- the relative width of the column
        - ``offset`` -- increase the left margin of the column by this amount
        - ``htmlId`` -- the id of the column
        - ``htmlClass`` -- the class of the column
        - ``onPhone`` -- does this column get displayed on a phone sized screen
        - ``onTablet`` -- does this column get displayed on a tablet sized screen
        - ``onDesktop`` -- does this column get displayed on a desktop sized screen

    **Return:**
        - ``column`` -- the column """

    if htmlId:
        htmlId = """id="%s" """ % (htmlId, )
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
    column = """
        <div class="span%s offset%s %s %s %s %s" %s>
            %s
        </div>
    """ % (
        span,
        offset,
        htmlClass,
        onPhone,
        onTablet,
        onDesktop,
        htmlId,
        content,
        )
    return column


###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################
## SNIPPET CREATED
## LAST MODIFIED : March 27, 2013
## CREATED : March 27, 2013
## AUTHOR : DRYX
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
        htmlId = """id="%s" """ % (htmlId, )
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
        <div class="container%s %s %s %s %s" %s>
            %s
        </div>
    """ % (
        responsive,
        htmlClass,
        onPhone,
        onTablet,
        onDesktop,
        htmlId,
        content,
        )
    return container

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
