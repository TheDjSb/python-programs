import math
def area(a1,b1,c1,a2,b2,c2):
    area  = math.sqrt((b1 * c2 - b2 * c1) ** 2+(a1 * c2 - a2 * c1) ** 2 +(a1 * b2 - a2 * b1) **2)
    
    return area

def main():
     a1=2
     b1=1
     c1=5
     a2=6
     b2=-2
     c2 =3
     
     a= area(a1,b1,c1,a2,b2,c2)
     print("Area of Parallelogram =",a)
     
     
main()