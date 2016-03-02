#!/usr/local/bin/python
# encoding: utf-8
"""
download_flicker_image.py
=========================
:Summary:
    Download a flicker image given the flicker URL

:Author:
    David Young

:Date Created:
    December 18, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython

# xdocopt-usage-tempx
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import readline
import glob
import pickle
import re
from docopt import docopt
from . import singleWebDocumentDownloader
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times
# from ..__init__ import *


def tab_complete(text, state):
    return (glob.glob(text + '*') + [None])[state]


def main(arguments=None):
    """
    The main function used when ``download_flicker_image.py`` is run as a single script from the cl, or when installed as a cl command
    """
    # setup the command-line util settings
    su = tools(
        arguments=arguments,
        docString=__doc__,
        logLevel="DEBUG",
        options_first=False
    )
    arguments, settings, log, dbConn = su.setup()

    # tab completion for raw_input
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(tab_complete)

    # unpack remaining cl arguments using `exec` to setup the variable names
    # automatically
    for arg, val in arguments.iteritems():
        if arg[0] == "-":
            varname = arg.replace("-", "") + "Flag"
        else:
            varname = arg.replace("<", "").replace(">", "")
        if isinstance(val, str) or isinstance(val, unicode):
            exec(varname + " = '%s'" % (val,))
        else:
            exec(varname + " = %s" % (val,))
        if arg == "--dbConn":
            dbConn = val
        log.debug('%s = %s' % (varname, val,))

    ## START LOGGING ##
    startTime = times.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE download_flicker_image.py AT %s' %
        (startTime,))

    # call the worker function
    # x-if-settings-or-database-credientials
    download_flicker_image(
        log=log,
        url=url,
    )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE download_flicker_image.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################


class download_flicker_image():

    """
    The worker class for the download_flicker_image module

    **Key Arguments:**
        - ``log`` -- logger
        - ``url`` -- url to the flicker page

    **Todo**
        - @review: when complete, clean download_flicker_image class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
        self,
        log,
        url,
    ):
        self.log = log
        log.debug("instansiating a new 'download_flicker_image' object")
        self.url = url
        # xt-self-arg-tmpx

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """get the download_flicker_image object

        **Return:**
            - ``download_flicker_image``

        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        self._find_image_link_in_flicker_html()

        self.log.info('completed the ``get`` method')
        return None

    def get_url(
            self):
        """ find image link in flicker html

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _find_image_link_in_flicker_html method
            - @review: when complete add logging
        """
        self.log.info(
            'starting the ``_find_image_link_in_flicker_html`` method')

        url = False
        urlDoc = singleWebDocumentDownloader(
            url=self.url,
            downloadDirectory="/tmp",
            log=self.log,
            timeStamp=1,
            credentials=False
        )

        if not urlDoc:
            return url

        import codecs
        pathToReadFile = urlDoc
        try:
            self.log.debug("attempting to open the file %s" %
                           (pathToReadFile,))
            readFile = codecs.open(pathToReadFile, encoding='utf-8', mode='r')
            thisData = readFile.read()
            readFile.close()
        except IOError, e:
            message = 'could not open the file %s' % (pathToReadFile,)
            self.log.critical(message)
            raise IOError(message)
        readFile.close()

        reOriginalImage = re.compile(
            r'\{"label":"Original","file":"(?P<filename>.*?)","url":"(?P<url>.*?)","width"', re.S)

        matchObject = re.search(
            r'\{"label":"Original","file":"(?P<filename>.*?)","url":"(?P<url>.*?)","width"', thisData, re.S)
        if matchObject:
            url = matchObject.group("url").replace("\/", "/")

        self.log.info(
            'completed the ``_find_image_link_in_flicker_html`` method')
        return url

    # use the tab-trigger below for new method
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx

# xt-class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# xt-worker-def

# use the tab-trigger below for new function
# xt-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
