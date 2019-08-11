#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 20:22:46 2019

@author: nishanth
"""

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #get address from command line
    address = ' '.join(sys.argv[1:])
else:
    #get address from clipboard
    address = pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/'+address)