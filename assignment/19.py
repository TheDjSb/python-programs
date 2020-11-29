# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 01:22:06 2020

@author: Subarna Basnet
"""
"""19.	A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
(i) Number of classes held
(ii) Number of classes attended.
And print percentage of class attended. Is student is allowed to sit in exam or not."""


print ("Number of classes held")
noh = int(input())
print ("Number of classes attended")
noa = int(input())
atten = (noa/float(noh))*100
print ("Attendence is",atten)
if atten >= 75:
  print ("You are allowed to sit in exam")
else:
  print ("Sorry, you are not allowed. Attend more classes from next time.")

