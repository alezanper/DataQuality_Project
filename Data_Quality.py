# -*- coding: utf-8 -*-
"""
Created on Sun Sep 01 13:00:15 2018

@author: alezanper
"""

import pandas as pd 

encoding = 'iso-8859-1'

class Rules:
    
    data = pd.DataFrame()
    counter = 0
    
    """
    Loading file into dataframe
    """
    def __init__(self, filename, delimiter):
        #Creating Dataframe
        self.data = pd.read_csv(filename,
                       delimiter = delimiter,
                       encoding = encoding)
        
        # Size of dataframe
        self.counter = (self.data).shape[0]

    """
    Checking for pattern
    """
    def checkPattern(self, columnToAnalize, pattern, goods):
        #Checking pattern and returning data that match or not match with pattern
        return self.data[self.data[columnToAnalize].
                         str.contains(pattern, regex=True) == goods]
        

