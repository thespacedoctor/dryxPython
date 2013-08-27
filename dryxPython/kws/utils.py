# Utilities file.  The following import are used so often I've placed them at
# the top of the file.  Other imports are executed only when needed.

import time
import os, sys
from datetime import datetime
import math
import warnings
warnings.filterwarnings('ignore', '.*the sets module is deprecated.*', DeprecationWarning, 'MySQLdb')


def dbConnect(lhost, luser, lpasswd, ldb, quitOnError=True):
   import MySQLdb

   try:
      conn = MySQLdb.connect (host = lhost,
                              user = luser,
                            passwd = lpasswd,
                                db = ldb)
   except MySQLdb.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
      if quitOnError:
         sys.exit (1)
      else:
         conn=None

   return conn


def getDSS2Image (ra, dec, x, y):
    from BeautifulSoup import BeautifulSoup
    import urllib2
    import urllib
    import urlparse

    baseurl = 'http://archive.eso.org'
    url = baseurl + '/dss/dss/image'
    values = {'ra' : ra,
              'dec' : dec,
              'name' : '',
              'x' : x,
              'y' : y,
              'Sky-Survey' : 'DSS-2-red',
              'equinox' : 'J2000' }

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    soup = BeautifulSoup(BeautifulSoup(the_page).prettify())
    for a in soup.findAll('a'):
        if not a['href'].startswith("http"):
           a['href'] = urlparse.urljoin(baseurl, a['href'])

    for img in soup.findAll('img'):
        if not img['src'].startswith("http"):
           img['src'] = urlparse.urljoin(baseurl, img['src'])

    return soup


def bin(x, digits=0):
    oct2bin = ['000','001','010','011','100','101','110','111']
    binstring = [oct2bin[int(n)] for n in oct(x)]
    return ''.join(binstring).lstrip('0').zfill(digits)


def ra_to_sex (ra, delimiter = ':'):

   # Calculation from Decimal Degrees:

   ra_hh   = int(ra/15)
   ra_mm   = int((ra/15 - ra_hh)*60)
   ra_ss   = int(((ra/15 - ra_hh)*60 - ra_mm)*60)
   ra_ff  = int((((ra/15 - ra_hh)*60 - ra_mm)*60 - ra_ss)*100)

   return ('%02d' %ra_hh + delimiter + '%02d' %ra_mm + delimiter + '%02d' %ra_ss + '.' + '%02d' %ra_ff)


def dec_to_sex (dec, delimiter = ':'):

   if (dec >= 0):
      hemisphere = '+'
   else:
      # Unicode minus sign - should be treated as non-breaking by browsers
      hemisphere = '-' 
      dec *= -1

   dec_deg = int(dec)
   dec_mm  = int((dec - dec_deg)*60)
   dec_ss  = int(((dec - dec_deg)*60 - dec_mm)*60)
   dec_f  = int(((((dec - dec_deg)*60 - dec_mm)*60) - dec_ss)*10)

   return (hemisphere + '%02d' %dec_deg + delimiter + '%02d' %dec_mm + delimiter + '%02d' %dec_ss + '.' + '%01d' %dec_f)


def coords_dec_to_sex (ra, dec, delimiter = ':'):

   return(ra_to_sex(ra,delimiter), dec_to_sex(dec,delimiter))


def ra_in_decimal_hours(ra):

   return(ra/15.0)

# Base-26 converter - for local QUB PS1 IDs
def baseN(num, base=26, numerals="abcdefghijklmnopqrstuvwxyz"):
   if num == 0:
       return numerals[0]

   if num < 0:
       return '-' + baseN((-1) * num, base, numerals)

   if not 2 <= base <= len(numerals):
       raise ValueError('Base must be between 2-%d' % len(numerals))

   left_digits = num // base
   if left_digits == 0:
       return numerals[num % base]
   else:
       return baseN(left_digits, base, numerals) + numerals[num % base]

# Base 26 number padded with base 26 zeroes (a)
def base26(num):
   if num < 0:
      raise ValueError('Number must be positive or zero')

   return baseN(num).rjust(3,'a')


class DictLookup(dict):
   """
   a dictionary which can lookup value by key, or keys by value
   """
   def __init__(self, items=[]):
      """items can be a list of pair_lists or a dictionary"""
      dict.__init__(self, items)

   def get_key(self, value):
      """find the key(s) as a list given a value"""
      return [item[0] for item in self.items() if item[1] == value]

   def get_value(self, key):
      """find the value given a key"""
      return self[key]


