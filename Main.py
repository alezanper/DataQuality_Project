# -*- coding: utf-8 -*-
"""
Created on Sun Sep 01 13:09:29 2018

@author: faben
"""

import Data_Quality as DQ

dataWork = DQ.Rules('people.csv', ';', False)


#print(dataWork.checkListReference('jobs.csv', 'job'))

#print(dataWork.checkEmail('email'))

#print(dataWork.checkNull('email'))

print(dataWork.checkUnity('email', 7))

