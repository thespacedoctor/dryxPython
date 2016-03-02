#!/usr/bin/env python
# encoding: utf-8
"""
astrometry_corrector.py
=======================
:Summary:
    Correct the astrometry/WCS keywords in the headers of FITS images

:Author:
    aldcroft @ http://www.astropython.org/snippet/2011/1/Fix-the-WCS-for-a-FITS-image-file (adapted by David Young)

:Date Created:
    May 15, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: davidrobertyoung@gmail.com

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython

Usage:
    astromCorrector create -p <parameterFilename>
    astromCorrector -p <parameterFilename> -f <fitsFile>
    astromCorrector -p <parameterFilename> -f <fitsFile> -n <hduNumber>

    -h, --help    show this help message
    -v, --version show version
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import shutil
import string
import numpy as np
import pywcs
import pyfits
# import scipy.optimize
import yaml

# import sherpa.astro.ui as ui
from numpy import sin, cos, radians
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times
import ra_sexegesimal_to_decimal
import declination_sexegesimal_to_decimal


def main(arguments=None):
    """
    The main function used when ``astrometry_corrector.py`` is run as a single script from the cl, or when installed as a cl command
    """
    ########## IMPORTS ##########
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    su = tools(
        arguments=arguments,
        docString=__doc__,
        logLevel="INFO"
    )
    arguments, settings, log, dbConn = su.setup()

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
        '--- STARTING TO RUN THE astrometry_corrector.py AT %s' %
        (startTime,))

    if parameterFilename and pFlag and create:
        create_parameter_file(
            log=log,
            parameterFilename=parameterFilename,
        )

    if not create and pFlag and fFlag and not nFlag:
        astrometry_corrector_from_yaml(
            log=log,
            fitsFile=fitsFile,
            yamlFile=parameterFilename
        )

    if not create and pFlag and fFlag and nFlag:
        astrometry_corrector_from_yaml(
            log=log,
            fitsFile=fitsFile,
            yamlFile=parameterFilename,
            hdu=hduNumber
        )

    # call the worker function
    # x-if-settings-or-database-credientials
    # astrometry_corrector(
    #     log=log,
    # )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE astrometry_corrector.py AT %s (RUNTIME: %s) --' %
        (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################
# xt-class-module-worker-tmpx


class WcsModel(object):

    """
    Modal the WCS for a FITS image

    **Key Arguments:**
        - ``log`` -- logger
        - ``wcs`` -- Image WCS transformation object
        - ``sky`` -- Reference (correct) source positions in RA, Dec
        - ``pix0`` -- Source pixel positions

    **Todo**
        - @review: when complete, clean WcsModel class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation

    def __init__(
            self,
            log,
            wcs,
            sky,
            pix0
    ):
        self.log = log
        self.wcs = wcs
        self.sky = sky
        self.pix0 = pix0.flatten()
        # Copy the original WCS CRVAL and CD values
        self.crval = wcs.wcs.crval.copy()
        if hasattr(wcs.wcs, 'cd'):
            self.cd = wcs.wcs.cd.copy()
        else:
            self.cd = wcs.wcs.pc.copy()
        # x-self-arg-tmpx
        return None

    def close(self):
        del self
        return None

    # Variable Data Atrributes

    # Override Variable Data Atrributes

    # Method Attributes
    # x-get-method-tempx
    def calc_pix(
            self,
            pars,
            x=None):
        """For the given d_ra, d_dec, and d_theta pars, update the WCS
 transformation and calculate the new pixel coordinates for each
 reference source position.

        **Key Arguments:**
            - ``pars`` -- d_ra, d_dec, and d_theta pars
            - ``x`` -- Sherpa passes an extra "X" argument, which in this case we always ignore.

        **Return:**
            - ``pix.flatten()`` -- updated pixel positions

        **Todo**
            - @review: when complete, clean calc_pix method
            - @review: when complete add logging
        """
        self.log.info('starting the ``calc_pix`` method')

        # get single parameters
        d_ra, d_dec, d_theta = pars
        self.wcs.wcs.crval = self.crval + np.array([d_ra, d_dec]) / 3600.0

        if hasattr(self.wcs.wcs, 'cd'):
            self.wcs.wcs.cd = np.dot(rotate(self.log, d_theta), self.cd)
        else:
            self.wcs.wcs.pc = np.dot(rotate(self.log, d_theta), self.cd)

        pix = self.wcs.wcs_sky2pix(self.sky, 1)

        varToPrint = pix.flatten()
        self.log.debug('pix: %(varToPrint)s' % locals())
        varToPrint = self.pix0.flatten()
        self.log.debug('pix0: %(varToPrint)s' % locals())

        self.log.info('completed the ``calc_pix`` method')

        return pix.flatten()

    # use the tab-trigger below for new method
    def calc_resid2(
            self,
            pars):
        """Return the squared sum of the residual difference between the
 original pixel coordinates and the new pixel coords (given offset
 specified in ``pars``)

 This gets called by the scipy.optimize.fmin function.

        **Key Arguments:**
            - ``pars`` -- d_ra, d_dec, and d_theta pars

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean calc_resid2 method
            - @review: when complete add logging
        """
        self.log.info('starting the ``calc_resid2`` method')

        pix = self.calc_pix(pars)
        resid2 = np.sum((self.pix0 - pix) ** 2)  # assumes uniform errors

        self.log.debug('resid2: %(resid2)s' % locals())

        self.log.info('completed the ``calc_resid2`` method')
        return resid2

    # use the tab-trigger below for new method
    # xt-class-method

    # Override Method Attributes
    # method-override-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : May 15, 2014