def getFlagDefs(flags, dictionary, delimiter = ' + '):
   flagDefs = []

   lookup = DictLookup(dictionary)

   # It's an 8 bit flag at the moment, and we only
   # use 6 bits.  Cycle through the flags and concatenate
   # the keys.
   for i in range(8):
      mask = (1<<7) >>i
      try:
         if flags & mask:
            flagDefs.append(''.join(lookup.get_key(flags & mask)))
      except TypeError:
         # We got a None (i.e. NULL) value
         return ''

   return delimiter.join(flagDefs)

def getCurrentMJD():
   jd = time.time()/86400.0+2440587.5
   mjd = jd-2400000.5
   return mjd


def getDateFromMJD(mjd):
   unixtime = (mjd + 2400000.5 - 2440587.5) * 86400.0;
   theDate = datetime.utcfromtimestamp(unixtime)
   return theDate.strftime("%Y-%m-%d %H:%M:%S")


# 2012-03-26 KWS Added function to convert from date to MJD
def getMJDFromSqlDate(sqlDate):
   mjd = None

   try:
      year, month, day = sqlDate[0:10].split('-')
      hours, minutes, seconds = sqlDate[11:19].split(':')
      t = (int(year), int(month), int(day), int(hours), int(minutes), int(seconds), 0, 0, 0)
      unixtime = int(time.mktime(t))
      mjd = unixtime/86400.0 - 2400000.5 + 2440587.5
   except ValueError, e:
      mjd = None
      print "String is not in SQL Date format."

   return mjd


def getDateFractionMJD(mjd):
   unixtime = (mjd + 2400000.5 - 2440587.5) * 86400.0;
   theDate = datetime.utcfromtimestamp(unixtime)
   dateString = theDate.strftime("%Y:%m:%d:%H:%M:%S")
   (year, month, day, hour, min, sec) = dateString.split(':')
   dayFraction = int(day) + int(hour)/24.0 + int(min)/(24.0 * 60.0) + int(sec)/(24.0 * 60.0 * 60.0)
   dateFraction = "%s %s %05.2f" % (year, month, dayFraction)
   return dateFraction


def sexToDec (sexv, ra = False, delimiter = ':'):
   # Note that the approach below only works because there are only two colons
   # in a sexagesimal representation.
   degrees = 0
   minutes = 0
   seconds = 0
   decimalDegrees = None
   sgn = 1

   try:
      # Look for a minus sign.  Note that -00 is the same as 00.

      (degreesString, minutesString, secondsString) = sexv.split(delimiter)

      if degreesString[0] == '-':
         sgn = -1
      else:
         sgn = 1

      degrees = abs(float(degreesString))
      minutes = float(minutesString)
      seconds = float(secondsString)
      if ra:
         degrees *= 15.0
         minutes *= 15.0
         seconds *= 15.0

      decimalDegrees = (degrees + (minutes / 60.0) + (seconds / 3600.0)) * sgn
      if not ra and (decimalDegrees < -90.0 or decimalDegrees > 90.0):
         decimalDegrees = None
      elif ra and (decimalDegrees < 0.0 or decimalDegrees > 360.0):
         decimalDegrees = None
   except ValueError:
      # Just in case we're passed a dodgy string
      decimalDegrees = None

   return decimalDegrees


def coords_sex_to_dec (ra, dec, delimiter = ':'):

   return(sexToDec(ra, ra=True ,delimiter=delimiter), sexToDec(dec, ra=False, delimiter=delimiter))


