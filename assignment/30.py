# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 02:23:06 2020

@author: Subarna Basnet
"""
"""30.	Write a program to check if elements of a list are same or not it read from front or back. E.g.-
2	3	15	15	3	2
"""

a = [1,2,3,3,2,1]
i = 0
mid = (len(a))/2
same = True
while i<mid:
  if a[i] != a[len(a)-i-1]:
    print ("Elements of list are not same")
    same = False
    break
  i = i+1
if same == True:
  print ("Elements of list are same",a)
