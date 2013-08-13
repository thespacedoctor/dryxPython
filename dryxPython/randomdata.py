#!/usr/local/bin/python
# encoding: utf-8
"""
**randomdata**

| Created by David Young on 2012-07-16
| If you have any questions requiring this script please email me: d.r.young@qub.ac.uk

**dryx syntax:**
 - ``xxx`` = come back here and do some more work
 - ``_someObject`` = a 'private' object that should only be changed for debugging

**notes:**
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import math
import random
from datetime import datetime, date, time, timedelta

#############################################################################################
#                                         DRYX METHODS COLLECTION
#############################################################################################

## FUNCTION TO PRDUCE A RANDOM LETTER
def random_letter():
  """
  get a random lowercase letter.
  """
  randomNum = math.ceil(random.random()*26);

  if (randomNum == 1): randomLetter = "a"
  if (randomNum == 2): randomLetter = "b"
  if (randomNum == 3): randomLetter = "c"
  if (randomNum == 4): randomLetter = "d"
  if (randomNum == 5): randomLetter = "e"
  if (randomNum == 6): randomLetter = "f"
  if (randomNum == 7): randomLetter = "g"
  if (randomNum == 8): randomLetter = "h"
  if (randomNum == 9): randomLetter = "i"
  if (randomNum == 10): randomLetter = "j"
  if (randomNum == 11): randomLetter = "k"
  if (randomNum == 12): randomLetter = "l"
  if (randomNum == 13): randomLetter = "m"
  if (randomNum == 14): randomLetter = "n"
  if (randomNum == 15): randomLetter = "o"
  if (randomNum == 16): randomLetter = "p"
  if (randomNum == 17): randomLetter = "q"
  if (randomNum == 18): randomLetter = "r"
  if (randomNum == 19): randomLetter = "s"
  if (randomNum == 20): randomLetter = "t"
  if (randomNum == 21): randomLetter = "u"
  if (randomNum == 22): randomLetter = "v"
  if (randomNum == 23): randomLetter = "w"
  if (randomNum == 24): randomLetter = "x"
  if (randomNum == 25): randomLetter = "y"
  if (randomNum == 26): randomLetter = "z"
  return randomLetter

## FUNCTION TO GENERATE RANDOM(ISH) RA & DEC (DEG)
def random_ra_dec():
  """
  get a random coordinate set

  Returns a tuple: ( ``randomRa``, ``randomDec``,```randomRaErr``,``randomDecErr``)
  """
  randomRa = random.random()*360.
  randomDec = -90+random.random()*180.
  randomRaErr = random.random()/360.
  randomDecErr = random.random()/360.
  return (randomRa, randomDec, randomRaErr, randomDecErr)

## FUNCTION TO GENERATE A RANDOM DATE BETWEEN TWO GIVEN DATES
def random_date_in_range(dateLower, dateUpper):
  """
  get a random date within a range of two dates.
  """
  dateRange = dateUpper-dateLower
  randomTimeInterval = timedelta(days=dateRange.days*random.random())
  randomDate = dateLower+randomTimeInterval
  return randomDate

## FUNCTION TO GENERATE A MAGNITUDE REALISTIC AND ERROR
def random_magnitude():
  """
  Get a random magnitude

  Returns:
   - ``magnitude`` -- a random magnitude < 16.0mag
   - ``magnitudeError`` -- a random magnitude error
  """
  base = 16.0
  magnitude = base + random.random()*7.0
  magnitudeError = random.random()*0.5
  return magnitude, magnitudeError

## FUNCTION TO GENERATE 'FILTER' COLUMN VALUE
def random_filter():
  """
  get a random filter

  Returns:
   - ``randomFilter`` -- a random telescope filter
  """
  randomNum = math.ceil(random.random()*7)

  if (randomNum == 1): randomFilter = "g"
  if (randomNum == 2): randomFilter = "r"
  if (randomNum == 3): randomFilter = "i"
  if (randomNum == 4): randomFilter = "z"
  if (randomNum == 5): randomFilter = "B"
  if (randomNum == 6): randomFilter = "V"
  if (randomNum == 7): randomFilter = "R"
  return randomFilter

## FUNCTION TO GENERATE SOURCE REDSHIFT
def random_redshift(lowerLimit,upperLimit):
  """
  Get a random redshift

  Returns:
   - ``redshift`` -- a random redshift between the limits provided

  **Key Arguments:**
   - ``lowerLimit`` -- lower limit to random redhsift range
   - ``upperLimit`` -- upper limit to random redhsift range


  """
  deltaRedshift = upperLimit-lowerLimit
  redshift = lowerLimit+deltaRedshift*random.random()
  return redshift

## FUNCTION TO SEE IF A NUMBER IS ODD OR EVEN
def is_odd(number):
  """
  Determine if the number is odd or not

  **Key Arguments:**
   - ``number`` -- number to be tested for 'odd'ness

  Returns:
   - True or False -- depending on whether the arugment is odd or even
  """
  if number%2==0:
      return False
  else:
      return True

## FUNCTION TO SEE IF A NUMBER IS ODD OR EVEN
def is_even(number):
  """
  Determine if the number is even or not

  **Key Arguments:**
   - ``number`` -- number to be tested for 'even'ness

  Returns:
   - True or False -- depending on whether the arugment is even or odd
  """
  if number%2==0:
    return True
  else:
    return False

## FUNCTION TO GENERATE A RANDOM SENTENCE (LOREM STYLE)
def random_sentence():
  """
  get a random lorem sentence

  Returns:
    - ``sentence`` -- random Lorem snippet
  """
  randomNum = math.ceil(random.random()*4)

  if (randomNum == 1): sentence = "Lorem ipsum dolor sit amet"
  if (randomNum == 2): sentence = "consectetur adipisicing elit"
  if (randomNum == 3): sentence = "sed do eiusmod tempor incididunt ut labore"
  if (randomNum == 4): sentence = "dolore magna aliqua"
  return sentence


## FUNCTION TO GENERATE RANDOM SN SPECTRAL TYPE
def random_sn_spectral_type():
  """
  get a random supernova spectral type

  Returns:
    - ``SpectralType`` -- random SN spectral type
  """
  randomNum = random.randint(1,7)

  if (randomNum == 1): SpectralType = "Ic"
  if (randomNum == 2): SpectralType = "IIP"
  if (randomNum == 3): SpectralType = "IIn"
  if (randomNum == 4): SpectralType = "Ia"
  if (randomNum == 5): SpectralType = "Ib"
  if (randomNum == 6): SpectralType = "??"
  if (randomNum == 7): SpectralType = "Ia"
  return SpectralType

## FUNCTION TO GENERATE 'EXPTIME' COLUMN VALUE
def random_exptime():
  """
  get a random exposure time

  Returns:
    - ``randomExptime`` -- a random exptime from a set of discrete values
  """
  randomNum = random.randint(1,7)

  if (randomNum == 1): randomExptime = "200"
  if (randomNum == 2): randomExptime = "100"
  if (randomNum == 3): randomExptime = "50"
  if (randomNum == 4): randomExptime = "250"
  if (randomNum == 5): randomExptime = "360"
  if (randomNum == 6): randomExptime = "720"
  if (randomNum == 7): randomExptime = "240"
  return randomExptime

## FUNCTION TO GENERATE REFERENCE SYSTEM COLUMN VALUES
def random_filter_set():
  """
  get a random astronomical filter set

  Returns:
    - ``randomRefSource`` -- random filter set name (sdss, 2MASS ...)
  """
  randomNum = random.randint(1,3)

  if (randomNum == 1): randomRefSource = "sdss"
  if (randomNum == 2): randomRefSource = "2MASS"
  if (randomNum == 3): randomRefSource = "Johnson-Cousins"
  return randomRefSource

## FUNCTION TO GENERATE REFERENCE SYSTEM COLUMN VALUES
def random_human_name():
  """
  get a random human name (rock star!)

  Returns:
    - ``randomName`` -- a random human name from a set of 7
  """
  randomNum = random.randint(1,7)

  if (randomNum == 1): randomName = "guy garvey"
  if (randomNum == 2): randomName = "thom yorke"
  if (randomNum == 3): randomName = "jack steadman"
  if (randomNum == 4): randomName = "gemma hayes"
  if (randomNum == 5): randomName = "ryan adams"
  if (randomNum == 6): randomName = "bon iver"
  if (randomNum == 7): randomName = "johnny cash"
  return randomName




