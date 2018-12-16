# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 10:12:17 2018

@author: alezanper
"""

class address:
    
    addressParts = []
    addressTokens = []
    
    def __init__(self, addr):
        self.extractParts(addr)
    
    def extractParts(self, addr):
        addrClean = addr
        for i in range(len(self.badTokens)):
            addrClean = (addrClean.replace(self.badTokens[i], ' '))
        self.addressParts = addrClean.upper().split()
        
    def getParts(self):
        return self.addressParts;
        
    
    
    badTokens = [';', ',', '$', ':']
        
        
        
