# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 01:47:59 2020

@author: Subarna Basnet
"""
"""24.Take 10 integer inputs from user and store them in a list. Again ask user to give a number. Now, tell user whether that number is present in list or not.
( Iterate over list using while loop ).
"""
i = 10
a = []
while i>0:
  print ("Enter 10 numbers")
  num = input()
  a.append(num)
  i = i-1
print ("Enter a number to check is in list or not")
n = input()
i = 9
count = 0
while i>=0:
  if n == a[i]:
    print ("Yes its present in list")
    count = count + 1
  i = i-1
if count == 0:
  print ("No it dos not present in list")


