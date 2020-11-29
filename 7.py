
import math 
pi = math.pi 
  

def volume(r): 
    vol = (4 / 3) * pi * r * r * r 
    return vol 

def surfacearea(r): 
    sur_ar = 4 * pi * r * r 
    return sur_ar 
  
radius = float(5) 
print( "Volume Of Sphere : ", volume(radius) ) 
print( "Surface Area Of Sphere : ", surfacearea(radius) ) 