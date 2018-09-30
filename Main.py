# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 13:09:29 2018

@author: faben
"""

import Data_Quality as DQ

dataWork = DQ.Rules('people.csv', ';')

print(dataWork.checkPattern('email', '[a-z]+@[a-z]+.com', False))
