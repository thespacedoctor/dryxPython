#!/usr/local/bin/python
# encoding: utf-8
"""
**regex**

Created by David Young on date 2012-10-24
If you have any questions requiring this script please email me: d.r.young@qub.ac.uk

dryx syntax:
p<Var> = variable formated in the way I want it output to file or screen
xxx = come back here and do some more work

"""

import sys
import os
import re


## DEFINE THE REGEXP COMPONENTS THAT CAN BE USED TO BUILD MORE COMPLICATIED REGEXPS ##


## XX:XX:XX.XX
raHMS_colon = '^\+?([0-9]|([0-1][0-9])|([2][0-3]))(:)[0-5][0-9](:)[0-5][0-9]((\.\d{1,})?)$'
## XX:XX:XX.XX
raHMS_space = '^\+?([0-9]|([0-1][0-9])|([2][0-3]))( )[0-5][0-9]( )[0-5][0-9]((\.\d{1,})?)$'
## XXh XXm XX.XX
raHMS_letters = '^\+?([0-9]|([0-1][0-9])|([2][0-3]))(h )[0-5][0-9](m )[0-5][0-9]((\.\d{1,})?s)$'

## XX:XX:XX.XX
decDMS_colon = '^([\+\-]?([0-9]|[0-8][0-9]))(:)[0-5][0-9](:)[0-5][0-9](\.\d{1,})?$'
## XX XX XX.XX
decDMS_space = '^([\+\-]?([0-9]|[0-8][0-9]))( )[0-5][0-9]( )[0-5][0-9](\.\d{1,})?$'
## XXd XXm XX.XXs
decDMS_space = '^([\+\-]?([0-9]|[0-8][0-9]))( )[0-5][0-9]( )[0-5][0-9](\.\d{1,})?$'