# CREATED : May 15, 2014
# AUTHOR : aldcroft @ http://www.astropython.org/snippet/2011/1/Fix-the-WCS-for-a-FITS-image-file -- adapted by DRYX
# LAST MODIFIED : May 15, 2014
# CREATED : May 15, 2014
# AUTHOR : aldcroft @ http://www.astropython.org/snippet/2011/1/Fix-the-WCS-for-a-FITS-image-file -- adapted by DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method
def astrometry_corrector(
        log,
        infile,
        outfile,
        sky_ref,
        sky_img,
        opt_alg='scipy',
        hdu=1):
    """Adjust the WCS transform in FITS file ``infile`` so that the sources
 positions given in ``sky_img`` most closely match the "correct" values in
 ``sky_ref``. The FITS image is assumed to be in the given ``hdu`` number
 (default=1). The updated image (along with any other HDUs) are written out
 to ``outfile``. The optimization algorithm can be "scipy"
 (scipy.optimize.fmin) or "sherpa".

    **Key Arguments:**
        - ``log`` -- logger
        - ``infile`` -- infile
        - ``outfile`` -- outfile
        - ``sky_ref`` -- positions of the reference sources
        - ``sky_img`` -- positions in the sky image to be corrected
        - ``opt_alg`` -- "scipy" | "sherpa"
        - ``hdu`` -- hdu number to be corrected


    **Return:**
        - None

    **Todo**
        - @review: when complete, clean astrometry_corrector function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``astrometry_corrector`` function')

    img_hdu, hdulist, wcs_img = read_fits(log, infile, hdu)
    new_wcs = match_wcs(log, wcs_img, sky_img, sky_ref, opt_alg)
    update_header_wcs(log, img_hdu, new_wcs)
    write_fits(log, hdulist, outfile)

    log.info('completed the ``astrometry_corrector`` function')
    return None

# LAST MODIFIED : May 15, 2014
# CREATED : May 15, 2014
# AUTHOR : aldcroft @
# http://www.astropython.org/snippet/2011/1/Fix-the-WCS-for-a-FITS-image-file
# -- adapted by DRYX


def match_wcs(
        log,
        wcs_img,
        sky_img,
        sky_ref,
        opt_alg='scipy'):
    """Adjust ``wcs_img`` (CRVAL{1,2} and CD{1,2}_{1,2}) using a rotation and linear
 offset so that ``coords_img`` matches ``coords_ref``

    **Key Arguments:**
        - ``sky_img`` -- list of (world_x, world_y) [aka RA, Dec] coords in input image
        - ``sky_ref`` -- list of reference (world_x, world_y) coords to match
        - ``wcs_img`` -- pywcs WCS object for input image

    **Return:**
        -  ``d_ra``, ``d_dec``, ``d_theta``  (``wcsmodel.wcs``)

    **Todo**
        - @review: when complete, clean match_wcs function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``match_wcs`` function')

    pix_img = wcs_img.wcs_sky2pix(sky_img, 1)
    wcsmodel = WcsModel(log, wcs_img, sky_ref, pix_img)
    y = np.array(pix_img).flatten()

    if opt_alg == 'sherpa':
        x = np.arange(len(y))
        ui.load_user_model(wcsmodel.calc_pix, 'wcsmod')
        ui.add_user_pars('wcsmod', ['d_ra', 'd_dec', 'd_theta'])
        wcsmod.d_ra = 0.0
        wcsmod.d_dec = 0.0
        wcsmod.d_theta = 0.0
        ui.load_arrays(1, x, y, np.ones(len(y)))
        ui.set_model(1, wcsmod)
        ui.set_method('simplex')
        ui.fit()
    else:
        x0 = np.array([0.0, 0.0, 0.0])
        d_ra, d_dec, d_theta = scipy.optimize.fmin(wcsmodel.calc_resid2, x0)
        print 'Scipy fit values:', d_ra, d_dec, d_theta

    log.info('completed the ``match_wcs`` function')
    return wcsmodel.wcs


