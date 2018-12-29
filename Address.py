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
        self.extractParts(addr)
        self.l = len(self.addressParts)
        self.extractTokens()

        
    """
    Function for cleaning address and create vector to work with.
    """
    def extractParts(self, addr):
        addrClean = addr
        for i in range(len(self.badTokens)):
            addrClean = (addrClean.replace(self.badTokens[i], ' '))
        self.addressParts = addrClean.upper().split()
        
    """
    Function for getting token from a address part.
    """
    def getToken(self, part):
        if re.match('^[A-ZÑ]+$', part):
            return '+'
        elif re.match('^[0-9]+$', part):
            return '^'
        else: return part
        
    """
    Function for translating address to tokens.
    """
    def extractTokens(self):
        for i in range(self.l):
            self.addressTokens.append(self.getToken(self.addressParts[i]))
            
        
    def getParts(self):
        return self.addressParts;
        
    def getTokens(self):
        return self.addressTokens;    
    
    badTokens = [';', ',', '$', ':', '.']
        
        
        
