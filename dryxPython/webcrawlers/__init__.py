#!/usr/local/bin/python
# encoding: utf-8
"""
**webcrawlers**

Created by David Young on October 25, 2012
If you have any questions requiring this script please email me: davidrobertyoung@gmail.com

dryx syntax:
p<Var> = variable formated in the way I want it output to file or screen
xxx = come back here and do some more work

"""


############################################
# MAIN LOOP - USED FOR DEBUGGING           #
############################################
def main():
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import pmCommonUtils as p

    ################ > SETUP ##################
    # SETUP DB CONNECTION AND A LOGGER
    dbConn, log = p.settings()
    ## START LOGGING ##
    log.info('----- STARTING TO RUN THE modulename -----')

    ################ > VARIABLE SETTINGS ######
    ################ >ACTION(S) ###############
    password_protected_page_downloader(dbConn, log)

    dbConn.commit()
    dbConn.close()
    ## FINISH LOGGING ##
    log.info('----- FINISHED ATTEMPT TO RUN THE modulename -----')

    # atelDownloader(4000,4567,'/Users/Dave/Dropbox/projects/WORK/html_to_mysql_db_parsers/atel_pages')
    # singleWebDocumentDownloader('http://docs.python.org/_static/py.png','/Users/Dave/Desktop',1)
    #_fetch('http://docs.python.org/_static/py.png')

    #urlList = ['http://www.pessto.org/index.html','http://docs.python.org/_static/py.png','http://static.bbci.co.uk/frameworks/barlesque/2.14.4/desktop/3.5/img/blq-blocks_grey_alpha.png','http://www.pessto.org/pessto/assets/images/home_button_body.png','http://www.pessto.org/pessto/assets/images/news_button_selected.png']
    # multiWebDocumentDownloader(urlList,'/Users/Dave/Desktop',1)

########################################################################
#  HELPER FUNCTION FOR DOC DOWNLOADERS                                 #
########################################################################
# LAST MODIFIED : 20121025
# CREATED : 20121025


def _fetch(url,):
    import logging as log
    import socket
    from eventlet import Timeout
    from eventlet.green import urllib2
    import sys

    tries = 10
    count = 1
    downloaded = False
    while count < tries and downloaded == False:
        try:
            log.debug('downloading ' + url.get_full_url())
            body = urllib2.urlopen(url).read()
            downloaded = True
        except socket.timeout, e:
            print "timeout on URL, trying again"
            count += 1
        except Exception, e:
            if "[Errno 60]" in str(e):
                print "timeout on URL, trying again"
                count += 1
            if "Error 502" in str(e):
                print "proxy error on URL, trying again"
                count += 1
            else:
                log.warning(
                    "could not download " + url.get_full_url() + " : " + str(e) + "\n")
                url = None
                body = None
                downloaded = True

    return url, body

# LAST MODIFIED : December 7, 2012
# CREATED : December 7, 2012
# AUTHOR : DRYX


def _dump_files_to_local_drive(bodies, theseUrls, log):
    """
    *takes the files stored in memory and dumps them to the local drive*

        ****Key Arguments:****
          - ``bodies`` -- array of file data (currently stored in memory)
          - ``theseUrls`` -- array of local files paths to dump the file data into
          - ``log`` -- logger

        **Return:**
          - ``None``
    """
    ################ > IMPORTS ################

    ################ > VARIABLE SETTINGS ######

    ################ >ACTION(S) ################
    j = 0
    log.debug("attempting to write file data to local drive")
    log.debug('%s URLS = %s' % (len(theseUrls), str(theseUrls),))
    for body in bodies:
        try:
            if theseUrls[j]:
                with open(theseUrls[j], 'w') as f:
                    f.write(body)
                f.close()
            j += 1
        except Exception, e:
            log.error(
                "could not write downloaded file to local drive - failed with this error %s: " %
                (str(e),))
            return -1
    return

########################################################################
#  MUTLI-DOC WEB DOWNLOAD                                              #
########################################################################
# LAST MODIFIED : 20121025
# CREATED : 20121025


