#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:05:42 2019

@author: nishanth
"""

def spam():
    bacon()

def bacon():
    raise Exception('How about you go fuck yourself?')

spam()
