#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 12:33:43 2019

@author: nishanth
"""

import json
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)

jsonDataAsPythonValue

pythonDict = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
jsonPython = json.dumps(pythonDict)

jsonPython

