# -*- coding: utf-8 -*-
"""
Created on Sun Sep 01 13:00:15 2018

@author: alezanper
"""

import pandas as pd 
import itertools


class Rules:  
    
    encoding = 'iso-8859-1'    
    data = pd.DataFrame()   # Data to work with
    counter = 0             # Size of dataFrame
    goods = False           # False for return bad registers
    delimiter = ','         # Default delimiter
    parts = []              # part from split function
    
    
    """
    Loading file into dataframe
    """
    def __init__(self, filename, delimiter, goods):
        self.goods = goods
        self.delimiter = delimiter
        self.parts = self.split(filename, 70)
#        self.data = pd.read_csv(filename,
#                       delimiter = delimiter,
#                       encoding = encoding)        
#       self.counter = (self.data).shape[0]

    
    """
    It takes 
    """
    def getDataFrame(self, filename):
        data = pd.read_csv(filename,
                       delimiter = self.delimiter,
                       encoding = self.encoding)
        return data
    
    """
    Split
    """
    def split(self, filename, numLines):
        parts = []
        with open(filename, encoding = self.encoding) as f:
            file = f.readlines()
            size = len(file)
            
            for i in range(int(size/numLines)+1):
                with open('part_' + str(i) + '_' + filename, "w", encoding = self.encoding) as csv:
                    parts.append('part_' + str(i) + '_' + filename)
                    csv.write(''.join(list(itertools.islice(file, 0, 1))))
                    csv.write(''.join(list(itertools.islice(file, 1, numLines)))) if (i == 0) else csv.write(''.join(list(itertools.islice(file, numLines*i, numLines + numLines*i))))
        return parts
        
    """
    Checking for null values
    """
    def checkNulls(self, columnToAnalize):
        #Checking for null values
        return self.data[self.data[columnToAnalize].isna()
                         == (not self.goods)]
    
    
    """
    """        
    def checkNull(self, columnToAnalize):
        print(self.parts)
        print(len(self.parts))
        
        for i in range(len(self.parts)):
            dataPart = self.getDataFrame(self.parts[i])            
            self.data = self.data.append(dataPart[dataPart[columnToAnalize].isna()
                         == (not self.goods)])
        return self.data
    

    """
    Checking for pattern
    """
    def checkPattern(self, columnToAnalize, pattern):        
        for i in range(len(self.parts)):
            dataPart = self.getDataFrame(self.parts[i])            
            self.data = self.data.append(
                    dataPart[dataPart[columnToAnalize].str.contains(pattern, regex=True) 
                         == self.goods].append(dataPart[dataPart[columnToAnalize].isna()
                         == (not self.goods)])
                    )   
        return self.data
    
    
    """
    Checking for email structure
    """
    def checkEmail(self, columnToAnalize):
        return self.checkPattern(columnToAnalize, '[\w]+@[\w]+.com')
    
    
    """
    Checking for data in list reference
    """
    def checkListReference(self, listname, listColumn, columnToAnalize):   
        listref = pd.read_csv(listname,
                       delimiter = self.delimiter,
                       encoding = self.encoding)
        
        for i in range(len(self.parts)):
            dataPart = self.getDataFrame(self.parts[i])            
            self.data = self.data.append(
                    dataPart[dataPart[columnToAnalize].isin(list(listref[listColumn]))
                         == self.goods]
                    )  
        
        return self.data
        
       

#    """
#    Checking for unicity
#    """
#    def checkUnity(self, columnToAnalize, maxRepeated):
#        #Checking for null values
#        if(self.goods):
#            return self.data.groupby(columnToAnalize).filter(lambda x: len(x) == 1)
#        else:
#            return self.data.groupby(columnToAnalize).filter(lambda x: len(x) > maxRepeated)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

