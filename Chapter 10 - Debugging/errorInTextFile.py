#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:10:36 2019

@author: nishanth
"""

import traceback

try:
    raise Exception('This is an error message')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Traceback is printed in the file')