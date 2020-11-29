# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 03:03:54 2020

@author: Subarna Basnet
"""
"""35.	Write a program to make a new string with all the consonents deleted from the string "Hello, have a good day"."""
a = ['a','e','i','o','u','A','E','I','O','U',' ']
b = "Hello, have a good day"
print(b)
for i in b:
  if i not in a:
    b = b[:b.index(i)]+b[b.index(i)+1:]
print ('only Vowels :',b)