#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:45:15 2019

@author: nishanth
"""

import shutil, os

os.getcwd()

# copying from text files to python folder
shutil.copy('/Users/nishanth/Desktop/All Star/Python/textFiles/bacon.txt','/Users/nishanth/Desktop/All Star/Python' )

#copying from python folder to textFiles folder with renamed file
shutil.copy('/Users/nishanth/Desktop/All Star/Python/bacon.txt', '/Users/nishanth/Desktop/All Star/Python/textFiles/fuckingbacon.txt')

#copy the entire directory
shutil.copytree('/Users/nishanth/Desktop/All Star/Python/textFiles','/Users/nishanth/Desktop/All Star/Python/textFiles_Backup')

#move the file while renaming it
shutil.move('/Users/nishanth/Desktop/All Star/Python/bacon.txt','/Users/nishanth/Desktop/All Star/Python/textFiles/greasybacon.txt')

# if directory do not exist it will name the file without extension
shutil.move('/Users/nishanth/Desktop/All Star/Python/textFiles/greasybacon.txt','/Users/nishanth/Desktop/All Star/Python/textFiles/greasybacon')


###
os.getcwd()

os.chdir('Desktop/All Star/Python/textFiles_Backup')

for filename in os.listdir():
    if filename.endswith('.txt'):
        print(filename)
        
for filename in os.listdir():
    if filename.endswith('.txt'):
        os.unlink(filename)
        
import send2trash
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not veggie')

baconFile.close()
send2trash.send2trash('bacon.txt')
###

for folderName, subFolder, fileNames in os.walk('/Users/nishanth/Desktop/All Star/Python'):
    print('The current folder name is' + folderName)
    for i in subFolder:
        print('Sub-folder of' + folderName + ': ' + i)
    for j in fileNames:
        print('Files inside' + folderName + ': ' + j)
    print(' ')
  
###
      
import zipfile, os

os.getcwd()
os.chdir('../')

exampleZip = zipfile.ZipFile('textFiles.zip')
exampleZip.namelist()

sonnetinfo = exampleZip.getinfo('textFiles/sonnet29.txt')
sonnetinfo.file_size
sonnetinfo.compress_size

print('compressed file is %sx smaller!' % (sonnetinfo.file_size/sonnetinfo.compress_size))
exampleZip.close()

###

shutil.move('/Users/nishanth/Desktop/All Star/Python/textFiles.zip',
            '/Users/nishanth/Desktop/All Star/Python/textFiles_Backup')

os.getcwd()

os.chdir('textFiles_Backup')

os.getcwd()

exampleZip = zipfile.ZipFile('textFiles.zip')
exampleZip.extractall()
exampleZip.close()

###

exampleZip = zipfile.ZipFile('textFiles.zip')
exampleZip.extract('textFiles/sonnet29.txt')
exampleZip.extract('textFiles/sonnet29.txt', '/Users/nishanth/Desktop/All Star')
exampleZip.close()

###

newZip = zipfile.ZipFile('textFiles.zip','w')
os.getcwd()
newZip.write('sonnet-backup.txt', compress_type = zipfile.ZIP_DEFLATED)

newZip.namelist()
newZip.close()


































