#!/usr/local/bin/python
# encoding: utf-8
"""
download_google_sheet.py
========================
:Summary:
    Download a google spreadsheet as csv

:Author:
    David Young

:Date Created:
    October 13, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from datetime import datetime, date, time
import gdata.docs.service
import gdata.spreadsheet.service
from dryxPython.projectsetup import setup_main_clutil


def download_google_sheet(
    log,
    email,
    password,
    gdoc_id
):
    """download google sheet

    **Key Arguments:**
        - ``log`` -- logger
        - ``email`` -- google email
        - ``password`` -- google password
        - ``gdoc_id`` -- the ID of the google spreadsheet (e.g. `1A9NOjQTS4nSt_KSb0YUTlQ0utTARjcGT5UWbsADcY1M#gid=0`)

    **Return:**
        - ``downloadFilepath`` -- the path the the downloaded CSV file
    """
    log.info('starting the ``download_google_sheet`` function')

    log.debug(
        """Attempting to downloading the CSV file with id %(gdoc_id)s""" % locals())

    # google drive client
    gd_client = gdata.docs.service.DocsService()

    # auth using ClientLogin
    gs_client = gdata.spreadsheet.service.SpreadsheetsService()
    gs_client.ClientLogin(email, password)

    # getting the key(resource id and tab id from the ID)
    resource = gdoc_id.split('#')[0]
    tab = gdoc_id.split('#')[1].split('=')[1]
    resource_id = 'spreadsheet:' + resource

    now = datetime.now()
    now = now.strftime("%Y%m%dt%H%M%S")
    downloadFilepath = "/tmp/%(gdoc_id)s_%(now)s.csv" % locals()

    log.debug('Downloading spreadsheet to %(downloadFilepath)s' % locals())

    docs_token = gd_client.GetClientLoginToken()
    gd_client.SetClientLoginToken(gs_client.GetClientLoginToken())
    gd_client.Export(resource_id, downloadFilepath, gid=tab)
    gd_client.SetClientLoginToken(docs_token)

    log.info('completed the ``download_google_sheet`` function')
    return downloadFilepath
