# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:45:31 2020

@author: Subarna Basnet
"""
"""3.Write a Python program to iterate over dictionaries using for loops."""
data = {'A': 10, 'B': 20, 'C': 30} 
for dict_key, dict_value in data.items():
    print(dict_key,'->',dict_value)
    