#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 19:14:51 2019

@author: nishanth
"""
import re
numRegex = re.compile(r'\d+')
numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')

numRegex = re.compile(r'^\d{1,3}(,\d{3})+$')
numRegex.search('12,34,567')

lastNameRegex = re.compile(r'^[A-Z]{1}[a-zA-Z]+\s(Nakamoto)$')
lastNameRegex.search('Satoshi nakamoto')

senRegex = re.compile(r'''(Alice|Bob|Carol)\s
                      (eats|pets|throws)\s
                      (apples|cats|baseballs)
                      (\.)$''', re.VERBOSE | re.IGNORECASE)
senRegex.findall('RoboCop eats apples.')

