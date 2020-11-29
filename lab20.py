#Python program to check whether the area of rectangle is greater than, less than or equal to its perimeter.

height =float(input("Enter the height of the rectangle :"))
width =float(input("Enter the width of the rectangle :"))

Area = width * height
print(Area)
perimeter= 2 * (width + height) 
print(perimeter)
if(Area==perimeter):
       print("Both Area  :{0} and perimeter: {1} are equal".format(Area,perimeter))
elif(Area<perimeter):
    print("Perimeter is largest :{0} >2 {1} than Area".format(perimeter,Area))
elif(Area>perimeter):
    print("Area is Largest :{0} > {1} than Perimeter".format(Area,perimeter))
else:
    print("Please Enter Valid Number")