#!/usr/local/bin/python
# encoding: utf-8
"""
*Given a FITS file containing a 1D spectrum, this code will output an ascii version of the file*

:Author:
    David Young

:Date Created:
    October 19, 2015

Usage:
    dft_convert_spectrum_fits_to_ascii <pathToFits>

    -h, --help            show this help message
"""
################# GLOBAL IMPORTS ####################
import sys
import os
os.environ['TERM'] = 'vt100'
import readline
import glob
import pickle
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times


def tab_complete(text, state):
    return (glob.glob(text + '*') + [None])[state]


def main(arguments=None):
    """
    *The main function used when ``convert_spectrum_fits_to_ascii.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    # setup the command-line util settings
    su = tools(
        arguments=arguments,
        docString=__doc__,
        logLevel="WARNING",
        options_first=False,
        projectName=False
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
        '--- STARTING TO RUN THE convert_spectrum_fits_to_ascii.py AT %s' %
        (startTime,))

    # set options interactively if user requests
    if "interactiveFlag" in locals() and interactiveFlag:

        # load previous settings
        moduleDirectory = os.path.dirname(__file__) + "/resources"
        pathToPickleFile = "%(moduleDirectory)s/previousSettings.p" % locals()
        try:
            with open(pathToPickleFile):
                pass
            previousSettingsExist = True
        except:
            previousSettingsExist = False
        previousSettings = {}
        if previousSettingsExist:
            previousSettings = pickle.load(open(pathToPickleFile, "rb"))

        # x-raw-input
        # x-boolean-raw-input
        # x-raw-input-with-default-value-from-previous-settings

        # save the most recently used requests
        pickleMeObjects = []
        pickleMe = {}
        theseLocals = locals()
        for k in pickleMeObjects:
            pickleMe[k] = theseLocals[k]
        pickle.dump(pickleMe, open(pathToPickleFile, "wb"))

    # call the worker function
    # x-if-settings-or-database-credientials
    convert_spectrum_fits_to_ascii(
        log=log,
        fitsFilePath=pathToFits
    ).get()

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE convert_spectrum_fits_to_ascii.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return


class convert_spectrum_fits_to_ascii():
    """
    *The worker class for the convert_spectrum_fits_to_ascii module*

    **Key Arguments:**
        - ``log`` -- logger
         - ``fitsFilePath`` -- path to the fits file

    .. todo::

        - @review: when complete, clean convert_spectrum_fits_to_ascii class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
        self,
        log,
        fitsFilePath
    ):
        self.log = log
        log.debug("instansiating a new 'convert_spectrum_fits_to_ascii' object")
        self.fitsFilePath = fitsFilePath

        # xt-self-arg-tmpx

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions

        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """
        *get the convert_spectrum_fits_to_ascii object*

        **Return:**
            - ``convert_spectrum_fits_to_ascii``

        .. todo::

            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.debug('starting the ``get`` method')

        self.convert(
            log=self.log,
            pathToFitsFile=self.fitsFilePath,
            fluxScalingFactor=False
        )

        self.log.debug('completed the ``get`` method')
        return convert_spectrum_fits_to_ascii

    def convert(
        self,
        log,
        pathToFitsFile,
        fluxScalingFactor=False
    ):
        """
        *Build the ascii table data from a reduced 1D fits spectrum*

        **Key Arguments:**
            - ``log`` -- logger
            - ``pathToFitsFile`` -- path to the final NTT Pipeline reduced spectrum.
            - ``fluxScalingFactor`` -- manually measured scaling factor for the spectrum (from photometry)

        **Return:**
            - ``pathToOutputFile`` -- path to the output ascii file
        """
        ################ > IMPORTS ################
        ## STANDARD LIB ##
        ## THIRD PARTY ##
        import numpy as np
        import pyfits as pf
        ## LOCAL APPLICATION ##

        ################ > VARIABLE SETTINGS ######

        ################ >ACTION(S) ################
        # OPEN THE FILE
        print pathToFitsFile
        hduList = pf.open(pathToFitsFile)
        # READ IN THE SCIENCE DATA AND PRIMARY HEADER
        fluxData = hduList[0].data[0]
        # uwFluxData = hduList[0].data[1]
        backgroundData = hduList[0].data[2]
        sigmaData = hduList[0].data[3]
        primHeader = hduList[0].header
        log.debug('counting the pixels in file pathToFitsFile: %s' %
                  (pathToFitsFile,))
        pixelCount = len(fluxData[0])
        log.debug('pixelCount %s' % (pixelCount,))

        # DETERMINE IF SOFI OR EFOSC
        voUCD = 'em.IR'
        try:
            instr = primCardList['HIERARCH ESO INS GRIS1 NAME'].key
            voUCD = 'em.opt'
        except:
            pass

        log.debug('fluxData %s' % (len(fluxData[0]),))
        # log.debug('uwFluxData %s' % (len(uwFluxData[0]),))
        log.debug('backgroundData %s' % (len(backgroundData[0]),))
        log.debug('sigmaData %s' % (len(sigmaData[0]),))

        ########## BUILD THE PRIMARY HEADER FOR BINTABLE ##########
        # READ THE NEEDED KEYWORDS & VALUES
        primCardList = primHeader.cards
        # DETERMINE PIXEL WAVELENTH RESOLUTION
        minWave = primCardList['WAVELMIN'].value * 10.
        maxWave = primCardList['WAVELMAX'].value * 10.
        rangeWave = maxWave - minWave
        pixelGaps = len(fluxData[0]) - 1
        delPixel = rangeWave / pixelGaps
        fluxError = primCardList['SPEC_ERR'].value

        wlArray = []
        for item in range(len(fluxData[0])):
            wlArray.append(item * delPixel + minWave)

        log.debug('format %s' % (format,))

        # CREATE ASCII FILE
        pathToAsciiFile = pathToFitsFile.replace(".fits", ".dat")
        try:
            log.debug("attempting to open the file %s" % (pathToAsciiFile,))
            writeFile = open(pathToAsciiFile, 'w')
        except IOError, e:
            message = 'could not open the file %s' % (pathToAsciiFile,)
            log.critical(message)
            raise IOError(message)

        for f, w in zip(fluxData[0], wlArray):
            thisWl = str(w).ljust(16)
            thisFlux = str(f).ljust(16)
            writeFile.write("%(thisWl)s  %(thisFlux)s\n" % locals())

        writeFile.close()
        return None

    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