# A wrapper for the C++ ConeSearch utility.  In lieu of creating a pure Python facility.
# Note that this is desiged to lookup IDs that are INTEGERS.
def wrapConeSearch(dbuser, dbpass, dbname, dbhost, tablename, ra, dec, radius):
   if dbpass == "":
      dbpass = """ "" """

   cmd = "ConeSearch " + dbuser + " " + dbpass + " " + dbname + " " + dbhost + " quick " + tablename + " "  + str(ra) + " " + str(dec) + " " + str(radius)
   #print cmd
   cmdout= os.popen(cmd)
   result= cmdout.readlines()
   if cmdout.close() != None:
      print "Problem with command"
      return -1

   numberOfMatches = 0
   matchedRowNumberLinePrefix = "Number of matched rows = "

   resultSetSortedBySep = []

   if len(result) == 1:
      # We probably got no matches
      #if result[0].startswith("No matches from "):
      #   print "No results"
      #else:
      #   print "Something went wrong..."
      pass
   else:
      resultSet = []
      for line in result:
         if line.startswith(matchedRowNumberLinePrefix):
            #print line.replace(matchedRowNumberLinePrefix,"").rstrip()
            numberOfMatches = int(line.replace(matchedRowNumberLinePrefix,"").rstrip())
         else:
            #print line.rstrip().lstrip().rstrip('"').lstrip("ID: ").replace(" Separation = ", "")
            (id, separation) = line.rstrip().lstrip().rstrip('"').lstrip("ID: ").replace(" Separation = ", "").split(',')
            keyvaluepair = {"id": int(id), "separation": float(separation)}
            resultSet.append(keyvaluepair)

      resultSetSortedBySep = sorted(resultSet, key=lambda k: k['separation'])

   return numberOfMatches, resultSetSortedBySep



def calculate_cartesians(ra, dec):
   ra = math.radians(ra)
   dec = math.radians(dec)
   cos_dec = math.cos(dec)
   cx = math.cos(ra) * cos_dec
   cy = math.sin(ra) * cos_dec
   cz = math.sin(dec)

   cartesians = (cx, cy, cz)
   return cartesians


pi = (4*math.atan(1.0))
DEG_TO_RAD_FACTOR = pi/180.0
RAD_TO_DEG_FACTOR = 180.0/pi

def getAngularSeparation(ra1, dec1, ra2, dec2):
   """
   Calculate the angular separation between two objects.  If either set of
   coordinates contains a colon, assume it's in sexagesimal and automatically
   convert into decimal before doing the calculation.
   """

   if ':' in str(ra1):
      ra1 = sexToDec(ra1, ra=True)
   if ':' in str(dec1):
      dec1 = sexToDec(dec1, ra=False)
   if ':' in str(ra2):
      ra2 = sexToDec(ra2, ra=True)
   if ':' in str(dec2):
      dec2 = sexToDec(dec2, ra=False)

   angularSeparation = None

   if ra1 and ra2 and dec1 and dec2:

      aa  = (90.0-dec1)*DEG_TO_RAD_FACTOR
      bb  = (90.0-dec2)*DEG_TO_RAD_FACTOR
      cc  = (ra1-ra2)*DEG_TO_RAD_FACTOR
      one = math.cos(aa)*math.cos(bb)
      two = math.sin(aa)*math.sin(bb)*math.cos(cc)

      # Because acos() returns NaN outside the ranges of -1 to +1
      # we need to check this.  Double precision decimal places
      # can give values like 1.0000000000002 which will throw an
      # exception.

      three = one+two
      if (three > 1.0):
         three = 1.0
      if (three < -1.0):
         three = -1.0

      angularSeparation = math.acos(three)*RAD_TO_DEG_FACTOR*3600.0

   return angularSeparation


# 2012-02-29 KWS Python Cone Search code - depends on new htmCircle Python/C++ module.
QUICK = 1
FULL  = 2
COUNT = 3

