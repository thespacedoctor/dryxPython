#!/usr/local/bin/python
# encoding: utf-8
"""
atelparser
===============
:Summary:
        Download and parse ATel to strip out RA, DEC & Names of objects into a MySQL DB table(s)

:Author:
        David Young

:Date Created:
        February 4, 2013

:dryx syntax:
        - ``xxx`` = come back here and do some more work
        - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
        - If you have any questions requiring this script please email me: d.r.young@qub.ac.uk
"""
################# GLOBAL IMPORTS ####################


######################################################
# MAIN LOOP - USED FOR DEBUGGING OR WHEN SCRIPTING   #
######################################################
def main():
        """Using the PESSTO Marshall database on mac to test & debug this module

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
        import pmCommonUtils as p
        import dryxPython.commonutils as cu

        ################ > SETUP ##################
        ## SETUP DB CONNECTION AND A LOGGER
        dbConn, log = p.settings()
        ## START LOGGING ##
        startTime = cu.get_now_sql_datetime()
        log.info('--- STARTING TO RUN THE atelparser AT %s' % (startTime,))

        ################ > VARIABLE SETTINGS ######
        downloadDirectory = "/tmp"
        dbTableName = "atel_fullcontent"

        ################ >ACTION(S) ###############
        #download_atels(dbConn, log, lowerAtelIndex, upperAtelIndex, downloadDirectory)
        #atels_to_database(dbConn, log, dbTableName, downloadDirectory)
        parse_atels(dbConn, log, "/Users/Dave/Desktop/")

        dbConn.commit()
        dbConn.close()
        ## FINISH LOGGING ##
        endTime = cu.get_now_sql_datetime()
        runningTime = cu.calculate_time_difference(startTime, endTime)
        log.info('-- FINISHED ATTEMPT TO RUN THE atelparser AT %s (RUNTIME: %s) --' % (endTime, runningTime,))
        return

###################################################################
# CLASSES                                                         #
###################################################################

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################


## LAST MODIFIED : 20121026
## CREATED : 20121026
def download_atels(dbConn, log, lowerAtelIndex, upperAtelIndex, downloadDirectory):
    """download all atels within given range of atels

            Key Arguuments:
                - ``lowerAtelIndex`` -- lowest atel number to download
                - ``upperAtelIndex`` -- lowest atel number to download
                - ``downloadDirectory`` -- directory to download ATels to

            Returns
                - None
    """
    ## > IMPORTS ##
    import dryxPython.webcrawlers as wc

    ###########################################################
    # >ACTION(S)                                              #
    ###########################################################
    # CREATE THE LIST OF ATEL URLS
    urlList = []
    baseUrl = 'http://www.astronomerstelegram.org/?read='
    for i in range(lowerAtelIndex, upperAtelIndex):
        urlList.extend([baseUrl + str(i)])

    try:
        log.info("downloading all ATels from %s to %s" % (lowerAtelIndex, upperAtelIndex))
        localUrls = wc.multiWebDocumentDownloader(urlList, downloadDirectory, log, dbConn, 0)
    except Exception, e:
        log.error("could not download atels : " + str(e) + "\n")

    return localUrls


## LAST MODIFIED : 20121107
## CREATED : 20121107
## AUTHOR : DRYX
def atels_to_database(dbConn, log, dbTableName, downloadDirectory):
        """
        Parse ATels into a mysql db. Parser to add ATels into a mysql db - each ATel has 'element' data (top level - title, author ...) and 'item' data (object specific data - ra, dec, mag, name ...).
        The parser will add one row per 'item' (object) into the db table.

        Key Arguments:
            - ``dbConn`` -- database connection
            - ``log`` -- logger
            - ``dbTableName`` -- name of the db table to add ATels to
            - ``downloadDirectory`` -- directory to download the ATel HTML files to

        """
        ################ > IMPORTS ################
        import re
        import sys
        import dryxPython.mysql as m
        from datetime import datetime

        ################ >SETTINGS ################
        # USED FOR DEVELOPMENT
        #sqlQuery = """DELETE FROM atel_fullcontent"""
        #m.execute_mysql_write_query(sqlQuery, dbConn, log)

        uniqueKeyList = ['atelNumber']  # THE UNIQUEKEY LIST FOR THE DATABASE TABLE
        checkRange = 10  # THE NUMBER OF ATELS TO CHECK PAST THE LAST KNOWN ATEL NUMBER

        ################ >ACTION(S) ################
        ## QUERY TO GRAB THE LATEST ATEL NUMBER
        sqlQuery = """SELECT atelNumber
                        FROM %s
                        ORDER BY atelNumber DESC
                        LIMIT 1""" % (dbTableName, )
        try:
            log.debug("attempting to find the last ingested atel number")
            rows = m.execute_mysql_read_query(sqlQuery, dbConn, log)
        except Exception, e:
            log.error("could not find the last ingested atel number - failed with this error: %s " % (str(e),))
            return -1


        ## SET THE RANGE OF FUTURE ATEL NUMBERS TO CHECK (10 IS REASONABLE)
        if len(rows) != 0:
            nextATel = int(rows[0]["atelNumber"]) + 1
        else:
            nextATel = 3900  # ROUGHLY THE START OF THE PESSTO SURVEY
            checkRange = 1000
        nextFewAtels = nextATel + checkRange

        ## DOWNLOAD THE NEXT FEW ATEL HTML FILES
        try:
            log.debug("attempting to download the html files of the next %s atels" % (checkRange,))
            localUrls = download_atels(dbConn, log, nextATel, nextFewAtels, downloadDirectory)
        except Exception, e:
            log.error("could not download the html files of the next %s atels - failed with this error: %s " % (checkRange, str(e),))
            return -1

        ## LOOP THROUGH THE FILES AND ADD THE VARIOUS HTML ELEMENTS AND TAGS TO MARSHALL DB

        for url in localUrls:
            rf = open(url, 'r')
            html = rf.read()
            elementDict = {}

            # ATEL TITLE
            reTitle = re.compile(r'<TITLE>.*?#\d{1,4}:\s?(.*?)\s?<\/TITLE>', re.M | re.I)
            try:
                title = reTitle.search(html).group(1)
            except:
                return  # QUIT WHENEVER A TITLE IS NOT FOUND IN THE HTML DOC (i.e. ATEL DOES NOT EXIST YET)
                title = None
            elementDict['title'] = title

            #ATEL NUMBER
            reAtelNumber = re.compile(r'<P ALIGN=CENTER>\s?ATel\s?#(\d{1,4})', re.M | re.I)
            try:
                atelNumber = reAtelNumber.search(html).group(1)
            except:
                atelNumber = None
            #print atelNumber
            elementDict['atelNumber'] = atelNumber

            # ATEL AUTHORS
            reWho = re.compile(r'<A HREF=\"mailto:([\w.\-@]*)\">(.*?)<', re.M | re.I)
            try:
                email = reWho.search(html).group(1)
                authors = reWho.search(html).group(2)
            except:
                email = None
                authors = None
            elementDict['email'] = email
            elementDict['authors'] = authors

            # ATEL DATETIME
            redateTime = re.compile(r'<STRONG>(\d{1,2}\s\w{1,10}\s\d{4});\s(\d{1,2}:\d{2})\sUT</STRONG>', re.M | re.I)
            try:
                date = redateTime.search(html).group(1)
                time = redateTime.search(html).group(2)

            except:
                date = None
                time = None

            datePublished = date + " " + time
            datePublished = datetime.strptime(datePublished, '%d %b %Y %H:%M')
            #print "datePublished = %s" % (datePublished,)
            elementDict['datePublished'] = datePublished

            # ATEL
            reTags = re.compile(r'<p class="subjects">Subjects: (.*?)</p>', re.M | re.I)
            try:
                tags = reTags.search(html).group(1)
            except:
                tags = None
            elementDict['tags'] = tags

            # ATEL USER ADDED TEXT
            reUserText = re.compile(r'</div id="subjects">.*?(<div id="references">.*?</div id="references">)?<P>(.*)</P>.*?(<a href="http://twitter.com/share|</TD><TD>)', re.S | re.I)
            try:
                userText = reUserText.search(html).group(2)
            except:
                userText = None
            elementDict['userText'] = userText

            ## FIND REFS IN USER ADDED TEXT
            refList = []
            reOneRef = re.compile(r'http:\/\/www.astronomerstelegram.org\/\?read=(\d{1,4})', re.M | re.I)
            try:
                refIter = reOneRef.finditer(userText)
            except:
                refIter = None
            if refIter:
                for item in refIter:
                    refList.extend([item.group(1)])
            else:
                pass
            refList = set(refList)
            refList = ", ".join(refList)
            elementDict['refList'] = refList

            # ATEL BACK REFERENCES - FIND EXTRA BACK REFS IN REFERENCE DIV
            reBacksRefs = re.compile(r'<div id="references">(.*?)</div id="references">', re.M | re.I)
            try:
                backRefs = reBacksRefs.search(html).group(1)
            except:
                backRefs = None
            backRefList = []
            reOneBackRef = re.compile(r'<A HREF="http:\/\/www.astronomerstelegram.org\/\?read=(\d{1,4})">\1</a>', re.M | re.I)
            try:
                backRefIter = reOneBackRef.finditer(backRefs)
            except:
                backRefIter = None
            if backRefIter:
                for item in backRefIter:
                    #print item.group(1)
                    backRefList.extend([item.group(1)])
            else:
                #print backRefIter
                pass
            ## REMOVE DUPLICATE ATEL NUMBERS FROM LIST
            backRefList = set(backRefList)
            backRefList = ", ".join(backRefList)
            elementDict['backRefList'] = backRefList

            ## ADD THE ATEL TO THE DATABASE
            try:
                log.debug("attempting to convert ATELs to MySQL table")
                m.convert_dictionary_to_mysql_table(dbConn, log, elementDict, dbTableName, uniqueKeyList)
            except Exception, e:
                log.critical("could not convert ATELs to MySQL table - failed with this error: %s " % (str(e),))
                return -1

            rf.close()

        return None


## LAST MODIFIED : February 5, 2013
## CREATED : February 5, 2013
## AUTHOR : DRYX
def parse_atels(dbConn, log, mdFolder):
    """Parse the content of the ATels in the database, appending the various components and values to the db. Also includes the ability convert the atels to markdown, highlighting matches of the parsing regexs.

    **Key Arguments:**
        - ``dbConn`` -- mysql database connection
        - ``log`` -- logger
        - ``mdFolder`` -- where to write the md files to

    **Return:**
        - None
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    import re
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import dryxPython.mysql as m
    import utils as u
    import dryxPython.commonutils as cu
    import dryxPython.astrotools as at

    ################ > VARIABLE SETTINGS ######
    ## METRICS TO FILTER ATELS
    numReferences = 0  # NUMBER OF REFERENCES WITH ATEL
    tags = ""  # ATEL TAGS
    numCoords = 0  # NUMBER OF COORDINATE PAIRS IN ATEL
    numHeaderName = 0  # NUMBER OF NAMES IN HEADER
    numTextName = 0  # NUMBER OF NAMES IN TEXT
    discHead = 0  # DISCOVERY KEYWORD FOUND IN HEADER?
    obsHead = 0  # OBSERVATION KEYWORD FOUND IN HEADER?
    clasHead = 0  # CLASSIFICATION KEYWORD FOUND IN HEADER?
    correctionHead = 0  # CORRECTION KEYWORD FOUND IN HEADER?
    discText = 0  # DISCOVERY KEYWORD FOUND IN TEXT?
    obsText = 0  # OBSERVATION KEYWORD FOUND IN TEXT?
    clasText = 0  # CLASSIFICATION KEYWORD FOUND IN TEXT?
    comment = 0  # COMMENT TAG IN ATEL

    ## SELECT STATEMENT FOR UNPROCESSED ATELS
    sqlQuery = """SELECT *
                    FROM atel_fullcontent
                    WHERE dateParsed is NULL
                    ORDER BY atelNumber"""

    #log.warning('sqlQuery %s' % (sqlQuery,))

    # USED FOR DEVELOPMENT
    # sqlQuery = """SELECT *
    #                 FROM atel_fullcontent
    #                 ORDER BY atelNumber"""

    try:
        log.debug("attempting to select the required atel text")
        rows = m.execute_mysql_read_query(sqlQuery, dbConn, log)
    except Exception, e:
        log.error("could not select the required atel text - failed with this error: %s " % (str(e),))
        return -1

    # USED FOR DEVELOPMENT
    # sqlQuery = """delete from atel_names;
    #                 delete from atel_coordinates;
    #                 ALTER TABLE `pessto_marshall_sandbox`.`atel_coordinates` AUTO_INCREMENT = 1 ;
    #                 ALTER TABLE `pessto_marshall_sandbox`.`atel_names` AUTO_INCREMENT = 1 ;"""
    # m.execute_mysql_write_query(sqlQuery, dbConn, log)

    ## REGEX BUILDS
    start = r"""((R\.?A\.?\b|Coord)[/()\w\d\s,.]{0,9}(\(J2000(\.0)?\)\s?)?(=|:|\s)|\d{4}-\d{2}-\d{2})\s{0,2}[+(]{0,2}"""
    middle = r"""(\sdeg)?(\s?,|:)?\s{0,2}(and\s{1,2}|\(?[\ddeg.':\s]{1,16}\)?(;|,)?\s{0,3})?(Decl?\.?\s*?[()\w\d\s]{0,9}(=|:|\s))?\s?"""
    end = r"""(\sdeg)?"""
    raSex = r"""(?P<raSex>(
                            (?P<raHrs>\d|[0-1]\d|[2][0-3])(:\s?|\s|h\s?)
                            (?P<raMin>[0-5][0-9])(:\s?|\s|m\s?)
                            (?P<raSec>[0-5]\d|\d(?!\d))s?(?P<raSubSec>\.\d{1,})?(\s|\s?s)?
                        )
                )"""
    decSex = r"""(?P<decSex>(
                            (?P<decDeg>(\+|-|–)?[0-8]\d)(:\s?|\s|d\s?|deg\s|o\s?)
                            (?P<decMin>[0-5][0-9])(:\s?|\s|m\s?|'?\s?)
                            (?P<decSec>[0-5]?\d)'?\s?(?P<decSubSec>\.\d{1,3})?'?s?
                        )
                )"""
    raDeg = r"""
                (?P<raDDeg>\d{1,3}(\.\d{1,}))
            """
    decDeg = r"""
                (?P<decDDeg>[\+\-\–]?\d{1,3}(\.\d{1,}))
            """

    nameList = [
                    r"""(PSN|PNV)\s?J\d{8}(\+|-|–)\d{3}(\+|-|–)?\d{3,4}""",
                    r"""(SN|Supernova)\s?(19|20)\d{2}[A-Za-z]{1,2}""",
                    r"""GX\s?\d{3}(\+|-|–)\d""",
                    r"""Fermi\s?J\d{4}(\+|-|–)\d{4}""",
                    r"""PHL\s?\d{3}""",
                    r"""QSO\s?B\d{4}(\+|-|–)\d{3}""",
                    r"""PTF(0|1)\d[a-zA-Z]{1,3}""",
                    r"""MASTER\s?((short\s)?ot\s)?J?\d{6}\.\d{2}(\+|-|–)\d{6}\.\d""",
                    r"""(FSRQ\s?)?PKS\s?\d{4}(\+|-|–)\d{3}""",
                    r"""BZQ\s?J\d{4}(\+|-|–)\d{4}""",
                    r"""(SN(-|–))?LSQ1\d[a-zA-Z]{1,4}""",
                    r"""M31N\s?(19|20)\d{2}(\+|-|–)\d{2}[a-z]""",
                    r"""IGR\s?J?\d{5}(\+|-|–)?\d{1,4}""",
                    r"""GRS\s?\d{4}(\+|-|–)\d{1,4}""",
                    r"""PS1(-|–)?(0|1)\d[a-zA-Z]{1,3}""",
                    r"""SDSS\s(galaxy\s)?J\d{6}\.\d{2}(\+|-|–)\d{6}\.\d""",
                    r"""(CSS|MLS|SSS)\d{6}:\d{6}(\+|-|–)\d{6}""",
                    r"""XMM(U|SL1)\s?J\d{6}\.\d{1}(\+|-|–)\d{6}""",
                    r"""SAX\s?J\d{4}\.\d(\+|-|–)\d{3,4}""",
                    r"""1RXS\s?J\d{6}\.\d(\+|-|–)\d{6}""",
                    r"""USNO(-|–)(B1|A2)\.0\s?(catalogue\s?)\d{4}(-|–)\d{7}""",
                    r"""KS\s?\d{4}(\+|-|–)\d{3}""",
                    r"""AX\s?J\d{4}\.\d(\+|-|–)\d{4}""",
                    r"""2MAS(S|X)\s?J?\d{8}(\+|-|–)\d{7}""",
                    r"""SWIFT\s?J\d{4,6}\.\d(\+|-|–)\d{1,6}""",
                    r"""4U\s?\d{4}(\+|-|–)\d{2,4}""",
                    r"""Hen\s\d{1}(\+|-|–)\d{4}""",
                    r"""(HMXB\s?)?XTE\s?J?\d{4}(\+|-|–)\d{3}""",
                    r"""MAXI\s?J?\d{4}(\+|-|–)\d{3}""",
                    r"""PG\s?J?\d{4}(\+|-|–)\d{3}""",
                    r"""PMN\s?J?\d{4}(\+|-|–)\d{4}""",
                    r"""Guide\sStar\sCatalog\sN4HU\d{6}""",
                    r"""CXOGBS\s?J?\d{6}\.8(\+|-|–)\d{6}""",
                    r"""Galactic\sPlane\s(gamma-ray\s)?Transient\sJ?\d{4}(\+|-|–)\d{4}""",
                    r"""TXS\s\d{4}(\+|-|–)\d{3}""",
                    r"""V\d{4}\sSgr""",
                    r"""Aql\sX(\+|-|–)1""",
                    r"""BLAZAR\s[a-zA-Z\d]{2}\s?\d{3,4}((\+|-|–)\d{2})?""",
                    r"""SNhunt\s\d{1,5}""",
                    r"""Nova\s[a-zA-Z]{3}\s(19|20)\d{2}""",
                    r"""GRB\s?\d{6}[a-zA-Z]{1,2}""",
                    r"""\bV\d{3,4}\s(Sagittarii|cyg)""",
                    r"""SGR\s\d4(\+|-|–)\d{2}""",
                    r"""(QSO|3EG|2FGL)\s?J?\d{4}(\.\d)?(\+|-|–)\d{4}""",
                    r"""BL\sLacertae""",
                    r"""\bCTA\s\d{3}"""
                ]

    ## JOIN ALL THE NAMES INTO ONE STRING
    nameStr = ("|").join(nameList)
    ## REGEX TO SEARCH FOR OBJECT NAMES IN THE ATEL BODIES
    reName = re.compile(r"""(%s)""" % (nameStr,), re.S | re.I)

    ## REGEX TO SEARCH FOR SEXEGESIMAL COORDINATES WITHIN THE BODY TEXT
    reSexeg = r"""
                    %s
                    %s
                    %s
                    %s
                    %s
                """ % (start, raSex, middle, decSex, end)

    reSexeg = re.compile(r"""%s""" % (reSexeg), re.S | re.I | re.X)

    ## REGEX TO SEARCH FOR DECIMAL DEGREES COORDINATES WITHIN THE BODY TEX
    reDegree = r"""
                    %s
                    %s
                    (\sdeg)?(\s?,|:)?\s{0,2}(and\s{1,2}|\(?%s\)?(;|,)?\s{0,3})?(Decl?\.?\s*?[()\w\d\s]{0,9}(=|:|\s))?\s?
                    %s
                    %s""" % (start, raDeg, raSex, decDeg, end,)

    reDegree = re.compile(r"""%s""" % (reDegree,), re.S | re.I | re.X)

    ## REGEX TO SEARCH FOR SEXEG COORDINATES IN TABLES
    reSexTable = r"""
                    %s
                    \s?(\||</td>\s?<td>)?\s?
                    %s
                """ % (raSex, decSex,)

    reSexTable = re.compile(r"""%s""" % (reSexTable, ), re.S | re.I | re.X)

    ## REGEX TO FIND THE SUPERNOVA TYPE
    reSNType = re.compile(r'type\s(I[abcilps]{1,3}n?)|(\bI[abcilnps]{1,3}n?)\s(SN|supernova)|<td>\s?\b(I[abcilps]{1,3}n?)\b\s?<\/td>|(SN\simpostor)|\|\s?\b(I[abcilps]{1,3}n?)\b\s?\||(SN|supernova)\s?(I[abcilps]{1,3}n?)', re.S | re.I)

    ################ >ACTION(S) ################
    #  -- USED FOR DEBUGGING
    filename = mdFolder + "parsed_atels.md"
    #wf = open(filename, 'w')

    ## ITERATE THROUGH THE NEW UNPROCESSED ATELS
    for row in rows:
        atelNumber = row["atelNumber"]
        userText = row["userText"]

        ## SETUP HEADERS FOR MD -- USED FOR DEBUGGING
        header = "\n# %s: %s" % (row["atelNumber"], row["title"],)
        references = "\n### **REFS:** %s" % (row["refList"],)
        numReferences = len(row["refList"])
        tags = "\n### **TAGS:** %s" % (row["tags"],)

        ## REMOVE NIGGLY STRINGS TO MAKE PARSING EASIER
        stringsToRemove = [
                            "<p>",
                            "</p>",
                            "<P>",
                            "</P>",
                            "<P ALIGN=CENTER><EM><A HREF='http://'></A></EM>",
                            "<pre>",
                            "</pre>",
                            "#",
                            "<b>",
                            "</b>",
                            "<br>",
                            "</br>",
                            "<P ALIGN=CENTER>",
                            "<EM>",
                            "</EM>",
                            "<sup>",
                            "</center>",
                            "<center>",
                            "</sup>",
                            "<sub>",
                            "</sub>",
                            "<SUP>",
                            "</CENTER>",
                            "<CENTER>",
                            "</SUP>",
                            "<SUB>",
                            "</SUB>",
                            "<br />",
                            "<pre />",
                            "<pre/>",
                            "<PRE>",
                            "<Pre>",
                            "<it>",
                            "</it>",
                            "<A ",
                            "</a>",
                            "</A>",
                            "<a ",
                            "_",
                            "--",
                            "</BR>",
                            "<BR>",
                            "&deg;",
                            "</div>",
                            "<div>",
                            "Ã?Â",
                            " ",
                            "***",
                            "<B>",
                            "</B>",
                            "\n"
                        ]
        for item in stringsToRemove:
            userText = userText.replace(item, "")

        for i in range(0, 6):
            userText = userText.replace("  ", " ")
        userText = userText.replace(";", ":")
        userText = userText.replace("&plusmn: 0.001", "")

        ## SEARCH FOR SEXEGESIMAL COORDINATES WITHIN THE BODY TEXT
        try:
            sIter = reSexeg.finditer(userText)
        except:
            sIter = None

        sList = []
        for item in sIter:
            ## CONVERT RA DEC TO DECIMAL DEGREES
            raSec = item.group('raSec')
            if item.group('raSubSec'):
                raSec += item.group('raSubSec')
            decSec = item.group('decSec')
            if item.group('decSubSec'):
                decSec += item.group('decSubSec')
            _raSex = """%s:%s:%s""" % (item.group('raHrs'), item.group('raMin'), raSec)
            _decSex = """%s:%s:%s""" % (item.group('decDeg'), item.group('decMin'), decSec)
            raDegrees = u.sexToDec(_raSex, ra=True)
            decDegrees = u.sexToDec(_decSex)
            sList.extend([[str(raDegrees), str(decDegrees)]])
            userText = userText.replace(item.group('raSex'), " **<font color=blue>" + item.group('raSex') + " </font>** ")
            userText = userText.replace(item.group('decSex'), " **<font color=blue>" + item.group('decSex') + " </font>** ")

        ## SEARCH FOR DECIMAL DEGREES COORDINATES WITHIN THE BODY TEXT
        try:
            sIter2 = reDegree.finditer(userText)
        except:
            sIter2 = None

        for item in sIter2:
            #print item.group('raDDeg'), item.group('decDDeg')
            sList.extend([[item.group('raDDeg'), item.group('decDDeg')]])
            userText = userText.replace(item.group('raDDeg'), " **<font color=green>" + item.group('raDDeg') + " </font>** ")
            userText = userText.replace(item.group('decDDeg'), " **<font color=green>" + item.group('decDDeg') + " </font>** ")

        ## SEARCH FOR SEXEG COORDINATES IN TABLES
        try:
            sIter3 = reSexTable.finditer(userText)
        except:
            sIter3 = None

        for item in sIter3:
            ## CONVERT RA DEC TO DECIMAL DEGREES
            raSec = item.group('raSec')
            if item.group('raSubSec'):
                raSec += item.group('raSubSec')
            decSec = item.group('decSec')
            if item.group('decSubSec'):
                decSec += item.group('decSubSec')
            _raSex = """%s:%s:%s""" % (item.group('raHrs'), item.group('raMin'), raSec)
            _decSex = """%s:%s:%s""" % (item.group('decDeg'), item.group('decMin'), decSec)
            raDegrees = u.sexToDec(_raSex, ra=True)
            decDegrees = u.sexToDec(_decSex)
            sList.extend([[str(raDegrees), str(decDegrees)]])
            userText = userText.replace(item.group('raSex'), " **<font color=#dc322f>" + item.group('raSex') + " </font>** ")
            userText = userText.replace(item.group('decSex'), " **<font color=#dc322f>" + item.group('decSex') + " </font>** ")

        numCoords = len(sList)

        ## SEARCH FOR NAMES IN THE ATEL BODY
        try:
            sIter4 = reName.finditer(header)
        except:
            sIter4 = None
        try:
            sIter5 = reName.finditer(userText)
        except:
            sIter5 = None

        hnList = []
        for item in sIter4:
            hnList.extend([item.group()])
        hnList = list(set(hnList))
        numHeaderName = len(hnList)

        tnList = []
        for item in sIter5:
            tnList.extend([item.group()])
        tnList = list(set(tnList))
        numTextName = len(tnList)
        nList = list(set(hnList + tnList))

        # CLEAN UP THE NAMES BEFORE INGEST
        for i in range(len(nList)):
            nList[i] = at.clean_supernova_name(dbConn, log, nList[i])
        nList = list(set(nList))

        try:
            userText = reName.sub(r"**<font color=#2aa198>\1</font>**", userText)
        except:
            pass
        try:
            header = reName.sub(r"**<font color=#2aa198>\1</font>**", header)
        except:
            pass

        ## DETERMINE THE ATEL TYPE - DISCOVERY, CLASSIFICATION OR OBSERVATION
        disc, obs, clas, correction, comment = 0, 0, 0, 0, 0
        discHead, obsHead, clasHead, correctionHead = 0, 0, 0, 0
        discText, obsText, clasText = 0, 0, 0

        # SEARCH FOR DISCOVERY KEYWORDS IN HEADER AND TEXT
        dList = []
        reDisc = re.compile(r"""(discovered\sby\sMASTER|Detection.{1,20}MASTER|detection\sof\sa\snew\s|discovery|candidate.{1,10}discovered|\ba\s?candidate|\d{1,4}:\s((Bright|MASTER)\sPSN\sin|Possible\snew\s|(A\s)?new.{1,30}(candidate|discovered)|(Bright|MASTER).{1,20}detection))""", re.I | re.M)
        reDiscPhrase = re.compile(r"""(We\sreport\sthe\sdiscovery\s)""", re.I)
        try:
            dpIter = reDiscPhrase.finditer(userText)
        except:
            dpIter = None
        for item in dpIter:
            discHead = 1  # MIGHT AS WELL BE IN THE HEADER - IF reDiscPhrase AT START OF ATEL, DEFINITELY A DISCOVERY
            dList.extend([item.group()])

        try:
            dhIter = reDisc.finditer(header)
        except:
            dhIter = None
        for item in dhIter:
            discHead = 1
            dList.extend([item.group()])

        try:
            dtIter = reDisc.finditer(userText)
        except:
            dtIter = None
        for item in dtIter:
            discText = 1
            dList.extend([item.group()])

        dList = list(set(dList))
        if len(dList) > 0:
            try:
                userText = reDiscPhrase.sub(r"**<font color=#b58900>\1</font>**", userText)
            except:
                pass
            try:
                userText = reDisc.sub(r"**<font color=#b58900>\1</font>**", userText)
            except:
                pass
            try:
                header = reDisc.sub(r"**<font color=#b58900>\1</font>**", header)
            except:
                pass

        # SEARCH FOR CLASSIFICATION KEYWORDS IN HEADER AND TEXT
        cList = []
        reClass = re.compile(r'(classification|SNID|spectroscopic\sconfirmation|GELATO|discovery.*?SN\sI[abcilps]{1,3}n?)', re.I)
        try:
            chIter = reClass.finditer(header)
        except:
            chIter = None
        for item in chIter:
            clasHead = 1
            cList.extend([item.group()])
        try:
            ctIter = reClass.finditer(userText)
        except:
            ctIter = None
        for item in ctIter:
            clasText = 1
            cList.extend([item.group()])

        reClass2 = re.compile(r'(\sis\sa\s|SN\simpostor|type\sI[abcilps]{0,3}n?|\sI[abcilps]{0,3}n?\ssupernova|\sa\sSN\sI[abcilps]{0,3}n?)', re.I)
        try:
            cIter2 = reClass2.finditer(header)
        except:
            cIter2 = None
        for item in cIter2:
            clasHead = 1
            cList.extend([item.group()])

        cList = list(set(cList))
        if len(cList) > 0:
            try:
                userText = reClass.sub(r"**<font color=#b58900>\1</font>**", userText)
            except:
                pass
            try:
                header = reClass.sub(r"**<font color=#b58900>\1</font>**", header)
            except:
                pass
            try:
                header = reClass2.sub(r"**<font color=#b58900>\1</font>**", header)
            except:
                pass

        # SEARCH FOR OBSERVATION KEYWORDS IN HEADER AND TEXT
        oList = []
        reObs = re.compile(r'(observations?|Outburst\sof\s|increase\sin\sflux\s|Progenitor\sIdentification|observed?|detects|new\soutburst|monitoring\sof)', re.I)
        try:
            ohIter = reObs.finditer(header)
        except:
            ohIter = None
        for item in ohIter:
            obsHead = 1
            oList.extend([item.group()])
        try:
            otIter = reObs.finditer(userText)
        except:
            otIter = None
        for item in otIter:
            obsText = 1
            oList.extend([item.group()])

        oList = list(set(oList))
        if len(oList) > 0:
            try:
                userText = reObs.sub(r"**<font color=#b58900>\1</font>**", userText)
            except:
                pass
            try:
                header = reObs.sub(r"**<font color=#b58900>\1</font>**", header)
            except:
                pass

        # SEARCH FOR CORRECTION KEYWORDS IN HEADER AND TEXT
        tList = []
        reCor = re.compile(r'((Correction|Erratum|Errata)\sto)', re.I)
        try:
            tIter = reCor.finditer(userText + header)
        except:
            tIter = None
        for item in tIter:
            tList.extend([item.group()])

        tList = list(set(tList))
        if len(tList) > 0:
            correctionHead = 1
            try:
                userText = reCor.sub(r"**<font color=#b58900>\1</font>**", userText)
            except:
                pass
            try:
                header = reCor.sub(r"**<font color=#b58900>\1</font>**", header)
            except:
                pass

        if "Comment" in tags:
            comment = 1

        # CREATE AN ATELTYPE TAG -- SIMPLE ROUTINE TO GUESS THE 'TYPE' OF ATEL
        atelType = ""
        obs, clas, disc, correction = 0, 0, 0, 0
        ## GIVE HEADER KEYWORDS PRIORITY OVER THE BODY TEXT
        if clasHead == 1:
            clas = 1
        if obsHead == 1:
            obs = 1
        if discHead == 1:
            disc = 1
        if correctionHead == 1:
            correction = 1
        if comment == 1:
            comment = 1

        if clasText == 1 and disc == 0 and obs == 0:
            clas = 1
        if obsText == 1 and disc == 0 and clas == 0:
            obs = 1
        if discText == 1 and obs == 0 and clas == 0:
            disc = 1

        if comment == 1:
            comment = 1

        if comment == 1:
            atelType += " comment "
        if correction == 1:
            atelType += " correction "
        if disc == 1:
            atelType += " discovery "
        if clas == 1:
            atelType += " classification "
        if obs == 1:
            atelType += " observation "

        # if atelType:
        #     atelType = " || **<font color=#b58900>" + atelType + " </font>** "
        header = header + atelType

        ## IF THE ATEL-TYPE IS CLASSIFICATION THEN LOOK FOR THE CLASSIFICATION
        SNTypeList = []
        SNTypeReplace = []
        singleClassification = None
        oneType = None
        if "classification" in atelType:
            try:
                SNTypeIter = reSNType.finditer(header + userText)
            except:
                SNTypeIter is None

            for item in SNTypeIter:
                SNTypeReplace.extend([item.group()])
                SNTypeList.extend([item.group(1)])
                SNTypeList.extend([item.group(2)])
                SNTypeList.extend([item.group(4)])
                SNTypeList.extend([item.group(5)])
                SNTypeList.extend([item.group(6)])
                SNTypeList.extend([item.group(8)])
            SNTypeList = list(set(SNTypeList))
            SNTypeReplace = list(set(SNTypeReplace))

            for item in SNTypeReplace:
                userText = userText.replace(item, " ***<font color=#859900>" + item + " </font>*** ")
                header = header.replace(item, " ***<font color=#859900>" + item + " </font>*** ")

            switch = 0
            for item in SNTypeList:
                if item:
                    if switch == 0:
                        oneType = item
                        switch = 1
                    else:
                        oneType = None
                    header = header + " ***<font color=#859900>" + item + " </font>*** "

        if not atelType:
            atelType = "observation"

        dateParsed = cu.get_now_sql_datetime()

        sqlQuery = """
                        UPDATE atel_fullcontent
                        SET atelType = "%s",
                        dateParsed = "%s"
                        WHERE atelNUmber = %s
                    """ % (atelType, dateParsed, atelNumber,)

        try:
            log.debug("attempting to update the ateltype and parsedate for atel number %s" % (atelNumber,))
            m.execute_mysql_write_query(sqlQuery, dbConn, log)
        except Exception, e:
            log.error("could not update the ateltype and parsedate for atel number %s - failed with this error: %s " % (atelNumber, str(e),))
            return -1

        isSN = 0
        if "Supernovae" in tags:
            isSN = 1

            ## PROVIDE THE SINGLE CLASSIFICATION IF THERE IS ONLY ONE GIVEN
            if oneType is not None:
                singleClassification = oneType
            else:
                singleClassification = None

            #print "ATEL# %s singleClassification %s " % (atelNumber, singleClassification,)

        #if "discovery" in atelType:
        #if "classification" in atelType:
        #if not atelType:

        #wf.write(header + references + tags + "\n\n" + userText + "\n\n## Parsed Values\n\n")
        for item in sList:
            #CREATE AN ATEL 'NAME' & URL USEFUL FOR INGEST
            atelName = "atel_" + str(atelNumber)
            atelUrl = "http://www.astronomerstelegram.org/?read=" + str(atelNumber)
            survey = "atel-coords"
            sqlQuery = """INSERT INTO atel_coordinates (
                                            atelNumber,
                                            atelName,
                                            atelUrl,
                                            survey,
                                            raDeg,
                                            decDeg,
                                            supernovaTag
                                        )
                    VALUES (
                                %s,
                                "%s",
                                "%s",
                                "%s",
                                %s,
                                %s,
                                %s
                            )""" % (atelNumber, atelName, atelUrl, survey, item[0], item[1], isSN)

            try:
                log.debug("attempting to ingest the atel coordinates into the database")
                m.execute_mysql_write_query(sqlQuery, dbConn, log)
            except Exception, e:
                log.error("could not ingest the atel coordinates into the database - failed with this error: %s " % (str(e),))
                return -1

            if singleClassification is not None:
                sqlQuery = """UPDATE atel_coordinates
                                SET singleClassification = "%s"
                                WHERE atelNumber = %s""" % (singleClassification, atelNumber,)

            try:
                log.debug("attempting to update classification for atel %s" % (atelNumber, ))
                m.execute_mysql_write_query(sqlQuery, dbConn, log)
            except Exception, e:
                log.error("could not update classification for atel %s - failed with this error: %s " % (atelNumber, str(e),))
                return -1

            #wf.write("R&D: %s\n\n" % (", ".join(item),))
        for item in nList:
            #CREATE AN ATEL 'NAME' & URL USEFUL FOR INGEST
            atelName = "atel_" + str(atelNumber)
            atelUrl = "http://www.astronomerstelegram.org/?read=" + str(atelNumber)
            survey = "atel-names"
            sqlQuery = """INSERT INTO atel_names (
                                            atelNumber,
                                            atelName,
                                            atelUrl,
                                            survey,
                                            name,
                                            supernovaTag
                                        )
                    VALUES (
                                %s,
                                "%s",
                                "%s",
                                "%s",
                                "%s",
                                %s
                    )""" % (atelNumber, atelName, atelUrl, survey, item, isSN)

            try:
                log.debug("attempting to ingest the atel names into the database")
                m.execute_mysql_write_query(sqlQuery, dbConn, log)
            except Exception, e:
                log.error("could not ingest the atel names into the database - failed with this error: %s " % (str(e),))
                return -1

            if singleClassification is not None:
                sqlQuery = """UPDATE atel_names
                                SET singleClassification = "%s"
                                WHERE atelNumber = %s""" % (singleClassification, atelNumber,)

            try:
                log.debug("attempting to update classification for atel %s" % (atelNumber, ))
                m.execute_mysql_write_query(sqlQuery, dbConn, log)
            except Exception, e:
                log.error("could not update classification for atel %s - failed with this error: %s " % (atelNumber, str(e),))
                return -1

            #wf.write("Name: %s\n\n" % (item,))

        # for item in SNTypeList:
        #     if item:
                #wf.write("SN Type: %s\n\n" % (item,))

        #wf.write("numReferences: %s\n\n" % (numReferences,))
        #wf.write("numCoords: %s\n\n" % (numCoords,))
        #wf.write("numHeaderName: %s\n\n" % (numHeaderName,))
        #wf.write("numTextName: %s\n\n" % (numTextName,))
        #wf.write("discHead: %s\n\n" % (discHead,))
        #wf.write("obsHead: %s\n\n" % (obsHead,))
        #wf.write("clasHead: %s\n\n" % (clasHead,))
        #wf.write("correctionHead: %s\n\n" % (correctionHead,))
        #wf.write("discText: %s\n\n" % (discText,))
        #wf.write("obsText: %s\n\n" % (obsText,))
        #wf.write("clasText: %s\n\n" % (clasText,))
        #wf.write("comment : %s\n\n" % (comment,))

    #wf.close()

    return

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
        main()


###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
