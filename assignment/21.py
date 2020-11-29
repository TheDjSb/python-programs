# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 01:29:57 2020

@author: Subarna Basnet
"""
"""21.Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
(i) if employee is female, then she will work only in urban areas.
(ii) if employee is a male and age is in between 20 to 40 then he may work in anywhere
(iii) if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
And any other input of age should print "ERROR"."""

print ("Enter age")
age = int(input())
print ("SEX? (M or F)")
sex = input()
print ("MARRIED? (Y or N)")
marry = input()
if sex == "F" and age>=20 and age<=60:
  print ("Urban areas only")
elif sex == "M" and age>=20 and age<=40:
  print ("You can work anywhere")
elif sex == "M" and age>40 and age<=60:
  print ("Urban areas only")
else:
  print ("ERROR")

