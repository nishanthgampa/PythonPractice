#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:38:41 2019

@author: nishanth
"""

import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
        
        print('creating %s...' %(zipFilename))
        
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    
    for folderName, subFolder, fileName in os.walk(folder):
        print('Adding files in %s...' %(folderName))
        
        backupZip.write(folderName)
        for filename in fileName:
            newBase = os.path.basename(folder) 
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(folderName, filename))
    backupZip.close()
    print('Done')
    
os.chdir('/Users/nishanth/Desktop/All Star/Python')
backupToZip('textFiles')
            
        
        