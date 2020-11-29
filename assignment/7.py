# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 00:13:09 2020

@author: Subarna Basnet
"""
"""7.write a program to print star patterns and alphabets pattern """
print("Print Alphabets  pattern in python ")
lNumber = 6
asciiNumber = 65
for i in range(0, lNumber):
    for j in range(0, i+1):
        character  = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber+=1
    print(" ")
    

print("Program to print star pattern pyramid: \n");

data6 =4
for i in range (0, data6):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range (data6, 0, -1):
    for j in range(0, i -1):
        print("*", end=' ')
    print("\r")