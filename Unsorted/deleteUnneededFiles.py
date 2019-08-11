#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:03:23 2019

@author: nishanth
"""

import os, shutil, send2trash, re

os.getcwd()

os.chdir('/Users/nishanth/Desktop/Parents Visa')

for folder, subFolder, file in os.walk('.'):
    for i in file:
        if os.path.getsize(i) > 100000:
            print(i)
    