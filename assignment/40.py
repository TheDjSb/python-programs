# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 03:39:58 2020

@author: Subarna Basnet
"""
"""
40.	Take a list containing only strings. Now, take a string input from user and rearrange the elements of the list according to the number of occurrence of the string taken from user in the elements of the list.
E.g.-LIST : ["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
STRING TAKEN : "bug"
OUTPUT LIST:["bug bun bug bun bug bug","buggy bug bug buggy","bunny bug","no bun"]
"""
a = ["apple banana apple banana","banana apple banana","banana banana","apple apple apple banana","no banana"]
print(a)
print('Enter any word to rearrange')
b = input()
c = {}
for i in a:
  count = 0
  for j in i.split():
    if j == b:
      count = count+1
  c[count]=i
d = []
for s in sorted(c):
  d.append(c[s])
d.reverse()
print (d)
