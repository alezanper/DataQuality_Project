# -*- coding: utf-8 -*-
"""
Created on Sun Sep 01 13:09:29 2018

@author: alezanper
"""

import Data_Quality as DQ
import pandas as pd

#people = pd.read_csv('people.csv', delimiter=';', encoding = 'iso-8859-1')
#print(people.head())

#people['email'] = people['email'].str.replace('@', '?')
#print(people.head())





# Start data quality rules 
dataWork = DQ.Rules('people.csv', 
                    ';', 
                    True) # False for retrieve bad registers only

#print(dataWork.checkListReference('jobs.csv', 'job', 'job'))
#print('.........')

#dataWork.checkPattern('email', '[\w]+@[\w]+.com')
#print(dataWork.checkListReference('jobs.csv', 'job', 'job'))
#print(dataWork.checkMaxLength('job', 10))
#print(dataWork.checkContains('job', 'developer'))

print(dataWork.removeBadCharacters('email', '@', '6'))










#dataWork.close()
