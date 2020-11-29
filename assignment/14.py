# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 01:01:10 2020

@author: Subarna Basnet
"""
"""14.Take two number and check whether the sum is greater than 5, less than 5 or equal to 5."""
print('Enter first Number')
a=int(input())
print('Enter Second Number')
b=int(input())
c=a+b
print('sum is:',c)
if c>5:
    print('Sum is greater than 5')
elif c<5 :
    print('Sum is less than 5')
elif c==5:
    print('Sum is equal to 5')

