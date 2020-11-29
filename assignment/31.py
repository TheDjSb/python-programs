# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 02:26:12 2020

@author: Subarna Basnet
"""
"""31.	Make a list by taking 10 input from user. Now delete all repeated elements of the list.
E.g.-
INPUT : [1,2,3,2,1,3,12,12,32]
OUTPUT : [1,2,3,12,32]
"""

a = [1,2,3,2,1,3,12,12,32]
print(a)
a = list(set(a))
print ('After deleting same elements:',a)