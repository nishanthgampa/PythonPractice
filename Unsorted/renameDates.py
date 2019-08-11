#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:26:09 2019

@author: nishanth
"""

import shutil, os, re

datePattern = re.compile(r"""
                         (.*?) # all the text before date
                         ((0|1)?\d)- # one or two digits for month
                         ((0|1|2|3)?\d)- # one or two digits for day
                         ((19|20)\d\d) #four digits of year
                         (.*?)$ #all text after the date
                         """, re.VERBOSE)


for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    
    if mo == None:
        continue
    
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    
    euroFilename = beforePart + '-' + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    
    print('renaming %s to %s...' %(amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)
    