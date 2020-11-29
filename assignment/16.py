# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 01:12:26 2020

@author: Subarna Basnet
"""
"""16.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity. Suppose, one unit will cost 100. Check and print total cost for user."""
print ("Enter quantity")
quantity = int(input())
if quantity*100 > 1000:
  print ("Cost is",((quantity*100)-(.1*quantity*100)))
else:
  print ("Cost is",quantity*100)
				
