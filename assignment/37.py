# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 03:22:27 2020

@author: Subarna Basnet
"""
"""37.	Using range(1,101), make two list, one containing all even numbers and other containing all odd numbers."""

even=[]
odd=[]
for i in range(1,101):
  if i%2 == 0:
    even.append(i)
  else:
    odd.append(i)

print(even)
print(odd)