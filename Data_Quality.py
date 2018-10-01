# -*- coding: utf-8 -*-
"""
Created on Sun Sep 01 13:00:15 2018

@author: alezanper
"""

import pandas as pd 

encoding = 'iso-8859-1'

class Rules:
    
    
    data = pd.DataFrame()   # Data to work with
    counter = 0             # Size of dataFrame
    goods = False           # False for return bad registers
    delimiter = ','
    
    """
    Loading file into dataframe
    """
    def __init__(self, filename, delimiter, goods):
        self.data = pd.read_csv(filename,
                       delimiter = delimiter,
                       encoding = encoding)
        
        self.counter = (self.data).shape[0]
        self.goods = goods
        self.delimiter = delimiter
        
        
    """
    Checking for null values
    """
    def checkNull(self, columnToAnalize):
        #Checking for null values
        return self.data[self.data[columnToAnalize].isna()
                         == (not self.goods)]
    
    
    """
    Checking for unicity
    """
    def checkUnity(self, columnToAnalize, maxRepeated):
        #Checking for null values
        if(self.goods):
            return self.data.groupby(columnToAnalize).filter(lambda x: len(x) == 1)
        else:
            return self.data.groupby(columnToAnalize).filter(lambda x: len(x) > maxRepeated)
        

    """
    Checking for pattern
    """
    def checkPattern(self, columnToAnalize, pattern):
        #Checking pattern and returning data that match or not with pattern
        return self.data[self.data[columnToAnalize].
                         str.contains(pattern, regex=True) 
                         == self.goods].append(self.checkNull(columnToAnalize))
    
    
    """
    Checking for data in list reference
    """
    def checkListReference(self, listname, columnToAnalize):   
        listref = pd.read_csv(listname,
                       delimiter = self.delimiter,
                       encoding = encoding)
        
        return self.data[self.data[columnToAnalize].
                         isin(list(listref['job']))
                         == self.goods]
        

    """
    Checking for email structure
    """
    def checkEmail(self, columnToAnalize):
        return self.checkPattern(columnToAnalize, '[\w]+@[\w]+.com')
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

