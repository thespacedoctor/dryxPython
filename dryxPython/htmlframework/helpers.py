#!/usr/bin/python
# encoding: utf-8
"""
helpers
======================================
:Summary:
    Partial for the htmlframework modules - contains helper functions for building webpages

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
def unescape_html(dbConn, log, html):
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

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
