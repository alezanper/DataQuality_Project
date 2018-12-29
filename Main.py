# -*- coding: utf-8 -*-
"""
@author: alezanper
"""
import Address


mAddress = Address.address('calle 45. 56a carrera 56 67 ,,,')
                           
print(mAddress.getParts())
print(mAddress.getTokens())

