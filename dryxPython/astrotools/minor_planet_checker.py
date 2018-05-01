#!/usr/local/bin/python
# encoding: utf-8
"""
*Check the minor planet centre for moving objects*

:Author:
    Ken Smith (adapted by David Young)

:Date Created:
    March 26, 2015

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    dat_minor_planet_checker <ra> <dec> <radiusArcmin> <mjd>

    -h, --help            show this help message
    ra                    ra
    dec                   dec
    radiusArcmin          radius in arcmins
    mjd                   mjd to 4 decimal places
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import readline
import glob
import collections
import pickle
import urllib
import urllib2
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times
from . import ra_to_sex, dec_to_sex
from mjd_to_date import mjd_to_date


def tab_complete(text, state):
    return (glob.glob(text + '*') + [None])[state]


def main(arguments=None):
    """
    *The main function used when ``minor_planet_checker.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    # setup the command-line util settings
    su = tools(
        arguments=arguments,
        docString=__doc__,
        logLevel="WARNING",
        options_first=True
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
        '--- STARTING TO RUN THE minor_planet_checker.py AT %s' %
        (startTime,))

    # call the worker function
    # x-if-settings-or-database-credientials
    mpc = minor_planet_checker(
        log=log,
        ra=ra,
        dec=dec,
        radius=int(radiusArcmin),
        mjd=float(mjd)
    )
    mpc = mpc.get()
    print mpc

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE minor_planet_checker.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################


