# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:02:59 2020

@File by : Subarna Basnet
"""
""" 1.Write a python script to sort (ascending and descending) a dictionary by value"""

data={'System ID':2019008144,'Roll No':190101306,'Sem':2,'Year':2020}  
l=list(data.values())             
print("Dictionary",l)   
l.sort()   
print('Ascending order is',l) 
l=list(data.values())
l.sort(reverse=True) 
print('Descending order is',l)


