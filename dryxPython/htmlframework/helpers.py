#!/usr/bin/python
# encoding: utf-8
"""
helpers.py
======================================
:Summary:
    helpers for TBS htmlframework

:Author:
    David Young

:Date Created:
    May 28, 2013

:dryx syntax:
    - ``xxx`` = come back here and do some more work
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this code please email me: d.r.young@qub.ac.uk
"""


def main():
    pass

if __name__ == '__main__':
    main()
###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# xxx-replace
## LAST MODIFIED : May 28, 2013
## CREATED : May 28, 2013
## AUTHOR : DRYX


def unescape_html(html):
    """Unescape a string previously escaped with cgi.escape()

    **Key Arguments:**
        - ``dbConn`` -- mysql database connection
        - ``log`` -- logger
        - ``html`` -- the string to be unescaped

    **Return:**
        - ``html`` -- the unescaped string
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ################ > VARIABLE SETTINGS ######

    ################ >ACTION(S) ################
    html = html.replace("&lt;", "<")
    html = html.replace("&gt;", ">")
    html = html.replace("&quot;", '"')
    # this has to be last:
    html = html.replace("&amp;", "&")

    return html

## LAST MODIFIED : June 26, 2014
## CREATED : June 26, 2014
## AUTHOR : DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method
def hide_from_device(
        content="",
        onPhone=True,
        onTablet=True,
        onDesktop=True):
    """hide from device)

    **Key Arguments:**
        
        # copy usage method(s) here and select the following snippet from the command palette:
        # x-setup-docstring-keys-from-selected-usage-options

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean hide_from_device) function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    
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


    span = """<span class="%(phoneClass)s %(tabletClass)s %(desktopClass)s">%(content)s</span>""" % locals() 
    return span

# use the tab-trigger below for new function
# xt-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
