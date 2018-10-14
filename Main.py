# -*- coding: utf-8 -*-
"""
Created on Sun Sep 01 13:09:29 2018

@author: alezanper
"""

import Data_Quality as DQ






# Start data quality rules 
dataWork = DQ.Rules('people.csv', 
                    ';', 
                    True) # False for retrieve bad registers only

#print(dataWork.checkListReference('jobs.csv', 'job', 'job'))
#print('.........')

#dataWork.checkPattern('email', '[\w]+@[\w]+.com')
#print(dataWork.checkListReference('jobs.csv', 'job', 'job'))
print(dataWork.checkMaxLength('job', 10))

dataWork.close()
