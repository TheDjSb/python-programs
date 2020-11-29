# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 02:28:57 2020

@author: Subarna Basnet
"""
"""
32.	Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists. E.g.-
INITIAL list :
58	24	13	15	63	9	8	81	1	78
After spliting :
58	24	13	15	63
9	8	81	1	78

"""
a = [58,24,13,15,63,9,8,81,1,78]
print('original list:',a)
print ('first half',a[:len(a)//2])
print ('second half',a[len(a)//2:])
