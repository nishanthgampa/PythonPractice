#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:29:38 2019

@author: nishanth
"""

import os, shutil, re

#raise Exception("You suck bitch")

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol must be single character string")
    if width <= 2:
        raise Exception("Width must be greater than 2")
    if height <= 2:
        raise Exception("Height must be greater than 2")
        
    print( symbol * width )
    for i in range(height-2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print( symbol * width )
    
for symbol, width, height in (('*', 5, 6), ('ZZ',6,3),('Z',1,3)):
    try: 
        boxPrint(symbol, width, height)
    except Exception as err:
        print('An exception occured: ' + str(err))