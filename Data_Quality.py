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
    Checking for pattern
    """
    def checkPattern(self, columnToAnalize, pattern):
        #Checking pattern and returning data that match or not with pattern
        return self.data[self.data[columnToAnalize].
                         str.contains(pattern, regex=True) 
                         == self.goods]
    
    
    """
    Checking for data in list reference
    """
    def inListReference(self, listname, columnToAnalize):   
        listref = pd.read_csv(listname,
                       delimiter = self.delimiter,
                       encoding = encoding)
        
        return self.data[self.data[columnToAnalize].
                         isin(list(listref['job']))
                         == self.goods]
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

