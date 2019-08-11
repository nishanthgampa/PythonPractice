#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:06:13 2019

@author: nishanth
"""

#Usage



import shelve, pyperclip, sys

mcbshelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbshelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbshelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1] in mcbshelf.keys():
        pyperclip.copy(mcbshelf[sys.argv[1]])
    
    
mcbshelf.close()
