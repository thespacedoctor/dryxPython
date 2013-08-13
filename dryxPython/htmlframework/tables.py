#!/usr/local/bin/python
# encoding: utf-8
"""
_dryxTBS_tables
=============================
:Summary:
    Tables partial for dryxTwitterBootstrap

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
def tr(
        cellContent="",
        color=False):
    """Generate a table row - TBS style

    **Key Arguments:**
        - ``cellContent`` -- the content - either <td>s or <th>s
        - ``color`` -- [ sucess | error | warning | info ]

    **Return:**
        - ``tr`` -- the table row
    """
    if color is False:
        color = ""

    tr = """
        <tr class="%s">
            %s
        </tr>""" % (color, cellContent,)

    return tr


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def th(
        content="",
        color=False):
    """Generate a table header cell - TBS style

    **Key Arguments:**
        - ``content`` -- the content
        - ``color`` -- [ sucess | error | warning | info ]

    **Return:**
        - ``th`` -- the table header cell
    """
    if color is False:
        color = ""

    th = """
        <th class="%s">
            %s
        </th>""" % (color, content,)

    return th


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def td(
        content="",
        color=False):
    """Generate a table data cell - TBS style

    **Key Arguments:**
        - ``content`` -- the content
        - ``color`` -- [ sucess | error | warning | info ]

    **Return:**
        - ``td`` -- the table data cell
    """
    if color is False:
        color = ""

    td = """
        <td class="%s">
            %s
        </td>""" % (color, content,)

    return td


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def tableCaption(
        content=""):
    """Generate a table caption - TBS style

    **Key Arguments:**
        - ``content`` -- the content

    **Return:**
        - ``tableCaption`` -- the table caption
    """
    tableCaption = """
        <tableCaption class="">
            %s
        </tableCaption>""" % (content,)

    return tableCaption


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def thead(
        trContent=""):
    """Generate a table head - TBS style

    **Key Arguments:**
        - ``trContent`` -- the table row content

    **Return:**
        - ``thead`` -- the table head
    """
    thead = """
        <thead class="">
            %s
        </thead>""" % (trContent,)

    return thead


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def tbody(
        trContent=""):
    """Generate a table body - TBS style

    **Key Arguments:**
        - ``trContent`` -- the table row content

    **Return:**
        - ``tbody`` -- the table body
    """
    tbody = """
        <tbody class="">
            %s
        </tbody>""" % (trContent,)

    return tbody


## LAST MODIFIED : April 16, 2013
## CREATED : April 16, 2013
## AUTHOR : DRYX
def table(
        caption="",
        thead="",
        tbody="",
        stripped=True,
        bordered=False,
        hover=True,
        condensed=False):
    """Generate a table - TBS style

    **Key Arguments:**
        - ``caption`` -- the table caption
        - ``thead`` -- the table head
        - ``tbody`` -- the table body
        - ``stripped`` -- Adds zebra-striping to any odd table row
        - ``bordered`` -- Add borders and rounded corners to the table.
        - ``hover`` -- Enable a hover state on table rows within a <tbody>
        - ``condensed`` -- Makes tables more compact by cutting cell padding in half.

    **Return:**
        - ``table`` -- the table
    """
    if stripped is True:
        stripped = "table-stripped"
    else:
        stripped = ""

    if bordered is True:
        bordered = "table-bordered"
    else:
        bordered = ""

    if hover is True:
        hover = "table-hover"
    else:
        hover = ""

    if condensed is True:
        condensed = "table-condensed"
    else:
        condensed = ""

    table = """
        <table class="table %s %s %s %s">
            %s
            %s
            %s
        </table>""" % (stripped, bordered, hover, condensed, caption, thead, tbody)

    return table

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################


###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
