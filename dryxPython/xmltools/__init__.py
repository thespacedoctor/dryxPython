#!/usr/local/bin/python
# encoding: utf-8
"""
**xmltools**

| Created by David Young on 2012-10-03
| If you have any questions requiring this script please email me: d.r.young@qub.ac.uk

dryx syntax:
 - ``xxx`` = come back here and do some more work
 - ``_someObject`` = a 'private' object that should only be changed for debugging

notes:
    -
"""

############################################
# MAIN LOOP - USED FOR DEBUGGING           #
############################################
def main():
    relativePathToProjectRoot = "../../../"
    sys.path.append("../../../pm_common_code/python/")
    import pesstoMarshallPythonPath as pp
    pp.set_python_path(relativePathToProjectRoot)
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##
    import pmCommonUtils as p

    ################ > SETUP ##################
    ## SETUP DB CONNECTION AND A LOGGER
    dbConn, log = p.settings()

    ## INSTANSIATE THE PESSTO FEEDERS RSS READER (pfr) ##
    pfr = rss_reader()
    pfr.dbConn = dbConn
    pfr.subscriptionTable = "xml_subscriptions"
    #pfr._downloadDirectory = '/Users/Dave/Desktop/xmlToolbox' # ONLY USE FOR DEBUGGING

    ## START LOGGING ##
    logger.info('----- STARTING TO READ THE PESSTO FEEDERS RSS FEEDS -----')

    # SETUP THE SUBSCRIPTIONS
    # pfr.set_subscription('http://feeds.bbci.co.uk/news/rss.xml','bbcNews',['title','updated_parsed'])
    # pfr.set_subscription('http://skyalert.org/feeds/667','crts_css',['updated','ra'])
    # pfr.set_subscription('http://skyalert.org/feeds/290','cbat',['updated','ra'])
    # pfr.set_subscription('http://skyalert.org/feeds/667','crts_css',['updated','ra'])
    # pfr.set_subscription('http://skyalert.org/feeds/664','crts_mls',['updated','ra'])
    # pfr.set_subscription('http://skyalert.org/feeds/665','crts_sss',['updated','ra'])
    pfr.refresh_feeds()

    dbConn.close()
    logger.info('----- FINISHED READING THE XML SUBSCRIPTIONS -----')

    return None


#############################################################################################
# CLASSES                                                                                   #
#############################################################################################
class xml_file():
    """
    | Blue-print for an XML file - can be local (via file path) or remote (via URL).
    | Returns both the XML channel elements and items as a dictionary and a list of dictionaries respectively.

    Variable Attributes:
        - ``rssFeedName`` -- name to be given to the rss feed
        - ``feedUrl`` -- URL of feed (xml file)
    """
    ## VARIABLES THAT NEED ADJUSTED WITH OBJECT INSTANSIATION ##
    rssFeedName = ""
    feedUrl = ""

    def __init__(self,log):
      self.log = log
      return None

    def get_object(self,log):
        """Returns the parsed XML file - split into channel *elements* and *items*.

        **Key Arguments:**
        - ``self``

        **Return:**
        - ``xml_channel_elements`` -- XML file channel elements (a dictionary)
        - ``xml_channel_items`` -- XML file channel items (a dictionary)
        """
        ################ >ACTION(S) ################
        xml_channel_elements = self.get_channel_elements()
        xml_channel_items = self.get_channel_items()
        return xml_channel_elements, xml_channel_items

    ########## METHOD TO GRAB CHANNEL ELEMENTS ##########
    def get_channel_elements(self):
        """Returns the parsed channel *elements* of the XML file.

        **Key Arguments:**
        - ``self``

        **Return:**
        - ``xfce`` -- XML file channel elements (a dictionary)
        """
        # PARSE FEED & LOG NUMBER OF ELEMENTS
        try:
          log.debug("attempting to parse the feed elements from the %s feed" % (self.rssFeedName,))
          log.debug('the '+self.rssFeedName+' rss channel has '+feedElementsCount+ ' feed elements')
          xml = self.parse_feed()
          feedElementsCount = str(len(xml.feed))
        except Exception, e:
          log.critical("could not parse the feed elements from the %s feed - failed with this error %s: " % (self.rssFeedName,str(e),))
          return -1

        # PLACE CHANNEL ELEMENTS INTO A DICTIONARY AND RETURN
        xfce = xml.feed
        return xfce

    ########## METHOD TO GRAB CHANNEL ITEMS ##########
    def get_channel_items(self):
        """Returns the parsed channel *items* of the XML file.

        **Key Arguments:**
        - ``self``

        **Return:**
        - ``xml_channel_items`` -- XML file channel elements (a dictionary)
        """
        # PARSE FEED & NUMBER OF ITEMS IN THE FEED
        try:
          log.debug("attempting to parse the feed items from the %s feed" % (self.rssFeedName,))
          log.debug('the '+self.rssFeedName+' channel has '+feedItemCount+ ' feed items')
          xml = self.parse_feed()
          feedItemCount = str(len(xml.entries))
        except Exception, e:
          log.critical("could not parse the feed items from the %s feed - failed with this error %s: " % (self.rssFeedName,str(e),))
          return -1

        # PLACE CHANNEL ITEMS INTO A LIST OF DICTIONARIES AND RETURN
        xml_channel_items = xml.entries
        return xml_channel_items

    ########## FEED PARSER METHOD ##########
    def parse_feed(self):
        """Parse the XML file

        **Key Arguments:**
        - ``self``

        **Return:**
        - ``xml`` -- the parsed XML file
        """
        ### IMPORTS #########################
        import feedparser
        # TRY AND PARSE THE FEED - RETURN PACKET
        try:
            log.debug('reading the '+self.rssFeedName+' xml file')
            xml = feedparser.parse( self.feedUrl )
        except Exception, e:
            log.critical('failed to read the '+self.rssFeedName+' xml file')
            sys.exit(0)

        return xml