def multiWebDocumentDownloader(
    urlList,
    downloadDirectory,
    log,
    timeStamp=1,
    timeout=180,
    concurrentDownloads=10,
    resetFilename=False,
    credentials=False,
    longTime=False,
    indexFilenames=False
):
    """
    *get multiple url documents and place in specified download directory*

        ****Key Arguments:****
          - ``urlList`` -- list of document urls
          - ``downloadDirectory`` -- directory(ies) to download the documents to - can be one url or a list of urls the same length as urlList
          - ``resetFilename`` -- a string to reset all filenames to
          - ``credentials`` -- basic http credentials { 'username' : "...", "password", "..." }
          - ``indexFilenames`` -- prepend filenames with index (where url appears in urllist)

        **Return:**
          - list of timestamped documents (same order as the input urlList)
    """
    ## > IMPORTS ##
    import sys
    import os
    import eventlet
    from eventlet.green import urllib2
    import dryxPython.commonutils as dcu
    import socket
    import re
    import base64

    ## >SETTINGS ##
    # timeout in seconds
    timeout = float(timeout)
    socket.setdefaulttimeout(timeout)

    ###########################################################
    # >ACTION(S)                                              #
    ###########################################################
    # BUILD THE 2D ARRAY FOR MULTI_THREADED DOWNLOADS
    thisArray = []
    bodies = []
    localUrls = []
    theseUrls = []
    requestList = []

    totalCount = len(urlList)

    # if only one download direcory
    if isinstance(downloadDirectory, str):
        for i, url in enumerate(urlList):
            # EXTRACT THE FILENAME FROM THE URL
            if resetFilename:
                filename = resetFilename
            else:
                filename = dcu.extract_filename_from_url(log, url)
                if indexFilenames:
                    filename = """%(i)03d_%(filename)s""" % locals()

            if not filename:
                continue

            if(timeStamp):
                # APPEND TIMESTAMP TO THE FILENAME
                filename = dcu.append_now_datestamp_to_filename(
                    log, filename, longTime=longTime)
            # GENERATE THE LOCAL FILE URL
            localFilepath = downloadDirectory + "/" + filename
            thisArray.extend([[url, localFilepath]])

            # GENERATE THE REQUESTS
            request = urllib2.Request(url)
            if credentials != False:
                username = credentials["username"]
                password = credentials["password"]
                base64string = base64.encodestring(
                    '%s:%s' % (username, password)).replace('\n', '')
                request.add_header("Authorization", "Basic %s" % base64string)
            requestList.append(request)

    elif isinstance(downloadDirectory, list):
        for u, d in zip(urlList, downloadDirectory):
            # EXTRACT THE FILENAME FROM THE URL
            if resetFilename:
                filename = resetFilename
            else:
                filename = dcu.extract_filename_from_url(log, url)

            if not filename:
                continue

            if(timeStamp):
                # APPEND TIMESTAMP TO THE FILENAME
                filename = dcu.append_now_datestamp_to_filename(
                    log, filename)
            # GENERATE THE LOCAL FILE URL
            localFilepath = d + "/" + filename
            thisArray.extend([[u, localFilepath]])
            log.debug(" about to download %s" % (u,))

            # GENERATE THE REQUESTS
            request = urllib2.Request(u)
            if credentials != False:
                log.debug('adding the credentials')
                username = credentials["username"]
                password = credentials["password"]
                base64string = base64.encodestring(
                    '%s:%s' % (username, password)).replace('\n', '')
                request.add_header("Authorization", "Basic %s" % base64string)
            requestList.append(request)

    pool = eventlet.GreenPool(concurrentDownloads)
    i = 0
    try:

        log.debug(
            "starting mutli-threaded download batch - %s concurrent downloads" %
            (concurrentDownloads,))
        log.debug('len(requestList): %s' % (len(requestList),))
        for url, body in pool.imap(_fetch, requestList):
            urlNum = i + 1
            if urlNum > 1:
                # Cursor up one line and clear line
                sys.stdout.write("\x1b[1A\x1b[2K")
            percent = (float(urlNum) / float(totalCount)) * 100.
            print "  %(urlNum)s / %(totalCount)s (%(percent)1.1f%%) URLs downloaded" % locals()

            if(body):
                bodies.extend([body])
                theseUrls.extend([thisArray[i][1]])
            else:
                theseUrls.extend([None])
                bodies.extend([None])

            # DUMP THE FILES FROM MEMORY EVERY CONCURRENT DOWNLOAD CYCLE
            if i % concurrentDownloads == 0:
                _dump_files_to_local_drive(bodies, theseUrls, log)
                localUrls.extend(theseUrls)
                # RESET THE TMP ARRAYS
                bodies = []
                theseUrls = []
            i += 1
    except eventlet.Timeout, e:
        log.error(
            "something went wrong with the mutli-threaded download : " + str(e) + "\n")

    # DUMP REMAINING FILES TO THE LOCAL DRIVE
    _dump_files_to_local_drive(bodies, theseUrls, log)
    localUrls.extend(theseUrls)

    return localUrls