# Hash of table names.  Produces list containing list of columns and table id.
# 2012-08-01 KWS Added tables for PESSTO lookups
CAT_ID_RA_DEC_COLS = {
   'tcs_transient_objects': [['id', 'ra_psf', 'dec_psf'],0],
   'tcs_2mass_psc_cat': [['designation', 'ra', 'decl'],1],
   'tcs_cat_v_2mass_psc_noextended': [['designation', 'ra', 'decl'],1],
   'tcs_2mass_xsc_cat': [['designation', 'ra', 'decl'],2],
   'tcs_guide_star_cat': [['hstID', 'RightAsc', 'Declination'],3], # Remember that RA and DEC are in RADIANS here
   'tcs_cat_v_guide_star_ps': [['hstID', 'RightAsc', 'Declination'],3], # Remember that RA and DEC are in RADIANS here
   'tcs_ned_cat': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift_1'],4],
   'tcs_cat_v_ned_not_gal_qso': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift_1'],4], # This and the following 3 views given same catalogue ID as base NED catalogue
   'tcs_cat_v_ned_qsos': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift_1'],4],
   'tcs_cat_v_ned_xrays': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift_1'],4],
   'tcs_cat_v_ned_galaxies': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift_1'],4],
   'tcs_sdss_galaxies_cat': [['Objid', 'ra', 'dec_', 'z'],5],
   'tcs_cat_v_sdss_galaxies_notspec': [['Objid', 'ra', 'dec_', 'z'],5], # Not spectroscopic galaxies
   'tcs_sdss_spect_galaxies_cat': [['Objid', 'ra', 'dec_', 'z'],6],
   'tcs_sdss_stars_cat': [['Objid', 'ra', 'dec_'],7],
   'tcs_veron_cat': [['recno', 'viz_RAJ2000', 'viz_DEJ2000', 'z'],8],
   'tcs_cat_deep2dr3': [['OBJNAME', 'RA_deg', 'DEC_deg', 'Z'],9],
   'tcs_cat_md01_ned': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift'],10],
   'tcs_cat_md02_ned': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift'],11],
   'tcs_cat_md03_ned': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift'],12],
   'tcs_cat_md04_ned': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift'],13],
   'tcs_cat_md05_ned': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift'],14],
   'tcs_cat_md06_ned': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift'],15],
   'tcs_cat_md07_ned': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift'],16],
   'tcs_cat_md08_ned': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift'],17],
   'tcs_cat_md09_ned': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift'],18],
   'tcs_cat_md10_ned': [['Object_Name', 'RA_deg', 'DEC_deg', 'Redshift'],19],
   'tcs_cat_md01_chiappetti2005': [['recno', 'viz_RAJ2000', 'viz_DEJ2000'],20],
   'tcs_cat_md01_pierre2007': [['recno', 'viz_RAJ2000', 'viz_DEJ2000'],21],
   'tcs_cat_md02_giacconi2002': [['recno', 'viz_RAJ2000', 'viz_DEJ2000'],22],
   'tcs_cat_md02_lefevre2004': [['recno', 'viz_RAJ2000', 'viz_DEJ2000', 'z'],23],
   'tcs_cat_md02_lehmer2005': [['recno', 'viz_RAJ2000', 'viz_DEJ2000'],24],
   'tcs_cat_md02_virani2006': [['recno', 'viz_RAJ2000', 'viz_DEJ2000'],25],
   'tcs_cat_md04_hasinger2007': [['recno', 'viz_RAJ2000', 'viz_DEJ2000'],26],
   'tcs_cat_md04_trump2007': [['recno', 'viz_RAJ2000', 'viz_DEJ2000', 'z'],27],
   'tcs_cat_md05_brunner2008': [['recno', 'viz_RAJ2000', 'viz_DEJ2000'],28],
   'tcs_cat_md07_laird2009': [['recno', 'viz_RAJ2000', 'viz_DEJ2000'],29],
   'tcs_cat_md07_nandra2005': [['recno', 'viz_RAJ2000', 'viz_DEJ2000'],30],
   'tcs_cat_md08_manners2003': [['recno', 'viz_RAJ2000', 'viz_DEJ2000'],31],
   'tcs_cat_sdss_stars_galaxies': [['Objid', 'ra', 'dec_'],32],
   'tcs_cat_v_sdss_starsgalaxies_stars': [['Objid', 'ra', 'dec_'],32],
   'tcs_cat_v_sdss_starsgalaxies_galaxies': [['Objid', 'ra', 'dec_'],32],
   'tcs_cat_sdss_lrg': [['Objid', 'ra', 'dec_'],33],
   'tcs_cat_slacs': [['Objid', 'ra', 'dec_'],34],
   'tcs_cat_milliquas': [['id', 'ra_deg', 'dec_deg', 'z'],35],
   'tcs_cat_sdss_dr9_photo_stars_galaxies': [['objID', 'ra', 'dec_', 'z_'],36], 
   'tcs_cat_v_sdss_dr9_galaxies_notspec': [['objID', 'ra', 'dec_', 'z_'],36], 
   'tcs_cat_v_sdss_dr9_stars': [['objID', 'ra', 'dec_'],36], 
   'tcs_cat_sdss_dr9_spect_galaxies_qsos': [['objID', 'ra', 'dec_', 'z_'],37], 
   'tcs_cat_v_sdss_dr9_spect_galaxies': [['objID', 'ra', 'dec_', 'z_'],37], 
   'tcs_cat_v_sdss_dr9_spect_qsos': [['objID', 'ra', 'dec_', 'z_'],37], 
   'tcs_cat_rosat_faint_1x29': [['id', 'ra_deg', 'dec_deg'],38],
   'tcs_cat_rosat_bright_1x10': [['id', 'ra_deg', 'dec_deg'],39],
   'tcs_cfa_detections': [['cfa_designation', 'raDeg', 'decDeg'],40],

   # PESSTO database catalogues

   'transientBucket': [['primaryKeyId', 'raDeg', 'decDeg'],1000],
   'view_transientBucketMaster': [['primaryKeyId', 'raDeg', 'decDeg'],1001],
}

