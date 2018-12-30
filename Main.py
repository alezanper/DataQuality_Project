# -*- coding: utf-8 -*-
"""
@author: alezanper
"""
import Address


mAddress = Address.address('calle 56a carrera 56 67 apartamento 345,,edificio la curuña,')
                           
print(mAddress.getParts())
print(mAddress.getTokens())

