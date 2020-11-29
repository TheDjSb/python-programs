#	Write a Python program to print a dictionary in table format.



dict1 = {} 
  

dict1 = {(0, 0): 'Subarna', (0, 1): 20, (0, 2): 'B-tech CSE', 
         (1, 0): 'Krishna', (1, 1): 20, (1, 2): 'B-tech MSE', 
         (2, 0): 'Ashim', (2, 1):19, (2, 2): 'B-Tech GSE'
} 
  

print(" NAME ", " AGE ", "  COURSE " ) 
  

for i in range(3): 
      
    for j in range(3): 
        print(dict1[(i, j)], end ='   ') 
          
    print() 