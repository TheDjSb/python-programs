# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 01:34:32 2020

@author: Subarna Basnet
"""
"""22.A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one. E.g.-
INPUT : 1234        OUTPUT : 4321
INPUT : 5982        OUTPUT : 2895
"""

num = int(input("Enter a number: "))
reverse_num = 0
while(num>0):
  remainder = num % 10
  reverse_num = (reverse_num * 10) + remainder
  num = num//10
print("The reverse number is : {}".format(reverse_num))