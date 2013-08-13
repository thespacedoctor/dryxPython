#!/usr/local/bin/python
# encoding: utf-8
"""
_dryxTBS_code
=============================
:Summary:
    Code partial for dryxTwitterBootstrap

:Author:
    David Young

:Date Created:
    April 16, 2013

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
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ################ >ACTION(S) ################
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
###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
