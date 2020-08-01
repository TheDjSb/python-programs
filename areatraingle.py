#WAP to find area of triangle
a=int(input("First side of triangle:"))
b=int(input("Second side of triangle:"))
c=int(input("Third side of triangle:"))
s=(a+b+c) / 2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle:",area)
