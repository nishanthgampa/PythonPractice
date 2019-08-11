#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 20:52:36 2019

@author: nishanth
"""

import os, shutil, re

os.getcwd()

os.chdir('/Users/nishanth/Desktop/All Star/Python/textFiles')

os.listdir()
print("What would you like to search for, please enter:")
regexSearch = re.compile(str(input()))

for textFile in os.listdir():
    if textFile.endswith('.txt') == 1:
        openText = open(textFile)
        readText = openText.readlines()
        #print(readText)
        print("Contents in the file name %s" % textFile)
        for i in readText:
            regexResult = regexSearch.search(i)
            if regexResult != None:
                print(i)
            
        
        
        
