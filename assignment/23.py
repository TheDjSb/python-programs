# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 01:45:46 2020

@author: Subarna Basnet
"""
"""23.A three digit number is called Armstrong number if sum of cube of its digit is equal to number itself.
E.g.- 153 is an Armstrong number because (13)+(53)+(33) = 153.
Write all Armstrong numbers between 100 to 500.
"""
num = int(input("Enter a number: "))  
sum = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")  
