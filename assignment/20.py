# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 01:25:24 2020

@author: Subarna Basnet
"""
"""20.Write a program to check if a year is leap year or not. If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400."""
year = int(input("Please Enter the Year Number you wish: "))

if (year%400 == 0):
          print("%d is a Leap Year" %year)
elif (year%100 == 0):
          print("%d is Not the Leap Year" %year)
elif (year%4 == 0):
          print("%d is a Leap Year" %year)
else:
          print("%d is Not the Leap Year" %year)
