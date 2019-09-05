#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:12:00 2019

@author: nishanth
"""

import openpyxl,os, datetime

pwd()
os.chdir('/Users/nishanth/Desktop/GIT/PythonPractice')
os.chdir('Chapter 12 - Working with Excel Spreadsheets')

wb = openpyxl.load_workbook('example.xlsx') #open workbook
type(wb)

wb.get_sheet_names() # gets you all the sheets names

sheet = wb.get_sheet_by_name('Sheet3')

type(sheet)

sheet.title

anotherSheet = wb.get_active_sheet()

anotherSheet

sheet = wb.get_sheet_by_name('Sheet1')

sheet['A1']

sheet['A1'].value

c = sheet['B1']

c.value

'Row ' + str(c.row) + ', Column ' + str(c.column) + ' is ' + str(c.value)

'Cell ' + c.coordinate + ' is ' + c.value