# 2012-02-02 KWS Cone Searcher based on the new SWIG C++ code.  Need speed.
# 2012-03-25 KWS Added django so that we can call the Django dict cursor if necessary.
def coneSearch(ra, dec, radius, tableName, htmLevel = 16, queryType = QUICK, conn = None, django = False):

   # 2012-02-02 KWS Require database connections for cone searching
   import MySQLdb

   # 2012-02-02 KWS Introduced a new SWIG htmCircle library for cone searching
   import htmCircle

   # Attempt a cone search of the given tableName.  Use internal models if conn
   # is None, otherwise use a given database connection (allows it to be called
   # externally as part of a script).

   # Code returns a list of lists.  First value in sublist is separation.  Second
   # is the row of data requested from the database.

   message = ""

   if htmLevel not in (16, 20):
      # We don't support anything other than Level 16 or Level 20 queries
      return "Must be HTM level 16 or 20", []

   # Check that RA and DEC are in decimal degrees.  If not, assume sexagesimal and attempt to convert

   if ':' in str(ra):
      ra = sexToDec(ra, ra=True)


   if ':' in str(dec):
      dec = sexToDec(dec, ra=False)


   try:
      quickColumns = CAT_ID_RA_DEC_COLS[tableName][0]
   except KeyError, e:
      return "Table %s not recognised." % tableName, []

   htmWhereClause = htmCircle.htmCircleRegion(htmLevel, ra, dec, radius)

   cartesians = calculate_cartesians(ra, dec)
   cartesianClause = 'and (cx * %.17f + cy * %.17f + cz * %.17f >= cos(%.17f))' % (cartesians[0], cartesians[1], cartesians[2], math.radians(radius/3600.0))

   columns = ['*']

   if queryType == QUICK:
      columns = quickColumns
   elif queryType == COUNT:
      columns = ['count(*) number']

   query = 'select ' + ','.join(columns) + ' from %s' % tableName + htmWhereClause + cartesianClause 
   #print query

   results = []

   if conn:
      # We have a database connection, so use it to make a call to the database

      # DO THE QUERY

      try:
         if django:
            cursor = conn.cursor ()
         else:
            cursor = conn.cursor (MySQLdb.cursors.DictCursor)

         cursor.execute(query)

         if django:
            resultSet = [ dict( (d[0],c) for d, c in zip(cursor.description, row) ) for row in cursor ]
         else:
            resultSet = cursor.fetchall ()


      except MySQLdb.Error, e:
         return "Error %d: %s" % (e.args[0], e.args[1]), []


      if resultSet:
         if queryType == COUNT:
            results = [[0.0, resultSet[0]['number']]]
            return "Count", results

         # Calculate the angular separation for each row
         for row in resultSet:
            if tableName == 'tcs_guide_star_cat':
               # Guide star cat RA and DEC are in RADIANS
               separation = getAngularSeparation(ra, dec, math.degrees(row[CAT_ID_RA_DEC_COLS[tableName][0][1]]), math.degrees(row[CAT_ID_RA_DEC_COLS[tableName][0][2]]))
            else:
               separation = getAngularSeparation(ra, dec, row[CAT_ID_RA_DEC_COLS[tableName][0][1]], row[CAT_ID_RA_DEC_COLS[tableName][0][2]])
            results.append([separation, row])

         # Sort by separation
         results.sort()
      else:
         message = "No matches from %s." % tableName
   else:
      message = query

   return message, results


# 2012-07-31 KWS Added new htmID code to the SWIG library.  This is a simple wrapper for returning
#                the HTM ID for a given (decimal) RA and DEC pair.

