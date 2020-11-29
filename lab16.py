"""Python program to print all odd numbers in a range"""

start, end = 4, 19
  

for num in range(start, end + 1):     
   
    if num % 2 != 0: 
        print(num, end = " ") 
        
        