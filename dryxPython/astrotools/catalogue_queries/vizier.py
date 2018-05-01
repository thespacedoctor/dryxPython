# !/usr/bin/env python
# encoding: utf-8
"""
*Query vizier via URL*

:Author:
    David Young

:Date Created:
    May 19, 2014

.. todo::
    
    @review: when complete pull all general functions and classes into dryxPython

# xdocopt-usage-tempx
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import string
import re
from subprocess import Popen, PIPE, STDOUT
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times
# from ..__init__ import *


def main(arguments=None):
    """
    *The main function used when ``vizier.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    ########## IMPORTS ##########
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    su = tools(
        arguments=arguments,
        docString=__doc__,
        logLevel="DEBUG"
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
        '--- STARTING TO RUN THE vizier.py AT %s' %
        (startTime,))

    # call the worker function
    # x-if-settings-or-database-credientials
    vizier(
        log=log,
        dbConn=dbConn,
    )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info('-- FINISHED ATTEMPT TO RUN THE vizier.py AT %s (RUNTIME: %s) --' %
             (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################
# xt-class-module-worker-tmpx
# xt-class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : May 19, 2014
# CREATED : May 19, 2014
# AUTHOR : DRYX
def vizier(
        log,
        ra,
        dec,
        catalogue,
        radius):
    """
    *vizier*

    **Key Arguments:**
        - ``log`` -- logger,
        - ``ra`` -- 
        - ``dec`` -- 
        - ``catalogue`` -- 
        - ``radius`` -- 

    **Return:**
        - None

    .. todo::

        - @review: when complete, clean vizier function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log.debug('starting the ``vizier`` function')

    cat = {
        'usnoa2': ['I/252/out', 'USNO-A2.0', 'Rmag'],
        '2mass': ['II/246/out', '2MASS', 'Jmag'],
        'usnob1': ['I/284/out', 'USNO-B1.0', 'R2mag']
    }

    catalogueId = cat[catalogue][0]
    catalogueName = cat[catalogue][1]
    catalogueMag = cat[catalogue][2]

    moduleDirectory = os.path.dirname(__file__)
    resources = moduleDirectory + "/resources"
    vizquery = "%(resources)s/vizquery" % locals()

    vizquery = """%(vizquery)s -mime=tsv  -site=vizier.u-strasbg.fr -source=%(catalogueId)s -c.ra=%(ra)s -c.dec=%(dec)s -c.eq=J2000 -c.rm=%(radius)s -c.geom=b -oc.form=h -sort=_RA*-c.eq -out.add=_RAJ2000,_DEJ2000 -out.max=10000 -out=%(catalogueName)s  -out=%(catalogueMag)s""" % locals()
    print vizquery
    cmd = """%(vizquery)s""" % locals()
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    output = output.split('\n')
    matches = []
    for i in output:
        if i and i[0] != '#':
            matches.append(i)
    ra, dec, objectName, mag = [], [], [], []
    for row in matches[3:]:
        output = row.split('\t')
        ra.append(re.sub(' ', ':', output[0]))
        dec.append(re.sub(' ', ':', output[1]))
        objectName.append(output[2].strip())
        try:
            mag.append(float(output[3]))
        except:
            mag.append(float(9999))

    log.debug('completed the ``vizier`` function')
    return {'ra': ra, 'dec': dec, 'id': objectName, 'mag': mag}

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
