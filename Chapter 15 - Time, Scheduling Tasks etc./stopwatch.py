#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 07:36:04 2019

@author: nishanth
"""

import time

print('Press RETURN to begin. Afterwards, press RETURN to "click" the stopwatch. Press COMMAND + C to exit')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s %s %s' %(lapNum,totalTime,lapTime), end = '')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone.')