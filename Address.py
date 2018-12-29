# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 10:12:17 2018

@author: alezanper
"""
import re

class address:
    
    addressParts = []
    addressTokens = []    
    l = 0;
    
    """
    Starting class    
    """    
    def __init__(self, addr):
        self.l = len(addr.split())
        self.extractParts(addr)
        
    """
    Function for cleaning address and create vector to work with.
    """
    def extractParts(self, addr):
        addrClean = addr
        for i in range(len(self.badTokens)):
            addrClean = (addrClean.replace(self.badTokens[i], ' '))
        self.addressParts = addrClean.upper().split()
        
    """
    Function for getting tokens from address vector.
    """
    def extractTokens(self):
        for i in range(self.l):
            re.match('[A-ZÑ]+', self.addressParts[i])
            
        
    def getParts(self):
        return self.addressParts;
        
    
    
    badTokens = [';', ',', '$', ':', '.']
        
        
        
