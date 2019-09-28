#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 07:34:43 2019

@author: nishanth
"""

import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile) #This generates reader object
exampleData = list(exampleReader) #converting the data to plain python list

exampleData

exampleData[0][0]
type(exampleData[0][0])

for row in exampleReader:
    print('Row #' + str(exampleReader.line_num)+ ' '+ str(row))
          
outputFile = open('output.csv', 'w', newline = '')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam','eggs','bacon','ham'])
outputFile.close()

outputFile = open('output.csv', 'w', newline = '')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['hello','world','whats','up?'])
outputFile.close()

outputFile = open('output.csv', 'w', newline = '')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['lets','add','some','rows'])
outputWriter.writerow(['spam','eggs','bacon','ham'])
outputWriter.writerow(['hello','world','whats','up?'])
outputFile.close()

csvFile = open('example.tsv','w',newline = '')
csvWriter = csv.writer(csvFile, delimiter = '\t', lineterminator = '\n\n')
csvWriter.writerow(['apple', 'oranges', 'bananas'])
csvWriter.writerow(['chicken','mutton','fish'])
csvWriter.writerow(['carrot','cabbage','cauliflower'])
csvFile.close()