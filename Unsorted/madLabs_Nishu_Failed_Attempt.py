#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:37:50 2019

@author: nishanth
"""

import os, shutil, re

os.getcwd()
os.chdir('textFiles')

madText = open('madLabs.txt', 'w')

madText.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')

madText.close()

madLab1 = open('madLabs.txt')

content = madLab1.readlines()

type(content)

madRegex = re.compile(r'ADJECTIVE|NOUN|VERB')

mo = madRegex.findall(content[0])

madDict = {}

for i in mo:
    print('Input the  replacing value for %s' % i)
    madDict[i] = input()

madDict

madLab1.close()
