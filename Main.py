# -*- coding: utf-8 -*-
"""
@author: alezanper
"""

import Data_Quality as DQ

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

print(dataWork.removeReplace('email', '@', '?'))










dataWork.close()
