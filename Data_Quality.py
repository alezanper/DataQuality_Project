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
    delimiter = ','
    parts = []
    
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
#    def checkNull(self, columnToAnalize):
#        #Checking for null values
#        return self.data[self.data[columnToAnalize].isna()
#                         == (not self.goods)]
        
    def checkNull(self, columnToAnalize):
        print(self.parts)
        print(len(self.parts))
        
        for i in range(len(self.parts)):
            dataPart = self.getDataFrame(self.parts[i])            
            self.data = self.data.append(dataPart[dataPart[columnToAnalize].isna()
                         == (not self.goods)])
        return self.data
    

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
                       encoding = self.encoding)
        
        return self.data[self.data[columnToAnalize].
                         isin(list(listref['job']))
                         == self.goods]
        

    """
    Checking for email structure
    """
    def checkEmail(self, columnToAnalize):
        return self.checkPattern(columnToAnalize, '[\w]+@[\w]+.com')
        
    
#print(Rules.split('','people.csv', 20))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