# use the tab-trigger below for new function
# LAST MODIFIED : May 15, 2014
# CREATED : May 15, 2014
# AUTHOR : aldcroft @
# http://www.astropython.org/snippet/2011/1/Fix-the-WCS-for-a-FITS-image-file
# -- adapted by DRYX
def rotate(
        log,
        degs):
    """Return a rotation matrix for counterclockwise rotation by ``deg`` degrees.

    **Key Arguments:**
        - ``log`` -- logger
        - ``deg`` -- rotation amount

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean rotate function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``rotate`` function')

    rads = radians(degs)
    s = sin(rads)
    c = cos(rads)

    log.info('completed the ``rotate`` function')
    return np.array([[c, -s], [s, c]])

# use the tab-trigger below for new function
# LAST MODIFIED : May 15, 2014
# CREATED : May 15, 2014
# AUTHOR : aldcroft @
# http://www.astropython.org/snippet/2011/1/Fix-the-WCS-for-a-FITS-image-file
# -- adapted by DRYX


def read_fits(
        log,
        name,
        hdu):
    """Read FITS file ``name`` with an image in specified ``hdu`` number.
 Return the image HDU, list of all HDUs and the WCS object associated
 with the image HDU.

    **Key Arguments:**
        - ``log`` -- logger
        - ``name`` -- filename
        - ``hdu`` -- hdu number to read

    **Return:**
        - ``img_hdu``, ``hdulist``, ``wcs``

    **Todo**
        - @review: when complete, clean read_fits function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``read_fits`` function')

    hdulist = pyfits.open(name)
    img_hdu = hdulist[hdu]
    wcs = pywcs.WCS(img_hdu.header)

    # Print out all of the settings that were parsed from the header
    # thisString = wcs.wcs.print_contents()
    # log.info('original wcs: %(thisString)s' % locals())

    log.info('completed the ``read_fits`` function')
    return img_hdu, hdulist, wcs

# use the tab-trigger below for new function
# LAST MODIFIED : ggs
# CREATED : ggs
# AUTHOR : aldcroft @ http://www.astropython.org/snippet/2011/1/Fix-the-WCS-for-a-FITS-image-file -- adapted by DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method


def write_fits(
        log,
        hdulist,
        name,
        clobber=True,
        checksum=True):
    """Write the ``hdulist`` to a FITS file with name ``name``.

    **Key Arguments:**
        - ``log`` -- logger
        - ``hdulist `` -- hdus to write
        - ``name`` -- path to the file to write

    **Return:**
        - None

    **Todo**
        - @review: when complete,
        clean write_fits function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``write_fits`` function')

    hdulist.writeto(name, clobber=clobber, checksum=checksum)

    log.info('completed the ``write_fits`` function')
    return None

# use the tab-trigger below for new function
# LAST MODIFIED : May 15, 2014
# CREATED : May 15, 2014
# AUTHOR : aldcroft @ http://www.astropython.org/snippet/2011/1/Fix-the-WCS-for-a-FITS-image-file -- adapted by DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method


def update_header_wcs(
        log,
        hdu,
        wcs):
    """Update the WCS CRVAL and CD values in the header for the given ``hdu``
 using the supplied ``wcs`` WCS object. This assumes that the CD values
 are being used instead of the PC values (as is the case for an HST
 Multidrizzle output). 

    **Key Arguments:**
        - ``log`` -- logger
        - ``hdu`` -- the hdu to update
        - ``wcs`` -- wcs keywords

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean update_header_wcs function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``update_header_wcs`` function')
    hdr = hdu.header
    hdr['CRVAL1'] = wcs.wcs.crval[0]
    hdr['CRVAL2'] = wcs.wcs.crval[1]
    if hasattr(wcs.wcs, 'cd'):
        hdr['CD1_1'] = wcs.wcs.cd[0, 0]
        hdr['CD1_2'] = wcs.wcs.cd[0, 1]
        hdr['CD2_1'] = wcs.wcs.cd[1, 0]
        hdr['CD2_2'] = wcs.wcs.cd[1, 1]
    if hasattr(wcs.wcs, 'pc'):
        hdr['PC1_1'] = wcs.wcs.pc[0, 0]
        hdr['PC1_2'] = wcs.wcs.pc[0, 1]
        hdr['PC2_1'] = wcs.wcs.pc[1, 0]
        hdr['PC2_2'] = wcs.wcs.pc[1, 1]

    log.info('completed the ``update_header_wcs`` function')
    return None

