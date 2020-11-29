# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 02:17:05 2020

@author: Subarna Basnet
"""
"""29.Write a program to print sum, average of all numbers, smallest and largest element of a list."""

a = [2,312,123,3,12,23,12,12]
sumx=0
for item in a:
  sumx = sumx + item
#6
print("sum of all elements : ",sumx)


av=sumx/len(a)
print('Average of list is :',av)

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