#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 07:45:09 2019

@author: nishanth
"""

import time

time.time()

def calcProd():
    product = 1
    for i in range(1,100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()

print('The result is %s digits long' % len(str(prod)))
print('elapsed time is %s' %(endTime - startTime))

for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)
    
now = time.time()
now

round(now,2)

round(now,4)

round(now)
