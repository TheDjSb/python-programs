# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:52:27 2020

@author: Subarna Basnet
"""

"""5.Write a Python program to get the maximum and minimum value in a dictionary"""

data = {'A':2015, 'B':2002, 'C': 3900}

m = max(data.keys(), key=(lambda k: data[k]))
mi = min(data.keys(), key=(lambda k: data[k]))

print('Maximum Value: ',data[m])
print('Minimum Value: ',data[mi])