# use the tab-trigger below for new function
# LAST MODIFIED : May 15, 2014
# CREATED : May 15, 2014
# AUTHOR : DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method


def create_parameter_file(
        log,
        parameterFilename):
    """create the yaml parameter file template

    **Key Arguments:**
        - ``log`` -- logger

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean create_parameter_file function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``create_parameter_file`` function')

    pwd = os.getcwd()
    parameterFilename = os.path.splitext(parameterFilename)[0]
    parameterFilename = """%(pwd)s/%(parameterFilename)s.yaml""" % locals()
    moduleDirectory = os.path.dirname(__file__)
    src = """%(moduleDirectory)s/resources/astrometry_corrector_tmpx.yaml""" % locals()
    shutil.copyfile(src, parameterFilename)

    log.info('completed the ``create_parameter_file`` function')
    return None

# use the tab-trigger below for new function
# LAST MODIFIED : May 16, 2014
# CREATED : May 16, 2014
# AUTHOR : DRYX
# copy usage method(s) into function below and select the following snippet from the command palette:
# x-setup-worker-function-parameters-from-usage-method


def astrometry_corrector_from_yaml(
        log,
        fitsFile,
        yamlFile,
        hdu=1):
    """astrometry corrector using parameters taken from a yaml file

    **Key Arguments:**
        - ``log`` -- logger,
        - ``fitsFile`` -- fits filename/path
        - ``yamlFile`` -- yaml filename/path

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean astrometry_corrector_from_yaml function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``astrometry_corrector_from_yaml`` function')

    pwd = os.getcwd()
    yamlFile = pwd + "/%(yamlFile)s" % locals()

    dcu.dryx_mkdir(
        log=log,
        directoryPath="%(pwd)s/corrected_fits/" % locals()
    )
    dcu.dryx_mkdir(
        log=log,
        directoryPath="%(pwd)s/original_fits/" % locals()
    )
    outfile = "%(pwd)s/corrected_fits/%(fitsFile)s" % locals()
    fitsFile = pwd + "/%(fitsFile)s" % locals()

    stream = file(yamlFile, 'r')
    yamlContent = yaml.load(stream)
    sky_ref = []
    sky_img = []

    for k, v in yamlContent.iteritems():
        if "version" not in k:
            for subk, subv in v.iteritems():

                theseLines = string.split(subv, ',')
                for i, line in enumerate(theseLines):
                    print i, line
                    line = line.strip()
                    if i == 0:
                        if ":" in line:
                            ra = ra_sexegesimal_to_decimal.ra_sexegesimal_to_decimal(
                                ra=line)
                        else:
                            ra = float(line)

                    if i == 1:
                        if ":" in line:
                            dec = declination_sexegesimal_to_decimal.declination_sexegesimal_to_decimal(
                                dec=line)
                        else:
                            dec = float(line)

                if "reference" in subk:
                    sky_ref.append((ra, dec))
                else:
                    sky_img.append((ra, dec))

    print sky_ref, sky_img

    stream.close()

    astrometry_corrector(
        log=log,
        infile=fitsFile,
        outfile=outfile,
        sky_ref=sky_ref,
        sky_img=sky_img,
        opt_alg='scipy',
        hdu=int(hdu)
    )

    source = fitsFile
    basename = os.path.basename(fitsFile)
    destination = "%(pwd)s/original_fits/%(basename)s" % locals()
    os.rename(source, destination)

    source = yamlFile
    basename = os.path.basename(yamlFile)
    destination = "%(pwd)s/original_fits/%(basename)s" % locals()
    os.rename(source, destination)

    log.info('completed the ``astrometry_corrector_from_yaml`` function')
    return None

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
