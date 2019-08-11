#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 19:32:33 2019

@author: nishanth
"""

import re

os.getcwd()
os.chdir('textFiles')

madLabs = open('madLabs.txt')

madText = madLabs.readlines()

madLabs.close()

madRegex = re.compile(r'ADJECTIVE|VERB|ADVERB|NOUN')

while True:
    madGroup = madRegex.search(madText[0])
    
    if madGroup == None:
        break
    if madGroup.group() == 'ADJECTIVE' or madGroup.group() == 'ADVERB':
        print('Enter a %s' % madGroup.group())
    elif madGroup.group() == 'NOUN' or madGroup.group() == 'VERB':
        print('Enter a %s' % madGroup.group())
    i = input()
    
    madText[0] = madRegex.sub(i, madText[0], 1)
    print(madText[0])

print("Name your file:")
name = input()
newFile = open('madLabs_new.txt', 'w')
newFile.write(madText[0])    
newFile.close()
