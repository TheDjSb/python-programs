# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:00:44 2020

@author: NotYourPc
"""


import math 
pi = math.pi 
  
def volume(r, h): 
    vol = pi * r * r * h 
    return vol 
  
def totalsurfacearea(r, h): 
    tsurf_ar = (2 * pi * r * h) + (2 * pi * r * r) 
    return tsurf_ar 
  

r = 8
h = 5

print("Volume Of Cylinder   =  ",volume(r, h)) 
print(" Surface Area  Of Cylinder =  ",totalsurfacearea(r,h)) 

