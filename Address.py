# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 10:12:17 2018

@author: alezanper
"""
import re

class address:
    
    addressParts = []
    addressTokens = []    
    
    urbanBlock = []
    
    l = 0;
    
    """
    Starting class    
    """    
    def __init__(self, addr):
        self.extractParts(addr)
        self.l = len(self.addressParts)
        self.extractTokens()
        self.createUrbanBlock()

        
    """
    Function for cleaning address and create vector to work with.
    """
    def extractParts(self, addr):
        addrClean = addr
        for i in range(len(self.badTokens)):
            addrClean = (addrClean.replace(self.badTokens[i], ' '))
        self.addressParts = addrClean.upper().split()
        
    """
    Function for getting token from an address part.
    """
    def getToken(self, part):
        if part in self.urban:
            return 'U'
        elif part in self.prop:
            return 'P'
        elif re.match('^[A-ZÑ]+$', part):
            return '+'
        elif re.match('^[0-9]+$', part):
            return '^'
        elif re.match('^[0-9]+[A-ZÑ]+$', part):
            return '>'
        elif re.match('^[A-ZÑ]+[0-9]+$', part):
            return '<'
        else: return part
        
    """
    Function for translating address to tokens.
    """
    def extractTokens(self):
        for i in range(self.l):
            self.addressTokens.append(self.getToken(self.addressParts[i]))
            

    """
    """
    
    def createUrbanBlock(self):
        for i in range(self.l):
            if self.addressTokens[i] != 'P':
                self.urbanBlock.append(self.addressParts[i])  
            else: break;
    
    
    def getUrbanBlock(self):
        return self.urbanBlock    
    
    def getParts(self):
        return self.addressParts
        
    def getTokens(self):
        return self.addressTokens; 
    
    badTokens = [';', ',', '$', ':', '.', '@', '#', '!', '%']
    
    urban = {'CL': 'CL',
             'CALLE': 'CL',
             'CAL': 'CL',
             'CARRERA': 'CR',
             'CR': 'CR',
             'DG': 'DG',
             'DIAGONAL': 'DG',
             'DIAG': 'DG'}
    
    prop = {'APT': 'APT',
            'APARTAMENTO': 'APT',
            'CS': 'CS',
            'CASA': 'CS',
            'ED': 'ED',
            'EDIFICIO': 'ED',
            'EDIFI': 'ED',
            'MANZANA': 'MZ',
            'MZ': 'MZ'}
        
        
        
