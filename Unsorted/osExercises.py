#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:11:03 2019

@author: nishanth
"""

import os

x = os.path.join('./','Desktop','All Star')
#‎⁨Macintosh HD⁩ ▸ ⁨Users⁩ ▸ ⁨nishanth⁩ ▸ ⁨Desktop⁩

os.getcwd()
os.chdir(x)
os.chdir('/Users/nishanth/Desktop/All Star')

os.makedirs('/Users/nishanth/Desktop/All Star/Nishanth/WhatsUpBuddy/ShallWeSmokePot')

os.getcwd()

os.chdir('./Nishanth')

os.chdir('../python')

os.path.abspath('.')

os.chdir('../')

os.path.abspath('.')

os.path.abspath('./All Star/Nishanth')

os.path.isabs('.')

os.path.isabs(os.path.abspath('.'))

os.path.relpath('/Users/nishanth/Desktop/All Star/Nishanth/WhatsUpBuddy/ShallWeSmokePot')

os.path.relpath('/Users/nishanth/Desktop/Education/MySQL')

os.chdir('./All Star/Nishanth')

myPath = '/Users/nishanth/Desktop/All Star/Python/allMyDogs.py'

os.path.basename(myPath)
os.path.dirname(myPath)

os.path.split(myPath)

myPath.split(os.path.sep)

os.path.getsize(myPath)

os.listdir(os.path.dirname(myPath))

totalSize = 0
for files in os.listdir(os.path.dirname(myPath)):
    totalSize = totalSize + os.path.getsize(os.path.join(os.path.dirname(myPath),files))

print(totalSize)    

os.path.exists('/users/nishanth/desktop/all star/python/allMyDogs.py')    

os.path.isdir(os.path.dirname(myPath))    
os.path.isfile(os.path.dirname(myPath))    
os.path.isfile(os.path.basename(myPath))
os.path.isfile(myPath)


os.getcwd()
os.chdir('../Python')

helloFile = open('hello.txt')
helloContent = helloFile.read()
print(helloContent)

sonnetFile = open('sonnet29.txt')
sonnetFile.readlines()

os.mkdir('textFiles')
os.chdir('textFiles')

baconFile = open('bacon.txt', 'w')
baconFile.write('I used to love bacon\n But I over ate bacon and\n I dont like it as much as I used to like it')

baconFile.close()
baconFile = open('bacon.txt','a')
baconFile.write('I wish I didn\'t over eat and got sick of it')

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.readlines()
content
baconFile.close()

import shelve
shelfFile = shelve.open('myData')
dogs = ['Harley','Zorro','Hercules','Whisky']
shelfFile['dogs'] = dogs
shelfFile.close()

shelfFile = shelve.open('myData')
type(shelfFile)
shelfFile['dogs']
shelfFile.close()

shelfFile = shelve.open('myData')
list(shelfFile.keys())
list(shelfFile.values())
shelfFile.close()






















