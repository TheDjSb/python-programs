#31.	 Write a Python program to replace last value of tuples in a list
#Sample list: [(30, 50, 70), (40, 60, 80), (70, 20, 90)]



num1 = [(30,50,70),(40,60,80),(70,20,90)]
num2 = [(20,30,40)]
num1[-1:] = num2
print(num1)