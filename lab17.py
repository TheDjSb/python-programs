#	Write a program to print the following series 12+22+.........................+102

 
number = int(input("Please Enter any Positive Number  : "))
total = 0

total = (number * (number + 1) * (2 * number + 1)) / 6

print("The Sum of Series upto {0}  = {1}".format(number, total))