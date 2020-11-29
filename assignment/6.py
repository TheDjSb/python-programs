# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:56:57 2020

@author: Subarna Basnet
"""
"""6.Write a program to print triangle in python. (pattern) """

print("Program to print half pyramid: ");
data = 4

for i in range (0, data):
    for j in range(0, i + 1):
        print("*", end=' ')

    print("\r")

print("Program to print half pyramid: ")

data2 = 5


for i in range (data2,0,-1):
    for j in range(0, i + 1):
        print("*", end=' ')

    print("\r")
    
print("Program to print half pyramid: ")

data3 = 5

for i in range (data3,0,-1):
    for j in range(0, i + 1):
        print(j, end=' ')

    print("\r")  
    
print("Program to print half pyramid: ")

data4 = 4

for i in range (0,data4):
    for j in range(0, i + 1):
        print(j, end=' ')

    print("\r")       
         
    

    