########################################################################
#  SINGLE DOC WEB DOWNLOADER                                           #
########################################################################
# LAST MODIFIED : 20121025
# CREATED : 20121025
def singleWebDocumentDownloader(url, downloadDirectory, log, timeStamp, credentials=False, resetFilename=False, timeout=20):
    """
    *get a url document and place in a specified directory*

        ****Key Arguments:****
          - ``url`` -- document url
          - ``downloadDirectory`` -- download directory path
          - ``timeStamp`` -- boolean, add a timestamp the end of the document name

        **Return:**
          - path to the local document
    """
    ## > IMPORTS ##
    import sys
    import logging as log

    log.debug("converting single url to list and downloading")
    urlList = [url]
    localUrlList = multiWebDocumentDownloader(
        urlList=urlList,
        downloadDirectory=downloadDirectory,
        log=log,
        timeStamp=timeStamp,
        credentials=credentials,
        resetFilename=resetFilename,
        timeout=timeout)
    filepath = localUrlList[0]

    #log.debug('>>>>>>>>>>>>>>> the local url is '+ filepath)
    return filepath


# LAST MODIFIED : January 15, 2013
# CREATED : January 15, 2013
# AUTHOR : DRYX
def password_protected_page_downloader(dbConn, log):
    """
    *get a page that is behind HTTPS authentication password protection*

    **Key Arguments:**
      - ``dbConn`` -- mysql database connection
      - ``log`` -- logger
      - ``___`` --

    **Return:**
      - None
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import commands
    import urllib2

    theurl = 'https://groups.google.com/a/pessto.org/group/alerts/manage_members/alerts.csv'
    username = 'david.young'
    password = 'spac3d0ct0r'
    # a great password

    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # this creates a password manager
    passman.add_password(None, theurl, username, password)
    # because we have put None at the start it will always
    # use this username/password combination for  urls
    # for which `theurl` is a super-url

    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    # create the AuthHandler

    opener = urllib2.build_opener(authhandler)

    urllib2.install_opener(opener)
    # All calls to urllib2.urlopen will now use our handler
    # Make sure not to include the protocol in with the URL, or
    # HTTPPasswordMgrWithDefaultRealm will be very confused.
    # You must (of course) use it when fetching the page though.

    pagehandle = urllib2.urlopen(theurl)
    # authentication is now handled automatically for us

    ################ > VARIABLE SETTINGS ######
    # command = 'wget --output-document=- --quiet --http-user=david.young --http-password=spac3d0ct0r https://groups.google.com/a/pessto.org/group/alerts/manage_members/alerts.csv'
    # status, text = commands.getstatusoutput(command)

    # url = "https://david.young:spac3d0ct0r@groups.google.com/a/pessto.org/group/alerts/manage_members/alerts.csv"
    # try:
    #   urllib2.urlopen(urllib2.Request(url))
    # except urllib2.HTTPError, e:
    #   print e.headers
    #   print e.headers.has_key('WWW-Authenticate')

    ################ >ACTION(S) ################
    # log.debug('status %s' % (status,))
    # log.debug('text %s' % (text,))

    return


if __name__ == '__main__':
    main()

import papers
import urlToPdf
import google_drive
from download_flicker_image import download_flicker_image
