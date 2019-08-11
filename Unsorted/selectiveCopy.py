#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:37:42 2019

@author: nishanth
"""

import os, shutil, re

os.getcwd()
os.chdir('../')

for folderName, subFolder, fileName in os.walk('/Users/nishanth/Desktop/All Star'):
    print('Current Directory is ' + folderName )
    #for i in subFolder:
        #print('Sub folder inside ' + folderName + ' :' + i)
    for j in fileName:
        if j.endswith('.py'):
            print('Python file name   :' + j)
            shutil.copy(folderName +'/'+ j,'/Users/nishanth/Desktop/PythonFiles' )