#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 14:44:07 2019

@author: nishanth
"""

import requests, os, bs4

os.chdir('/Users/nishanth/Desktop/All Star/Python/Chaptor 11 - Web Scraping')

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok = True)

while not url.endswith('#'):
                       print('Downloading the page %s ...' % url)
                       res = requests.get(url)
                       res.raise_for_status()
                       
                       soup = bs4.BeautifulSoup(res.text)
                       
                       comicElem = soup.select('#comic img')
                       if comicElem == []:
                           print('Couldn\'t find the image')
                       else:
                           comicUrl = 'http:' + comicElem[0].get('src')
                           
                           print('Downloading the image %s...' % (comicUrl))
                           
                           res = requests.get(comicUrl)
                           res.raise_for_status()
                       imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)), 'wb')
                       
                       for chunk in res.iter_content(1000000):
                           imageFile.write(chunk)
                       imageFile.close()
                       
                       prevLink = soup.select('a[rel = "prev"]')[0]
                       
                       url = 'http://xkcd.com' + prevLink.get('href')

print("Done")
                                             
                                            