class minor_planet_checker():

    """
    *The worker class for the minor_planet_checker module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``ra`` -- ra
        - ``dec`` -- dec
        - ``radius`` -- radius
        - ``mjd`` -- mjd
        - ``limitingMag`` -- limitingMag
        - ``urlNum`` -- urlNum
        - ``matchRadius`` -- matchRadius
        - ``showMovers`` -- showMovers

    .. todo::

        - @review: when complete, clean minor_planet_checker class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
        self,
        log,
        ra,
        dec,
        radius,
        mjd,
        limitingMag=24.0,
        urlNum=1,
        matchRadius=False,
        showMovers=True
    ):
        self.log = log
        self.log.debug("instansiating a new 'minor_planet_checker' object")
        self.ra = ra
        self.dec = dec
        self.radius = float(radius)
        self.mjd = mjd
        self.limitingMag = limitingMag
        self.urlNum = urlNum
        self.matchRadius = matchRadius
        self.showMovers = showMovers

        # xt-self-arg-tmpx

        if self.urlNum == 1:
            self.url = 'http://scully.cfa.harvard.edu/cgi-bin/mpcheck.cgi'
        elif self.urlNum == 2:
            self.url = 'http://mpcapp1.cfa.harvard.edu/cgi-bin/mpcheck.cgi'

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
        """
        *get the minor_planet_checker object*

        **Return:**
            - ``minor_planet_checker``

        .. todo::

            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.debug('starting the ``get`` method')

        self._send_request_to_minor_planet_centre()
        self._check_mp_match()

        if not self.moverName:
            self.moverName = "NO MPC MATCH FOUND"

        self.log.debug('completed the ``get`` method')
        return self.moverName

    def _send_request_to_minor_planet_centre(
            self):
        """
        *send request to minor planet centre*

        **Key Arguments:**
            # -

        **Return:**
            - None

        .. todo::

            - @review: when complete, clean _send_request_to_minor_planet_centre method
            - @review: when complete add logging
        """
        self.log.debug(
            'completed the ````_send_request_to_minor_planet_centre`` method')

        ra = self.ra
        dec = self.dec
        radius = self.radius
        limitingMag = self.limitingMag

        mpInfo = []

        # get ra and dec in correct format
        try:
            ra = float(ra)
            dec = float(dec)
            ra = ra_to_sex(
                ra=ra,
                delimiter=' '
            )
            dec = dec_to_sex(
                dec=dec,
                delimiter=' '
            )
        except Exception, e:
            self.log.error(
                "could not convert ra and dec to sexagesimal - failed with this error: %s " % (str(e),))
            return -1

        # The RA and dec must be in space delimited sexagesimal, but are given
        # here in decimal
        try:
            self.log.debug(
                "attempting to convert ra and dec to the fornat required by MPC")
            ra = ra.replace(":", " ")
            dec = dec.replace(":", " ")
        except Exception, e:
            self.log.error(
                "could not convert ra and dec to the fornat required by MPC - failed with this error: %s " % (str(e),))
            return -1

        # Generally we have the date in MJD, so convert to date fraction
        dateFract = mjd_to_date(
            log=self.log,
            mjd=self.mjd,
            fraction=True
        )
        year, month, day = dateFract.get().split(' ')

        # Minimum radius of 5 arcmins and max of 300 arcmins allowed.
        if radius < 5:
            pass
            # radius = 5
        if radius > 300:
            radius = 300

        # Setup an OrderedDict.  Used this because analysis of what the web page submits implies
        # that the values are sent in THIS order.  We'll do the same to simulate the web form
        # submission.
        values = collections.OrderedDict()
        values['year'] = year
        values['month'] = month
        values['day'] = day
        values['which'] = 'pos'
        values['ra'] = ra
        values['decl'] = dec
        values['TextArea'] = ''
        values['radius'] = radius
        values['limit'] = limitingMag
        values['oc'] = '500'
        values['sort'] = 'd'
        values['mot'] = 'h'
        values['tmot'] = 's'
        values['pdes'] = 'u'
        values['needed'] = 'f'
        values['ps'] = 'n'
        values['type'] = 'p'

        data = urllib.urlencode(values)

        txheaders = {
            'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/536.30.1 (KHTML, like Gecko) Version/6.0.5 Safari/536.30.1'}

        # create a request object
        req = urllib2.Request(self.url, data, txheaders)
        thisUrl = req.get_full_url()
        thisUrl += "?" + req.get_data()
        print thisUrl
        psResponsePage = urllib2.urlopen(req)

        # Because the cookie handler is installed, this should result in two
        # requests to the Server
        try:
            # Now send the file.
            psResponsePage = urllib2.urlopen(req).read()
            mpInfo = self._extract_mp_info(htmlPage=psResponsePage)

        except IOError, e:
            print "Something went horribly wrong."
            print e

        self.log.debug(
            'completed the ``_send_request_to_minor_planet_centre`` method')
        return mpInfo

    # use the tab-trigger below for new method
    def _extract_mp_info(
            self,
            htmlPage):
        """
        *Parse the data returned by the MP Center into a dictionary*

        **Key Arguments:**
            # -

        **Return:**
            - None

        .. todo::

            - @review: when complete, clean _extract_mp_info method
            - @review: when complete add logging
        """
        self.log.debug('starting the ``_extract_mp_info`` method')

        from BeautifulSoup import BeautifulSoup
        movers = []
        soup = BeautifulSoup(BeautifulSoup(htmlPage).prettify())
        preData = soup.findAll('pre')

        if len(preData) == 1:
            if preData[0].text is not None:
                dataRows = preData[0].text.split('\n')
                # We have some results.  Skip the 1st 2 lines (header line, one
                # blank line)
                if len(dataRows) > 2:
                    for line in dataRows[2:]:
                        row = list(
                            self._slice_string(line, 25, 11, 10, 6, 7, 7, 7, 7, 6, 100))

                        details = {'designation': row[0],
                                   'ra': row[1],
                                   'dec': row[2],
                                   'V': row[3],
                                   'raOff': row[4],
                                   'decOff': row[5],
                                   'raMot': row[6],
                                   'decMot': row[7],
                                   'orbit': row[8],
                                   'comments': row[9]}

                        movers.append(details)

        self.movers = movers

        self.log.debug('completed the ``_extract_mp_info`` method')
        return

    # use the tab-trigger below for new method
    def _slice_string(
            self,
            s,
            *args):
        """
        *Code to split a string into fixed fields defined by list of numbers provided in args*

        **Key Arguments:**
            # -

        **Return:**
            - None

        .. todo::

            - @review: when complete, clean _slice_string method
            - @review: when complete add logging
        """
        self.log.debug('starting the ``_slice_string`` method')

        position = 0
        for length in args:
            yield s[position:position + length].strip()
            position += length
        self.log.debug('completed the ``_slice_string`` method')

    # use the tab-trigger below for new method
    def _check_mp_match(
            self):
        """
        *Check that the returned data from MPC is a match.*

        **Key Arguments:**
            # -

        **Return:**
            - None

        .. todo::

            - @review: when complete, clean _check_mp_match method
            - @review: when complete add logging
        """
        self.log.debug('starting the ``_check_mp_match`` method')

        moverName = None

        # The self.movers are organised in order of increasing angular separation.
        # If the 1st row doesn't match, don't bother with the rest.
        if len(self.movers) > 0:
            # Get the offests.  We don't care which direction they are in. Value
            # should be < 1.0 arcmins.
            if self.movers[0]['raOff'] and self.movers[0]['decOff']:
                # Get rid of the NESW designations
                raOff = decOff = None
                try:
                    raOff = float(self.movers[0]['raOff'].replace('S', '').replace(
                        'N', '').replace('E', '').replace('W', ''))
                    decOff = float(self.movers[0]['decOff'].replace(
                        'S', '').replace('N', '').replace('E', '').replace('W', ''))
                except ValueError, e:
                    print "Can't convert the offsets %s, %s. Unable to check them." % (self.movers[0]['raOff'], self.movers[0]['decOff'])
                    self.moverName = moverName
                    return

                if self.matchRadius:
                    if raOff is not None and decOff is not None and raOff < self.matchRadius and decOff < self.matchRadius:
                        moverName = self.movers[0]['designation']
                    else:
                        print raOff
                        print decOff
                        print self.matchRadius
                else:
                    moverName = self.movers[0]['designation']

        self.moverName = moverName

        self.log.debug('completed the ``_check_mp_match`` method')
        return None

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
