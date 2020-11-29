# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 00:49:53 2020

@author: Subarna Basnet
"""
"""13.	Take 3 inputs from user and check :
(i) all are equal
(ii) any of two are equal	( use and or )"""

print('Enter First Number')
fn=int(input())
print('Enter Second Number')
sn=int(input())
print('Enter Third Number')
tn=int(input())

if fn==sn==tn:
    print('All are Equal')
elif fn==sn:
    print('First and second are equal')
elif sn==tn:
    print('Second and third are equal')
elif fn==tn:
    print('First and third are equal')
else:
    print('All are not equal')
