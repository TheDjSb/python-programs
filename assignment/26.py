# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 02:20:04 2020

@author: Subarna Basnet
"""
"""26.Write a program to find the product of all elements of a list."""
my_list = []
#2
for i in range(1,4):
  my_list.append(i)
#3
print(my_list)
#4
result = 1
#5
for item in my_list:
  result = result * item
#6
print("product of all elements : ",result)
