#!/usr/bin/env python
# encoding: utf-8
"""
sortable_table.py
=======================
:Summary:
    A sortable, customisable HTML table 

:Author:
    David Young

:Date Created:
    May 27, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import datetime
import re
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil
from .__init__ import tbody
from ..__init__ import *


###################################################################
# CLASSES                                                         #
###################################################################
class sortable_table():

    """
    The worker class for the sortable_table module

    **Key Arguments:**
        - ``dbConn`` -- mysql database connection
        - ``log`` -- logger
        - ``currentPageUrl`` -- the baseurl for the webpage
        - ``columnNameList`` -- a list of column objects for the table
        - ``defaultSort`` -- the column to sort on by default
        - ``tableRowsDictionary`` -- dictionary of column names and values (e.g. a mysql query result)
    """
    ## Initialisation

    def __init__(
            self,
            log,
            dbConn=False,
            currentPageUrl="",
            columnNameList=[],
            defaultSort=False,
            tableRowsDictionary={}
    ):
        self.log = log
        self.dbConn = dbConn
        self.currentPageUrl = currentPageUrl
        self.columnNameList = columnNameList
        self.defaultSort = defaultSort
        self.tableRowsDictionary = tableRowsDictionary
        # xt-self-arg-tmpx

        ## Variable Data Atrributes
        self.colors = ["green", "red", "blue", "yellow",
                       "orange", "violet", "magenta", "cyan", ]
        self.columndDisplayNameDictionary = {}
        self.headerPopoverText = "click to sort"
        self.searchKeyAndColumn = False
        self.columnsToHide = []

        ## determine how table is to be sorted from url
        thisSort = re.search(
            r'sortBy=(\w+)&',
            self.currentPageUrl,
            flags=0  # re.S
        )
        if thisSort:
            thisSort = thisSort.group(1)
        elif self.defaultSort:
            thisSort = self.defaultSort
        else:
            thisSort = False

        thisSortDesc = re.search(
            r'sortDesc=(\w+)&?',
            self.currentPageUrl,
            flags=0  # re.S
        )
        if thisSortDesc:
            thisSortDesc = thisSortDesc.group(1)
        else:
            thisSortDesc = "False"

        arrow = ""
        if "true" in thisSortDesc.lower():
            arrow = coloredText(
                text="""&nbsp&nbsp<i class="icon-arrow-up4"></i>""" % locals(),
                color="red",
            )
        else:
            arrow = coloredText(
                text="""&nbsp&nbsp<i class="icon-arrow-down4"></i>""",
                color="red",
            )
        self.thisSort = thisSort
        self.thisSortDesc = thisSortDesc
        self.arrow = arrow

        # remove sort and sortDesc from url to general a baseUrl for header
        # sorting
        reSort = re.compile(r'sortBy=\w+&?')
        reDesc = re.compile(r'sortDesc=\w+&?')
        self.baseUrl = reSort.sub("", self.currentPageUrl)
        self.baseUrl = reDesc.sub("", self.baseUrl)
        thisUrl = self.baseUrl
        if thisUrl[-3:] == ".py":
            thisUrl = "%(thisUrl)s?" % locals()
        elif thisUrl[-1:] not in ["?", "&"]:
            thisUrl = "%(thisUrl)s&" % locals()
        self.baseUrl = thisUrl

        return None

    def close(self):
        del self
        return None

    ## Method Attributes
    def get(self):
        """get the sortable_table object
    
        **Return:**
            - ``sortable_table``
        """

        tableHead = self.get_table_head()
        tbody = self.get_table_body()

        sortable_table = table(
            caption='',
            thead=tableHead,
            tbody=tbody,
            striped=True,
            bordered=False,
            hover=True,
            condensed=True
        )

        return sortable_table

    def get_table_head(
            self):
        """get table head
        
        **Return:**
            - ``tableHead`` -- the table head
        """
        ## init variables
        tableHead = ""

        ## build the table header
        _popover = popover(
            tooltip=True,
            placement="bottom",  # [ top | bottom | left | right ]
            trigger="hover",  # [ False | click | hover | focus | manual ]
            title=self.headerPopoverText,
            content=False,
            delay=600
        )

        index = 0
        for c in self.columnNameList:
            ## build sort url
            direction = "False"
            if self.thisSort == c and self.thisSortDesc == "False":
                direction = "True"
            thisUrl = self.baseUrl
            newSortUrl = """%(thisUrl)ssortBy=%(c)s&sortDesc=%(direction)s""" % locals()

            thisArrow = ""
            if c.lower() == self.thisSort.lower():
                thisArrow = self.arrow

            ## add text color and change display names if necessary
            if c in self.columndDisplayNameDictionary.keys():
                thisText = self.columndDisplayNameDictionary[c]
            else:
                thisText = c
            self.columndDisplayNameDictionary[c] = coloredText(
                text=thisText + thisArrow,
                color=self.colors[index],
                size=False,  # 1-10
                pull=False,  # "left" | "right"
            )
            if index < len(self.colors) - 1:
                index += 1
            else:
                index = 0

            if c not in self.columnsToHide:
                cell = th(
                    content=self.columndDisplayNameDictionary[c],
                    color=False,
                    href=newSortUrl,
                    popover=_popover
                )
                tableHead = "%(tableHead)s %(cell)s" % locals()

        tableHead = tr(
            cellContent=tableHead,
            color=False,
        )
        tableHead = thead(
            trContent=tableHead
        )
        return tableHead

    def get_table_body(
            self):
        """get table body
        
        **Return:**
            - ``tableBody``
        """
        theseTickets = ""

        ## build the table body
        for obj in self.tableRowsDictionary:

            if self.searchKeyAndColumn:
                regex = re.compile(r'^(.*?\?).*')
                href = regex.sub("\g<1>", self.baseUrl, count=1)
                href = href + \
                    self.searchKeyAndColumn[0] + "=" + \
                    obj[self.searchKeyAndColumn[1]]
            else:
                href = False

            tableRow = ""
            index = 0
            for c in self.columnNameList:
                try:
                    obj[c] = float(obj[c])
                except:
                    pass
                if c.lower() in ["radeg", "decdeg"]:
                    obj[c] = "%6.3f" % obj[c]
                elif (isinstance(obj[c], float) or isinstance(obj[c], long)) and obj[c]:
                    obj[c] = "%6.2f" % obj[c]
                elif not obj[c] or (isinstance(obj[c], str) and ("unkn" in obj[c].lower())):
                    obj[c] = ""
                elif isinstance(obj[c], datetime.datetime):
                    # obj[c] = "boom"
                    relativeDate = dcu.pretty_date(
                        date=obj[c]
                    )
                    thisDate = str(obj[c])[:10]
                    thisDate = coloredText(
                        text="(%(thisDate)s)" % locals(),
                        color="grey",
                        size=2,
                    )
                    obj[c] = "%(relativeDate)s %(thisDate)s" % locals()

                obj[c] = coloredText(
                    text=obj[c],
                    color=self.colors[index],
                )
                if index < len(self.colors) - 1:
                    index += 1
                else:
                    index = 0

                if c not in self.columnsToHide:
                    cell = td(
                        content=obj[c],
                    )
                    tableRow = "%(tableRow)s %(cell)s" % locals()

            tableRow = tr(
                cellContent=tableRow,
                color=False,
                href=href,
                popover=False
            )
            theseTickets = "%(theseTickets)s%(tableRow)s" % locals()

        tableBody = tbody(
            trContent=theseTickets
        )
        return tableBody

    # use the tab-trigger below for new method
    # xt-class-method

    ## Override Method Attributes
    # method-override-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# xt-worker-def
# use the tab-trigger below for new function
# xt-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

############################################
# CODE TO BE DEPECIATED                    #
############################################
if __name__ == '__main__':
    main()

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
