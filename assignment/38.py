# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 03:24:06 2020

@author: Subarna Basnet
"""

"""38.From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists."""
even=[]
odd=[]

for i in range(1,101):
  if i%2 == 0:
    even.append(i)
  else:
    odd.append(i)
    

final=[]
for j in even:
    if (j%4==0) or (j%6==0) and (j%8==0) or (j%10==0) or (j%3==0) or (j%5==0) or (j%7==0) or (j%9==0):
        final.append(j)  
for j in odd:
    if (j%4==0) or (j%6==0) and (j%8==0) or (j%10==0) or (j%3==0) or (j%5==0) or (j%7==0) or (j%9==0):
        final.append(j)           
        
print('No divisible by:',final)
#print('No of divisible by 6:',six)