#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 20:21:08 2019

@author: nishanth
"""


import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
print(res)
res.status_code == requests.codes.ok

res.raise_for_status()

len(res.text)

print(res.text[:250])

#-----------------------------------------------

res1 = requests.get('http://inventwithpython.com/page_that_does_not_exist')

res1.raise_for_status()

res1.status_code 

#-----------------------------------------------

res2 = requests.get('http://inventwithpython.com/page_that_does_not_exist')
print(res2)
try:
    res2.raise_for_status()
except:
    print('There was a problem: %s error' %(res2.status_code))

#-----------------------------------------------
    

res3 = requests.get('https://automatetheboringstuff.com/files/rj.txt')
romeoJuliet = open('rj.txt','wb')
res3.raise_for_status()
for chunk in res3.iter_content():
    romeoJuliet.write(chunk)

romeoJuliet.close()

pwd()

#-------------------------------------------------

import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)

#-----------------------------------------------

import os
os.getcwd()
os.chdir('/Users/nishanth/Desktop/All Star/Python/Chaptor 11 - Web Scraping')

emapleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(emapleFile.read())
elems = exampleSoup.select('#author')
type(elems)
len(elems)
type(elems[0])
elems[0].getText()
str(elems[0])
elems[0].attrs

pElems = exampleSoup.select('p')
str(pElems[0])
pElems[0].getText()
str(pElems[1])
pElems[1].getText()
str(pElems[2])
pElems[2].getText()

spamElem = exampleSoup.select('span')[0]
str(spamElem)



