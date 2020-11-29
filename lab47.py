

#Write a Python program to sort a list of elements using the selection sort algorithm

import sys 
A = [2,12,5,12,14,36,129,78,55,31,10,5] 

for i in range(len(A)): 
      
 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
              
        
    A[i], A[min_idx] = A[min_idx], A[i] 
  

print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %A[i]),  