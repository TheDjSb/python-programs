# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 01:16:16 2020

@author: Subarna Basnet
"""
"""17.A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount."""

print ("Enter salary")
salary = int(input())
print ("Enter year of service")
yos = int(input())
if yos>5:
  print ("Bonus is",.05*salary)
else:
  print ("No bonus")