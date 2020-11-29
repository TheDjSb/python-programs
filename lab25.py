#Write a Python program to remove duplicates from a list. 


listi = [1, 3, 5, 6, 3, 5, 6, 1] 
print ("The original list is : " +  str(listi)) 
  
res = [] 
for i in listi: 
    if i not in res: 
        res.append(i)   
print ("The list after removing duplicates : " + str(res)) 