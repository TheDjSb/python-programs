# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 02:08:14 2020

@author: Subarna Basnet
"""
"""28.Find largest and smallest elements of a list."""
a = [2,312,123,3,12,23,12,12]
largest = a[0]
i = 0
while i<len(a):
  if a[i]>largest:
    largest = a[i]
  i = i+1
print ('Largest is :',largest)

smallest = a[0]
j = 0
while i>len(a):
  if a[i]>smallest:
    largest = a[i]
  i = i+1
print ('Smallest is :',smallest)