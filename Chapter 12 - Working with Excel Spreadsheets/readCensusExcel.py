#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 17:31:20 2019

@author: nishanth
"""

import os, openpyxl, pprint

os.chdir('/Users/nishanth/Desktop/GIT/PythonPractice')
os.chdir('Chapter 12 - Working with Excel Spreadsheets')

wb = openpyxl.load_workbook('censuspopdata.xlsx')

wb.sheetnames

sheet = wb['Population by Census Tract']
countyData = {}

sheet.max_row

for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C'+ str(row)].value
    population = sheet['D' + str(row)].value
    
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts':0,'population':0})
    
    countyData[state][county]['tracts'] += 1
    
    countyData[state][county]['population'] += int(population)
    
resultFile = open('census2010.py', 'w')

resultFile.write('allData = ' + pprint.pformat(countyData))

resultFile.close()