#############################################
# RSS READER (WRITTEN BY DRYX)              #
#############################################
class rss_reader():
    """
    Blue-print for an RSS Reader - builds and maintains an RSS Reader within a MySQL DB

    Variable Attributes:
        - ``dbConn`` -- the connection to the database required to host the rss feed data
        - ``subscriptionTable`` -- name of the table that will hold the feed subscription list
    """
    ## GLOBAL IMPORTS ##

    #### PUBLIC VARIABLE ATTRIBUTES ####
    subscriptionTable = ''

    #### PRIVATE VARIABLE ATTRIBUTES ####
    _downloadDirectory = '/tmp/rss_reader_xml_packets'
    _feedTablePrefix = 'rss_channel_'
    _voeTablePrefix = 'voevent_streams_'

    def __init__(self,dbConn,log):
      self.log = log
      self.dbConn = dbConn
      return None

    #### METHODS ####
    ########################################################################
    ## LAST MODIFIED : 20121101
    ## CREATED : 20121101
    def set_subscription(self,feedURL,rssFeedName,rssFeedSource,uniqueColumns):
        """
            Add an XML subscription to the *subscriptionTable*

            **Key Arguments:**
                - ``feedURL`` -- the URL of the XML file for the rss feed channel
                - ``rssFeedName`` -- name of the rss feed channel to be logged in subscription table e.g. BBC News
                - ``feedSoruce`` -- the top level source e.g. BBC
                - ``uniqueColumns`` -- list of columns to set as unique so that duplicate items are ignored

            Return:
                - ``None``
        """
        ## > IMPORTS ##
        import dryxPython.commonutils as cu
        import dryxPython.webcrawlers as wc
        import dryxPython.mysql as m
        import sys

        ## >SETTINGS ##

        ###########################################################
        # >ACTION(S)                                              #
        ###########################################################
        # FIRST CHECK TO MAKE SURE THE FEED IS NOT SUBSCRIBED TO ALREADY
        sqlQuery = """SELECT table_name
                    FROM information_schema.tables
                    WHERE table_schema = DATABASE()
                    AND table_name = '%s';""" % (self.subscriptionTable,)
        try:
          log.debug("attempting to check if the %s feed is subscribed to yet" % (self.subscriptionTable,))
          rows = m.execute_mysql_read_query(sqlQuery,self.dbConn)
        except Exception, e:
          log.error("could not check if the %s feed is subscribed to yet - failed with this error %s: " % (self.subscriptionTable,str(e),))
          return -1

        if len(rows)!=0:
            sqlQuery = "select count(*) from %s where feedUrl = '%s'" % (self.subscriptionTable, feedURL)
            try:
              log.debug("attempting to count the count the number of subscribed feeds with url: %s" % (feedURL,))
              count = m.execute_mysql_read_query(sqlQuery,self.dbConn)
            except Exception, e:
              log.error("could not count the count the number of subscribed feeds with url: %s - failed with this error %s: " % (feedURL,str(e),))
              return -1

            if count[0]['count(*)'] == 1:
                return None

        ## LOGGING HEADER ##
        log.info('- SUBSCRIBING TO '+rssFeedName+' FEED -')

        # CREATE DOWNLOADS DIRECTORY
        cu.dryx_mkdir(self._downloadDirectory)

        # DOWNLOAD ALL THE XML FILES
        try:
            log.debug("downloading %s xml file" % (rssFeedName,))
            localUrl = wc.singleWebDocumentDownloader(feedURL,self._downloadDirectory,0)
        except Exception, e:
            log.error("could not download %s xml file : %s" % (rssFeedName,str(e)))
            return -1

        # INSTANTIATE THE XML FILE OBJECT
        xf = xml_file()
        xf.feedUrl = localUrl
        xf.rssFeedName = rssFeedName

        # CHANNEL ELEMENTS = TOP LEVEL XML FEED METADATA
        # GRAB THE DICTIONARY OF ELEMENTS AND CREATE/APPEND TO MYSQL TABLE
        xfce = xf.get_channel_elements()
        # ADD EXTRA COLUMNS TO THE DICTIONARY
        now = str(cu.get_now_sql_datetime())
        xfce['dateCreated'] = now
        xfce['dateLastModified'] = now
        xfce['dateLastRead'] = now
        xfce['rssFeedName'] = rssFeedName
        xfce['feedURL'] = feedURL
        xfce['rssFeedSource'] = rssFeedSource
        if(type(uniqueColumns) is list): # I.E. DICTIONARY
            xfce['feedTableUniqueKeyName'] = "_".join(uniqueColumns)
            xfce['uniqueKeyCols'] = ",".join(uniqueColumns)
        else:
            xfce['feedTableUniqueKeyName'] = uniqueColumns
            xfce['uniqueKeyCols'] = uniqueColumns

        # APPEND TO MYSQL SUBSCRIPTION TABLE
        try:
          log.debug("attempting to appending %s feed subscription to the mysql %s table" % (rssFeedName,self.subscriptionTable))
          m.convert_dictionary_to_mysql_table(self.dbConn,xfce,self.subscriptionTable,['feedURL',])
        except Exception, e:
          log.error("could not appending %s feed subscription to the mysql %s table - failed with this error %s: " % (rssFeedName,self.subscriptionTable,str(e),))
          return -1

        ## LOGGING FOOTER ##
        log.info('- SUCCESSFULLY SUBSCRIBED TO '+feedURL+' FEED -')

        return None


    ############################################################################################################
    ## LAST MODIFIED : 20121101
    ## CREATED : 20121101
    def refresh_rss_feeds(self):
        """Refresh all feeds in the *subscriptionTable* - adding feed items to the the relevant RSS channel tables

            **Key Arguments:**

            Return:
                - ``None``
        """
        ## > IMPORTS ##
        import dryxPython.webcrawlers as wc
        import dryxPython.mysql as m
        import dryxPython.commonutils as cu

        ## >SETTINGS ##

        ## LOGGING HEADER ##
        log.info('<m> STARTING TO REFRESH THE FEEDS FOUND IN '+self.subscriptionTable+'<m>')

        ###########################################################
        # >ACTION(S)                                              #
        ###########################################################
        # CREATE DOWNLOADS DIRECTORY
        cu.dryx_mkdir(self._downloadDirectory)

        ## READ THE FEED NAMES AND URLS FROM SUBSCRIPTION TABLE
        sqlQuery = 'SELECT rssFeedName, feedURL, rssFeedSource, dateLastRead, uniqueKeyCols from '+self.subscriptionTable
        try:
          log.debug("attempting to reading feed data from the subscription table : %s" % (self.subscriptionTable,))
          feeds = m.execute_mysql_read_query(sqlQuery,dbConn, log)
        except Exception, e:
          log.error("could not reading feed data from the subscription table : %s - failed with this error %s: " % (self.subscriptionTable,str(e),))
          return -1

        ## DOWNLOAD THE FEED CHANNEL XML FILES AND SWITCH TO LOCAL URL
        remoteURLList = []
        for feed in feeds:
            remoteURLList += [feed['feedURL']]
        try:
          log.debug("attempting to downloading the feed channel xml files")
          localUrls = wc.multiWebDocumentDownloader(remoteURLList,self._downloadDirectory,1)
        except Exception, e:
          log.error("could not downloading the feed channel xml files - failed with this error %s: " % (str(e),))
          return -1

        ifc = 0
        for feed in feeds:
            feed['remoteFeedUrl'] = feed['feedURL']
            feed['feedURL'] = localUrls[ifc]
            ifc += 1

            # INSTANTIATE THE XML FILE OBJECT
            xf = xml_file()
            xf.feedUrl = feed['feedURL']
            xf.rssFeedName = feed['rssFeedName']

            # DETERMINE UNQUIE KEY
            ukCols = str.split(feed['uniqueKeyCols'])

            # CHANNEL ITEMS = BASE LEVEL XML FEED METADATA - THE NEWS/CONTENT
            # GRAB THE LIST OF XML ITEM DICTIONARIES
            xml_channel_items = xf.get_channel_items()
            # ADD EXTRA COLUMNS TO THE DICTIONARY
            now = str(cu.get_now_sql_datetime())
            for item in xml_channel_items:
                item['dateCreated'] = now
                item['dateLastModified'] = now
                item['awaitingAction'] = 1
                item['rssFeedUrl'] = feed['remoteFeedUrl']
                item['rssFeedName'] = feed['rssFeedName']
                item['rssFeedSource'] = feed['rssFeedSource']

            feedTableName = self._feedTablePrefix+feed['rssFeedName']
            feedTableName = cu.make_lowercase_nospace(feedTableName)

            ## APPEND THE DATA TO THE TABLE
            try:
              log.debug("attempting to 'adding data to the %s table" % (feedTableName,))
              for i in range(len(xml_channel_items)):
                log.debug('here is the element dictionary: %s' % (str(xml_channel_items[i].keys()),))
                m.convert_dictionary_to_mysql_table(dbConn,xml_channel_items[i],feedTableName,ukCols)
            except Exception, e:
              log.error("could not 'adding data to the %s table - failed with this error %s: " % (feedTableName,str(e),))
              return -1

        ## LOGGING FOOTER ##
        log.info('<m> SUCCESSFULLY ATTEMPTED TO REFRESH THE FEEDS FOUND IN '+self.subscriptionTable+'<m>')

        return None


    #############################################################################################################
    ## LAST MODIFIED : 20121105
    ## CREATED : 20121105
    def refresh_voevent_feeds(self):
        """Refresh all VoEvents in the *subscriptionTable* - adding feed items to the relevant VoEvent channel tables

            Return:
                - ``None``
        """
        ## > IMPORTS ##
        import dryxPython.webcrawlers as wc
        import dryxPython.mysql as m
        import dryxPython.commonutils as cu
        from VOEventLib import Vutil as vou
        import VOEventLib as vo
        import re
        import sys

        ## >SETTINGS ##

        ## LOGGING HEADER ##
        log.info('<m> STARTING TO REFRESH THE VOEVENT STREAMS FOUND IN '+self.subscriptionTable+'<m>')

        ###########################################################
        # >ACTION(S)                                              #
        ###########################################################
        # CREATE DOWNLOADS DIRECTORY
        cu.dryx_mkdir(self._downloadDirectory)

        ## READ THE FEED NAMES AND URLS FROM SUBSCRIPTION TABLE
        sqlQuery = 'SELECT rssFeedSource, rssFeedName, feedURL, dateLastRead, uniqueKeyCols from '+self.subscriptionTable
        try:
          log.debug("attempting to read the feed names and urls from the %s table" % (self.subscriptionTable,))
          feeds = m.execute_mysql_read_query(sqlQuery,self.dbConn)
        except Exception, e:
          log.error("could not read the feed names and urls from the %s table - failed with this error %s: " % (self.subscriptionTable,str(e),))
          return -1

        ## DOWNLOAD THE FEEDS AND SWITCH TO LOCAL URLS
        remoteURLList = []
        for feed in feeds:
            remoteURLList += [feed['feedURL']]
        try:
          log.debug("attempting to download the voevent stream xml files")
          localUrls = wc.multiWebDocumentDownloader(remoteURLList,self._downloadDirectory,1)
        except Exception, e:
          log.error("could not download the voevent stream xml files - failed with this error %s: " % (str(e),))
          return -1

        ifc = 0
        for feed in feeds:
            feed['voeURL'] = feed['feedURL']
            feed['feedURL'] = localUrls[ifc]
            ifc += 1

            ## CLEAR THE LIST & DICTIONARY REQUIRED TO HOLD THE VOEVENT 'METADATA' - ANY DATA NOT FOUND WITHIN <WHAT>..</WHAT>
            metadataList = []
            metadataDict = {}

            ## CREATE THE VOEVENT ITS & DATA OBJECTS
            try:
              log.debug("attempting to read the %s voevent xml file" % (feed['rssFeedName'],))
              event =  vou.parse(feed['feedURL'])
            except Exception, e:
              log.error("could not read the %s voevent xml file - failed with this error %s" % (feed['rssFeedName'],str(e)))
              return -1

            log.debug("attempting to parse the data found in the %s voevent xml file" % (feed['rssFeedName'],))

            ## PARSE 'DESCRIPTION' VALUES
            try: metadataList += [('description',event.get_Description())]
            except Exception, e: pass

            ## PARSE 'IVORN' VALUES
            try: metadataList += [('ivorn',event.get_ivorn())]
            except Exception, e: pass

            ## PARSE 'ROLE' VALUES
            try: metadataList += [('role',event.get_role())]
            except Exception, e: pass

            ## PARSE 'VERSION' VALUES
            try: metadataList += [('version',event.get_version())]
            except Exception, e: pass

            ## PARSE 'CITATION' VALUES
            try: citations = event.get_Citations()
            except: pass
            try:  metadataList += [('cite',citations)]
            except: pass
            try: metadataList += [('cite_des',citations.get_Description())]
            except Exception, e: pass
            try: cite_ivorn = citations.get_EventIVORN()
            except Exception, e: pass
            try:  metadataList += [('cite_ivorn',cite_ivorn)]
            except: pass
            try: metadataList += [('cite_ivorn_cite',cite_ivorn.get_cite())]
            except Exception, e: pass
            try: metadataList += [('cite_ivorn_value',cite_ivorn.get_valueOf_())]
            except Exception, e: pass

            ## PARSE 'HOW' VALUES
            try: how = event.get_How()
            except Exception, e: pass
            try:  metadataList += [('how',how)]
            except: pass
            try: metadataList += [('how_des',how.get_Description())]
            except Exception, e: pass
            try: how_ref = how.get_Reference()
            except Exception, e: pass
            try:  metadataList += [('how_ref',how_ref)]
            except: pass
            try: metadataList += [('how_ref_mean',how_ref.get_meaning())]
            except Exception, e: pass
            try: metadataList += [('how_ref_mtype',how_ref.get_mimetype())]
            except Exception, e: pass
            try: metadataList += [('how_ref_type',how_ref.get_type())]
            except Exception, e: pass
            try: metadataList += [('how_ref_uri',how_ref.get_uri())]
            except Exception, e: pass
            try: metadataList += [('how_ref_valueOf_',how_ref.get_valueOf_())]
            except Exception, e: pass

            ## PARSE 'REFERENCE' VALUES
            try: reference = event.get_Reference()
            except Exception, e: pass
            try:  metadataList += [('reference',reference)]
            except: pass
            try: metadataList += [('ref_mean',reference.get_meaning())]
            except Exception, e: pass
            try: metadataList += [('ref_mtype',reference.get_mimetype())]
            except Exception, e: pass
            try: metadataList += [('ref_type',reference.get_type())]
            except Exception, e: pass
            try: metadataList += [('ref_uri',reference.get_uri())]
            except Exception, e: pass
            try: metadataList += [('ref_valueOf',reference.get_valueOf_())]
            except Exception, e: pass

            ## PARSE 'WHY' VALUES
            try: why = event.get_Why()
            except Exception, e: pass
            try:  metadataList += [('why',why)]
            except: pass
            try: metadataList += [('why_conc',why.get_Concept())]
            except Exception, e: pass
            try: metadataList += [('why_desc',why.get_Description())]
            except Exception, e: pass
            try: why_inf = why.get_Inference()
            except Exception, e: pass
            try:
                metadataList += [('why_inf',why_inf)]
                log.debug('why_inf value: %s' % (why_inf,))
            except Exception, e: log.debug('why_inf exception %s' % (str(e),))
            try: metadataList += [('why_inf_conc', why_inf.get_Concept())]
            except Exception, e: print "did not find concept:", str(e)
            try: metadataList += [('why_inf_desc', why_inf.get_Description())]
            except Exception, e: pass
            try: metadataList += [('why_inf_name', why_inf.get_Name())]
            except Exception, e: pass
            try: metadataList += [('why_inf_ref', why_inf.get_Reference())]
            except Exception, e: pass
            try: metadataList += [('why_inf_prob', why_inf.get_probability())]
            except Exception, e: pass
            try: metadataList += [('why_inf_rela', why_inf.get_relation())]
            except Exception, e: pass
            try: metadataList += [('why_name',why.get_Name())]
            except Exception, e: pass
            try: metadataList += [('why_ref',why.get_Reference())]
            except Exception, e: pass
            try: metadataList += [('why_expir',why.get_expires())]
            except Exception, e: pass
            try: metadataList += [('why_import',why.get_importance())]
            except Exception, e: pass


            ## PARSE 'WHO' VALUES
            try: who = event.get_Who()
            except Exception, e: pass
            try:  metadataList += [('who',who)]
            except: pass
            try: metadataList += [('who_date', who.get_Date())]
            except Exception, e: pass
            try: metadataList += [('who_des', who.get_Description())]
            except Exception, e: pass
            try: metadataList += [('who_ref', who.get_Reference())]
            except Exception, e: pass
            #### AND 'AUTHOR' IN 'WHO'
            try: author = who.get_Author()
            except Exception, e: pass
            try:  metadataList += [('who_aut',author)]
            except: pass
            try: metadataList += [('who_aut_email', author.get_contactEmail())]
            except Exception, e: pass
            try: metadataList += [('who_aut_name', author.get_contactName())]
            except Exception, e: pass
            try: metadataList += [('who_aut_phone', author.get_contactPhone())]
            except Exception, e: pass
            try: metadataList += [('who_aut_contr', author.get_contributor())]
            except Exception, e: pass
            try: metadataList += [('who_aut_logo', author.get_logoURL())]
            except Exception, e: pass
            try: metadataList += [('who_aut_sname', author.get_shortName())]
            except Exception, e: pass
            try: metadataList += [('who_aut_title', author.get_title())]
            except Exception, e: pass
            try: metadataList += [('who_aut_ivorn', who.get_AuthorIVORN())]
            except Exception, e: pass

            ## PARSE 'WHEREWHEN' VALUES
            ww = vou.getWhereWhen(event)
            for key in ww.keys():
                try: metadataList += [('wherewhen_'+str(key),ww[key])]
                except Exception, e: pass
            ## PARSE BASE 'WHAT' VALUES
            try: what = event.get_What()
            except Exception, e: pass
            try:  metadataList += [('what',what)]
            except: pass
            try: whatdataBaseList = []
            except Exception, e: pass
            try: whatdataBaseList += [('des',what.get_Description())]
            except Exception, e: pass
            try: whatdataBaseList += [('table',what.get_Table())]
            except Exception, e: pass
            try: reference = what.get_Reference()
            except Exception, e: pass
            try:  metadataList += [('ref',reference)]
            except: pass
            ## EITHER NONE OR A CLASS
            try: whatdataBaseList += [('ref_mean',reference.get_meaning())]
            except Exception, e: pass
            try: whatdataBaseList += [('ref_mtype',reference.get_mimetype())]
            except Exception, e: pass
            try: whatdataBaseList += [('ref_type',reference.get_type())]
            except Exception, e: pass
            try: whatdataBaseList += [('ref_uri',reference.get_uri())]
            except Exception, e: pass
            try: whatdataBaseList += [('ref_valueOf',reference.get_valueOf_())]
            except Exception, e: pass

            ## AND 'PARAMS' IN 'WHAT' -- BASE
            try: params = what.get_Param()
            except Exception, e: pass
            for param in params:
                prefix = 'param_'+str(param.get_name())+'_'
                try: whatdataBaseList += [(prefix+'des',param.get_Description())]
                except Exception, e: passset_subscription
                try: whatdataBaseList += [(prefix+'ref', param.get_Reference())]
                except Exception, e: pass
                try: whatdataBaseList += [(prefix+'value', param.get_Value())]
                except Exception, e: pass
                try: whatdataBaseList += [(prefix+'dataType', param.get_dataType())]
                except Exception, e: pass
                try: whatdataBaseList += [(prefix+'name', param.get_name())]
                except Exception, e: pass
                try: whatdataBaseList += [(prefix+'ucd', param.get_ucd())]
                except Exception, e: pass
                try: whatdataBaseList += [(prefix+'unit', param.get_unit())]
                except Exception, e: pass
                try: whatdataBaseList += [(prefix+'utype', param.get_utype())]
                except Exception, e: pass
                try: whatdataBaseList += [(prefix+'value', param.get_value())]
                except Exception, e: pass

            ## AND 'GROUPS' IN 'WHAT'
            try: groups = what.get_Group()
            except Exception, e: pass
            groupsList = []
            for group in groups:
                thisGroupList = []
                try: thisGroupName = str(group.get_name())
                except Exception, e: pass
                try: thisGroupList = [('name',thisGroupName)]
                except Exception, e: pass
                try: params = group.get_Param()
                except Exception, e: pass
                for param in params:
                    try: prefix = 'param_'+str(param.get_name())+'_'
                    except Exception, e: pass
                    try: thisGroupList += [(prefix+'name',param.get_name())]
                    except Exception, e: pass
                    try: thisGroupList += [(prefix+'des',param.get_Description())]
                    except Exception, e: pass
                    try: thisGroupList += [(prefix+'ref', param.get_Reference())]
                    except Exception, e: pass
                    try: thisGroupList += [(prefix+'value', param.get_Value())]
                    except Exception, e: pass
                    try: thisGroupList += [(prefix+'dataType', param.get_dataType())]
                    except Exception, e: pass
                    try: thisGroupList += [(prefix+'name', param.get_name())]
                    except Exception, e: pass
                    try: thisGroupList += [(prefix+'ucd', param.get_ucd())]
                    except Exception, e: pass
                    try: thisGroupList += [(prefix+'unit', param.get_unit())]
                    except Exception, e: pass
                    try: thisGroupList += [(prefix+'utype', param.get_utype())]
                    except Exception, e: pass
                    try: thisGroupList += [(prefix+'value', param.get_value())]
                    except Exception, e: pass
                try: groupsList += [thisGroupList]
                except Exception, e: pass


            ###### CREATE/APPEND TO METADATA SQL TABLE #######
            ## CREATE METADATA DICTIONARY
            log.debug("attempting to create a dictionary of the meta-data parsed from the %s voevent xml file" % (feed['rssFeedName'],))
            metadataDict = {}
            for tag in metadataList:
                key, value = tag
                key = cu.make_lowercase_nospace(key)
                if(type(value) is list):
                    log.debug('key: %s is a list (value %s)' % (key,value))
                    if(len(value)>0):
                        metadataDict[str(key)] = value[0]
                    else:
                        pass
                elif(value):
                    log.debug('key: %s exists and is a %s (value %s)' % (key,type(value),value))
                    metadataDict[str(key)] = value
                else:
                    pass

            # DETERMINE UNQUIE KEY
            unqCols = str.split(feed['uniqueKeyCols'])

            # ADD EXTRA COLUMNS TO THE DICTIONARY
            metadataDict['voEventUrl'] = feed['voeURL']
            now = str(cu.get_now_sql_datetime())
            metadataDict['dateCreated'] = now
            metadataDict['dateLastModified'] = now
            metadataDict['awaitingAction'] = 1
            metadataDict['rssFeedName'] = feed['rssFeedName']
            metadataDict['rssFeedSource'] = feed['rssFeedSource']

            feedTableName = self._voeTablePrefix+feed['rssFeedName']+"_metadata"
            feedTableName = cu.make_lowercase_nospace(feedTableName)
            try:
              log.debug("attempting to append data from the %s voevent xml file into %s" % (feed['rssFeedName'],feedTableName,))
              m.convert_dictionary_to_mysql_table(self.dbConn,metadataDict,feedTableName,unqCols)
            except Exception, e:
              log.error("could not append data from the %s voevent xml file into %s - failed with this error %s: " % (feed['rssFeedName'],feedTableName,str(e),))
              return -1

            ###### CREATE/APPEND TO WHATDATABASE SQL TABLE #######
            ## CREATE WHATDATABASE DICTIONARY
            whatdataBaseDict = {}
            log.debug("creating a dictionary of the what-data parsed from the %s voevent xml file" % (feed['rssFeedName'],))
            for tag in whatdataBaseList:
                key, value = tag
                key = cu.make_lowercase_nospace(key)
                if(type(value) is list):
                    log.debug('key: %s is a list (value %s)' % (key,value))
                    if(len(value)>0):
                        whatdataBaseDict[str(key)] = value[0]
                    else:
                        pass
                elif(value):
                    log.debug('key: %s exists and is a %s (value %s)' % (key,type(value),value))
                    whatdataBaseDict[str(key)] = value
                else:
                    pass

            sqlQuery = "select primaryId from "+feedTableName+" where voEventUrl = '"+feed['voeURL']+"'"
            contextId = m.execute_mysql_read_query(sqlQuery,self.dbConn)
            contextId = contextId

            # ADD EXTRA COLUMNS TO THE DICTIONARY
            whatdataBaseDict['dateCreated'] = now
            whatdataBaseDict['dateLastModified'] = now
            whatdataBaseDict['awaitingAction'] = 1
            whatdataBaseDict['voPrimaryId'] = contextId[0]['primaryId']
            whatdataBaseDict['rssFeedName'] = feed['rssFeedName']
            whatdataBaseDict['rssFeedSource'] = feed['rssFeedSource']
            whatdataBaseDict['voEventUrl'] = feed['voeURL']
            whatdataBaseDict['rssFeedName'] = feed['rssFeedName']
            whatdataBaseDict['rssFeedSource'] = feed['rssFeedSource']

            whatdataBaseTableName = self._voeTablePrefix+feed['rssFeedName']+"_what_base"
            whatdataBaseTableName = cu.make_lowercase_nospace(whatdataBaseTableName)
            try:
              log.debug("attempting to append data from the %s voevent xml file into %s" % (feed['rssFeedName'],whatdataBaseTableName,))
              m.convert_dictionary_to_mysql_table(self.dbConn,whatdataBaseDict,whatdataBaseTableName,['primaryId','voEventUrl'])
            except Exception, e:
              log.error("could not append data from the %s voevent xml file into %s - failed with this error %s: " % (feed['rssFeedName'],whatdataBaseTableName,str(e),))
              return -1

            for groupList in groupsList:
                ###### CREATE/APPEND TO WHATDATA GROUP SQL TABLE #######
                ## CREATE WHATDATABASE GROUP DICTIONARY
                groupDict = {}
                for tag in groupList:
                    key, value = tag
                    key = cu.make_lowercase_nospace(key)
                    if(type(value) is list):
                        log.debug('key: %s is a list (value %s)' % (key,value))
                        if(len(value)>0):
                            groupDict[str(key)] = value[0]
                        else:
                            pass
                    elif(value):
                        log.debug('key: %s exists and is a %s (value %s)' % (key,type(value),value))
                        groupDict[str(key)] = value
                    else:
                        pass

                # ADD EXTRA COLUMNS TO THE DICTIONARY
                groupDict['voEventUrl'] = feed['voeURL']
                groupDict['dateCreated'] = now
                groupDict['dateLastModified'] = now
                groupDict['awaitingAction'] = 1
                groupDict['voPrimaryId'] = contextId[0]['primaryId']

                ukCols = []
                groupTableName = self._voeTablePrefix+feed['rssFeedName']+'_what_group_'+groupDict['name']
                groupTableName = cu.make_lowercase_nospace(groupTableName)
                g = groupTableName
                log.debug('groupTableName %s' % (groupTableName,))
                if "asteroid_params" in g:
                    ukCols = ['primaryId','param_apparent_motion_value','param_cssid_value','param_sssid_value']
                elif "first_detection_params" in g:
                    ukCols = ['primaryId','param_average_seeing_value','param_magnitude_value']
                elif "second_detection_params" in g:
                    ukCols = ['primaryId','param_average_seeing2_value','param_magnitude2_value']
                elif "third_detection_params" in g:
                    ukCols = ['primaryId','param_average_seeing3_value','param_magnitude3_value']
                elif "fourth_detection_params" in g:
                    ukCols = ['primaryId','param_average_seeing4_value','param_magnitude4_value']
                elif "portfolio" in g:
                    ukCols = ['primaryId','param_lightcurve_value']

                try:
                  log.debug("attempting to append data from the %s voevent xml file into %s" % (feed['rssFeedName'],groupTableName,))
                  m.convert_dictionary_to_mysql_table(self.dbConn,groupDict,groupTableName,ukCols)
                except Exception, e:
                  log.error("could not append data from the %s voevent xml file into %s - failed with this error %s: " % (feed['rssFeedName'],groupTableName,str(e),))
                  return -1


        ## LOGGING FOOTER ##
        log.info('<m> SUCCESSFULLY ATTEMPTED TO REFRESH THE FEEDS FOUND IN '+self.subscriptionTable+'<m>')

        return None

############################################
# PUBLIC FUNCTIONS                         #
############################################



############################################
# PRIVATE (HELPER) FUNCTIONS               #
############################################



if __name__ == '__main__':
  main()