def htmID(ra, dec, htmLevel = 16):
   id = None
   if htmLevel == 16 or htmLevel == 20:
      import htmCircle

      try:
         id = htmCircle.htmID(htmLevel, ra, dec)

      except Exception, e:
         # Catch all exceptions. Result will be a None HTM ID.
         pass

   return id



# 2012-05-31 KWS Added new code.
# Brute force cone search.  Go through all objects in a CMF file and find out distance from given RA and DEC pairs.
# Code will produce a list of objects near to our stated RA and DEC pairs, but does not currently eliminate duplicates.

# 2012-06-01 KWS Picked out MJD-OBS, Filename and Filter

def bruteForceCMFConeSearch(filename, coordinatePairs, radius):
   import pyfits as p

   h = p.open(filename)
   t = h[1].data

   cols = h[1].columns

   # Find filename, mjd and filter.  Looking for a single object in a single file will of course yield a single value
   # for all these.  But if this is scripted to look over multiple files, it's useful to know this data.

   mjd = h[0].header['MJD-OBS']
   filter = h[0].header['FPA.FILTERID'].replace('.00000','')

   basename = os.path.basename(filename)

   # Pick out the columns that relate to RA and DEC.

   raIndex = cols.names.index('RA_PSF')
   decIndex = cols.names.index('DEC_PSF')

   resultsTable = []

   # Check for matches, build a results table
   # 2012-06-01 KWS The coordinate pairs are presented in the order we entered them.
   #                We'll therefore add a column to the end of the list of columns
   #                so that we can identify our object again.
   i = 0
   for coord in coordinatePairs:
      for row in t:
         raCat = row[raIndex]
         decCat = row[decIndex]

         separation = getAngularSeparation(coord[0], coord[1], raCat, decCat)
         if separation < radius:
            # Add the returned row (there may be more than one) and the object counter
            resultsTable.append([row, i])
      i += 1

   if resultsTable:
      # Column headers
      for name in cols.names:
         # Change names of the RA/DEC columns so the DS9 catalogue reader can read them
         if name == 'RA_PSF':
            name = 'RA_J2000'
         if name == 'DEC_PSF':
            name = 'DEC_J2000'

         print "%s\t" % name,
      print "%s\t%s\t%s\t%s" % ('filter', 'mjd', 'filename', 'object_id')

      # Data

      for row in resultsTable:
         for col in row[0]:
            print "%s\t" % col,

         print "%s\t%s\t%s\t%s" % (filter, mjd, basename, row[1])

   return



# 2011-06-21 KWS New code added

# J2000 to Galactic coordinates calculation
# This code extracted from a JavaScript utility
# and converted into Python

J2000toGalactic = [
                   -0.054875529, -0.873437105, -0.483834992,
                    0.494109454, -0.444829594,  0.746982249,
                   -0.867666136, -0.198076390,  0.455983795
                  ]


# returns a radec array of two elements
def transform ( coords, matrix ):
   pi = math.pi

   r0 = calculate_cartesians(coords[0], coords[1]) 

   s0 = [
         r0[0]*matrix[0] + r0[1]*matrix[1] + r0[2]*matrix[2], 
         r0[0]*matrix[3] + r0[1]*matrix[4] + r0[2]*matrix[5], 
         r0[0]*matrix[6] + r0[1]*matrix[7] + r0[2]*matrix[8]
        ] 
 
   r = math.sqrt ( s0[0]*s0[0] + s0[1]*s0[1] + s0[2]*s0[2] )

   result = [ 0.0, 0.0 ]
   result[1] = math.asin ( s0[2]/r )

   cosaa = ( (s0[0]/r) / math.cos(result[1] ) )
   sinaa = ( (s0[1]/r) / math.cos(result[1] ) )
   result[0] = math.atan2 (sinaa,cosaa)
   if result[0] < 0.0:
      result[0] = result[0] + pi + pi

   # Convert to degrees

   result[0] = math.degrees(result[0])
   result[1] = math.degrees(result[1])

   return result


# 2012-03-07 KWS Created redshiftToDistance calculator based on our C++ code,
#                which is itself based on Ned Wright's Cosmology Calculator code.

