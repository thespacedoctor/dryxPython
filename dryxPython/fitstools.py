#!/usr/local/bin/python
# encoding: utf-8
"""
fitstools
===============
:Summary:
    Some helpful tools to work with FITS files

:Author:
    David Young

:Date Created:
    March 19, 2013

:dryx syntax:
    - ``xxx`` = come back here and do some more work
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script please email me: d.r.young@qub.ac.uk
"""
################# GLOBAL IMPORTS ####################
import sys
import os

######################################################
# MAIN LOOP - USED FOR DEBUGGING OR WHEN SCRIPTING   #
######################################################


def main():
    """Used for debugging

    Key Arguments:
        -
        - dbConn -- mysql database connection
        - log -- logger

    Return:
        - None
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import pesstoMarshallPythonPath as pp
    pp.set_python_path()
    import pmCommonUtils as p
    import dryxPython.commonutils as cu

    ################ > SETUP ##################
    ## SETUP DB CONNECTION AND A LOGGER
    dbConn, log = p.settings()
    ## START LOGGING ##
    startTime = cu.get_now_sql_datetime()
    log.info('--- STARTING TO RUN THE fitstools AT %s' % (startTime,))

    ################ > VARIABLE SETTINGS ######
    ################ >ACTION(S) ###############

    dbConn.commit()
    dbConn.close()
    ## FINISH LOGGING ##
    endTime = cu.get_now_sql_datetime()
    runningTime = cu.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE fitstools AT %s (RUNTIME: %s) --' %
             (endTime, runningTime,))
    return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
## LAST MODIFIED : March 19, 2013
## CREATED : March 19, 2013
## AUTHOR : DRYX
def convert_fits_header_to_dictionary(
        log,
        pathToFitsFile,
        headerExtension=0):
    """Convert a FITS file header keywords / values into a python dictionary

    **Key Arguments:**
        - ``log`` -- logger
        - ``pathToFitsFile`` -- path to the fits file
        - ``headerExtension`` -- the header extension to look in

    **Return:**
        - ``headerDictionary`` -- the header converted to a dictionary suitable for mysql ingest
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ################ > VARIABLE SETTINGS ######
    ################ >ACTION(S) ################
    log.info('starting the ``convert_fits_header_to_dictionary`` function')
    if not isinstance(pathToFitsFile, str):
        raise TypeError("pathToFitsFile argument needs to be a string")

    try:
        with open(pathToFitsFile):
            pass
            fileExists = True
    except IOError:
       fileExists = False
       raise IOError("the fits file %s does not exist" % (pathToFitsFile,))

    headerDictionary = {}
    try:
        fitsHeader = get_fits_header(log, pathToFitsFile, headerExtension=headerExtension)
        cardList = fitsHeader.ascardlist()
        print cardList
    except:
        headerDictionary["corrupted"] = [True, "file is corrupted"]
        return headerDictionary

    for cl in cardList:
        if len(cl.key) > 0:
            # log.debug('cl: %s' % (cl,))
            headerDictionary[cl.key] = [cl.value, cl.comment]

    log.info('finished the ``convert_fits_header_to_dictionary`` function')

    return headerDictionary

