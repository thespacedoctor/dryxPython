#!/usr/local/bin/python
# encoding: utf-8
"""
ned.py
======
:Summary:
    Crossmatch NED

:Author:
    David Young

:Date Created:
    October 22, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:

Usage:
    dat_crossmatch_ned <ra> <dec> <arcsec>
    dat_crossmatch_ned -n <ra> <dec> <arcsec>

    -h, --help            show this help message
    -v, --version         show version
    -n, --nearest         nearest object only
    ra                    ra (decimal degrees or sexegesimal)
    dec                   dec (decimal degrees or sexegesimal)
    arcsec                arcsec (conesearch radius)
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import csv
import codecs
import string
import re
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import webcrawlers as dwc
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil


def main(arguments=None):
    """
    The main function used when ``ned.py`` is run as a single script from the cl, or when installed as a cl command
    """
    # setup the command-line util settings
    su = setup_main_clutil(
        arguments=arguments,
        docString=__doc__,
        logLevel="WARNING",
        options_first=True
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
    startTime = dcu.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE ned.py AT %s' %
        (startTime,))

    # call the worker function
    ned(
        log=log,
        ra=ra,
        dec=dec,
        arcsec=arcsec,
        nearest=nearestFlag
    )

    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE ned.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return


def ned(
        log,
        ra,
        dec,
        arcsec,
        nearest=True):
    """ned

    **Key Arguments:**
        - ``log`` -- logger
        - ``ra`` -- ra
        - ``dec`` -- dec
        - ``arcsec`` -- arcsec conesearch radius
        - ``nearest`` -- nearest object only?

    **Return:**
        - ``results`` -- list of dictionaries of the matching galaxies from NED

    **Todo**
        - @review: when complete, clean ned function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``ned`` function')
    from dryxPython import astrotools as dat

    try:
        raDeg = float(ra)
    except:
        raDeg = dat.ra_sexegesimal_to_decimal.ra_sexegesimal_to_decimal(
            ra=raDeg)
    try:
        decDeg = float(dec)
    except:
        decDeg = dat.declination_sexegesimal_to_decimal.declination_sexegesimal_to_decimal(
            dec=dec)

    arcmin = float(arcsec) / 60.

    url = "http://ned.ipac.caltech.edu/cgi-bin/objsearch?search_type=Near+Position+Search&in_csys=Equatorial&in_equinox=J2000.0&lon=%(raDeg)sd&lat=%(decDeg)sd&radius=%(arcmin)s&hconst=73&omegam=0.27&omegav=0.73&corr_z=1&z_constraint=Unconstrained&z_value1=&z_value2=&z_unit=z&ot_include=ANY&in_objtypes1=Galaxies&in_objtypes1=GPairs&in_objtypes1=GTriples&in_objtypes1=GGroups&in_objtypes1=GClusters&in_objtypes1=QSO&in_objtypes1=QSOGroups&in_objtypes1=GravLens&in_objtypes1=AbsLineSys&in_objtypes1=EmissnLine&nmp_op=ANY&out_csys=Equatorial&out_equinox=J2000.0&obj_sort=Distance+to+search+center&of=pre_text&zv_breaker=30000.0&list_limit=5&img_stamp=YES&of=ascii_bar" % locals(
    )

    urlDoc = dwc.singleWebDocumentDownloader(
        url=url,
        downloadDirectory="/tmp",
        log=log,
        timeStamp=1,
        credentials=False
    )

    results = []
    if urlDoc:
        pathToReadFile = urlDoc
        try:
            log.debug("attempting to open the file %s" % (pathToReadFile,))
            readFile = codecs.open(pathToReadFile, encoding='utf-8', mode='rb')
            thisData = readFile.read()
            readFile.close()
        except IOError, e:
            message = 'could not open the file %s' % (pathToReadFile,)
            log.critical(message)
            raise IOError(message)
        readFile.close()

        matchObject = re.search(r"No\.\|Object Name.*?\n(.*)", thisData, re.S)
        if matchObject:
            # Print the header for stdout
            headers = ["objectName", "objectType", "raDeg", "decDeg",
                       "redshift", "redshiftFlag", "arcminSeparation"]
            thisHeader = "| "
            for head in headers:
                thisHeader += str(head).ljust(40, ' ') + " | "
            print thisHeader
            theseLines = string.split(matchObject.group(), '\n')
            csvReader = csv.DictReader(
                theseLines, dialect='excel', delimiter='|', quotechar='"')
            for row in csvReader:
                thisDict = {}
                thisRow = "| "
                thisDict["raDeg"] = row["RA(deg)"].strip()
                thisDict["decDeg"] = row["DEC(deg)"].strip()
                thisDict["redshift"] = row["Redshift"].strip()
                thisDict["redshiftFlag"] = row["Redshift Flag"].strip()
                thisDict["objectName"] = row["Object Name"].strip()
                thisDict["objectType"] = row["Type"].strip()
                thisDict["arcminSeparation"] = row["Distance (arcmin)"].strip()
                results.append(thisDict)
                for head in headers:
                    thisRow += str(thisDict[head]).ljust(40, ' ') + " | "
                print thisRow
                if nearest:
                    break
        else:
            print "NOMATCH"
    else:
        print "NOMATCH"

    log.info('completed the ``ned`` function')
    return results


if __name__ == '__main__':
    main()