def redshiftToDistance(z):

   # Cosmological Parameters (to be changed if required)
   WM = 0.3           # Omega_matter
   WV = 0.7           # Omega_vacuum
   H0 = 70.0           # Hubble constant (km s-1 Mpc-1)

   # Other variables
   h = H0/100.0
   WR = 4.165E-5/(h*h)     # Omega_radiation
   WK = 1.0-WM-WV-WR       # Omega_curvature = 1 - Omega(Total)
   c = 299792.458          # speed of light (km/s)

   # Arbitrarily set the values of these variables to zero just so we can define them.

   DCMR  = 0.0             # comoving radial distance in units of c/H0
   DCMR_Mpc = 0.0          # comoving radial distance in units of Mpc
   DA = 0.0                # angular size distance in units of c/H0
   DA_Mpc = 0.0            # angular size distance in units of Mpc
   DA_scale = 0.0          # scale at angular size distance in units of Kpc / arcsec
   DL = 0.0                # luminosity distance in units of c/H0
   DL_Mpc = 0.0            # luminosity distance in units of Mpc
   DMOD = 0.0              # Distance modulus determined from luminosity distance
   a = 0.0                 # 1/(1+z), the scale factor of the Universe

   az = 1.0/(1.0+z)        # 1/(1+z), for the given redshift

   # Compute the integral over a=1/(1+z) from az to 1 in n steps
   n = 1000
   for i in range(n):
      a = az+(1.0-az)*(i+0.5)/n
      adot = math.sqrt(WK+ (WM/a) + (WR/(math.pow(a,2))) +(WV*math.pow(a,2)))
      DCMR = DCMR + 1.0/(a*adot)

   DCMR = (1.0-az)*DCMR/n           # comoving radial distance in units of c/H0
   DCMR_Mpc = (c/H0)*DCMR           # comoving radial distance in units of Mpc

   # Tangental comoving radial distance
   x = math.sqrt(abs(WK))*DCMR
   if x > 0.1:
      if WK > 0.0:
         ratio = 0.5*(math.exp(x)-math.exp(-x))/x
      else:
         ratio = math.sin(x)/x
   else:
      y = math.pow(x,2)
      if WK < 0.0:
         y=-y
      ratio = 1 + y/6.0 + math.pow(y,2)/120.0

   DA = az*ratio*DCMR               #angular size distance in units of c/H0
   DA_Mpc = (c/H0)*DA               #angular size distance in units of Mpc
   DA_scale = DA_Mpc/206.264806     #scale at angular size distance in units of Kpc / arcsec
   DL = DA/math.pow(az,2)                #luminosity distance in units of c/H0
   DL_Mpc = (c/H0)*DL               #luminosity distance in units of Mpc
   DMOD = 5*math.log10(DL_Mpc*1e6)-5     #Distance modulus determined from luminosity distance


   results = \
   {
      "dcmr_mpc": DCMR_Mpc,
      "da_mpc": DA_Mpc,
      "da_scale": DA_scale,
      "dl_mpc": DL_Mpc,
      "dmod": DMOD,
      "z" : z
   }

   return results


# Some common error codes for bad HTTP access

OK                 = 0
PAGE_NOT_FOUND     = 1
BAD_SERVER_ADDRESS = 2
HTTP_ERROR         = 3

def getRemoteWebPage(url, username=None, password=None, realm=None):
   import urllib2

   responseErrorCode = OK
   responsePage = ''

   if username and password:
      # Use authentiction credentials

      # We want to do some basic authentication.
      # NOTE - if we don't know the Realm, just enter None for the first
      #        parameter of add_password
      #realm = 'Restricted Section'

      passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
      passman.add_password(realm, url, username, password)
      authhandler = urllib2.HTTPBasicAuthHandler(passman)
      # create the AuthHandler

      opener = urllib2.build_opener(authhandler)
      urllib2.install_opener(opener)

   try:
      req = urllib2.Request(url)
      responsePage = urllib2.urlopen(req).read()

   except urllib2.HTTPError, e:
      if e.code == 404:
         print "Page not found. Perhaps the server has not processed the request yet"
         responseErrorCode = PAGE_NOT_FOUND
      else:
         print e
         responseErrorCode = HTTP_ERROR

   except urllib2.URLError, e:
      print "Bad URL"
      responseErrorCode = BAD_SERVER_ADDRESS

   return (responsePage, responseErrorCode)

# 2012-10-04 KWS Moved enum to utils.py
def enum(**enums):
   return type('Enum', (), enums)