## LAST MODIFIED : March 19, 2013
## CREATED : March 19, 2013
## AUTHOR : DRYX
def get_fits_header(
        log,
        pathToFits,
        headerExtension=0):
    """Return the HDU for the given fits file

    **Key Arguments:**
        - ``log`` -- logger
        - ``pathToFits`` -- the absolute path to the fits file
        - ``headerExtension`` -- the header extension to look in

    **Return:**
        - ``hdu`` -- the FITS header requested
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    import pyfits as pf
    ## LOCAL APPLICATION ##

    ################ > VARIABLE SETTINGS ######

    ################ >ACTION(S) ################
    try:
        hdu = pf.getheader(pathToFits, headerExtension)
    # FIX THE CARDS (SHOULD BE NO LONGER THAN 80 CHARACTERS)
    except:
        try:
            _correct_extended_fits_keywords(pathToFits)
        except:
            sys.exit('image ' + str(
                pathToFits) + ' is corrupted, delete it and start again')
            hdu = pf.getheader(pathToFits, headerExtension)

    return hdu

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################
## LAST MODIFIED : March 19, 2013
## CREATED : March 19, 2013
## AUTHOR : Stefano Valenti & DRYX


def _correct_extended_fits_keywords(log, pathToFits):
    """Values within the fits header should be no longer than 80 characters

    **Key Arguments:**
        - ``log`` -- logger
        - ``pathToFits`` -- path the the FITS file

    **Return:**
        - None
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import re
    ## THIRD PARTY ##
    from pyfits import open as popen
    from numpy import asarray
    ## LOCAL APPLICATION ##

    ################ > VARIABLE SETTINGS ######

    ################ >ACTION(S) ################
    hdulist = popen(pathToFits)
    a = hdulist[0]._verify('fix')
    _header = hdulist[0].header
    for i in range(len(a)):
        if not a[i]:
            a[i] = ['']
    ww = asarray([i for i in range(len(a)) if (re.sub(' ', '', a[i][0]) != '')])
    if len(ww) > 0:
        newheader = []
        headername = []
        for j in _header.items():
            headername.append(j[0])
            newheader.append(j[1])
        hdulist.close()
        imm = popen(pathToFits, mode='update')
        _header = imm[0].header
        for i in ww:
            if headername[i]:
                try:
                    _header.update(headername[i], newheader[i])
                except:
                    _header.update(headername[i], 'xxxx')
        imm.flush()
        imm.close()

    return


## LAST MODIFIED : May 28, 2013
## CREATED : May 28, 2013
## AUTHOR : DRYX

def remove_keyword_from_file(
        log,
        pathToFitsFile,
        keyword):
    """Remove a given keyword card from a fits file

    **Return:**
        - None
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    import pyfits as pf
    ## LOCAL APPLICATION ##

    ################ >ACTION(S) ################
    hduList = pf.open(pathToFitsFile)
    fitsData = hduList[0].data
    primHeader = hduList[0].header
    hduList.close()
    os.remove(pathToFitsFile)
    primCardList = primHeader.ascardlist()

    thisCardList = []
    for key in primCardList.keys():
        if key != keyword:
            thisCardList.append(primCardList[key])

    primHeader = pf.Header(cards=thisCardList)
    primHdu = pf.PrimaryHDU(header=primHeader, data=fitsData)
    thisHduList = pf.HDUList([primHdu,])

    thisHduList.writeto(pathToFitsFile, checksum=True)

    log.debug('primHeader %s' % (primHeader,))

    return


## LAST MODIFIED : May 28, 2013
## CREATED : May 28, 2013
## AUTHOR : DRYX

def add_or_replace_keyword_to_fits(
        log,
        pathToFitsFile,
        keywordName,
        keywordValue,
        keywordComment):
    """Add or replace a given keyword card from a fits file

    **Return:**
        - None
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    import pyfits as pf
    ## LOCAL APPLICATION ##

    ################ >ACTION(S) ################
    hduList = pf.open(pathToFitsFile)
    fitsData = hduList[0].data
    primHeader = hduList[0].header
    hduList.close()
    os.remove(pathToFitsFile)
    primCardList = primHeader.ascardlist()

    if keywordName in primCardList.keys():
        primCardList[keywordName].comment = keywordComment
        primCardList[keywordName].value = keywordValue
    else:
        card = pf.Card(keywordName, keywordValue, keywordComment)
        primCardList.append(card)

    primHeader = pf.Header(cards=primCardList)
    primHdu = pf.PrimaryHDU(header=primHeader, data=fitsData)
    thisHduList = pf.HDUList([primHdu,])

    thisHduList.writeto(pathToFitsFile, checksum=True)

    log.debug('primHeader %s' % (primHeader,))

    return


if __name__ == '__main__':
    main()


###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
