#Positive indexing and Negative Indexing 

pos = [10, -21, 4, -45, 66, -93, 1]   
pos_count, neg_count = 0, 0 
# iterating each number in list 
for num in pos: 
         # checking condition 
    if num >= 0: 
        pos_count += 1
  
    else: 
        neg_count += 1
          
print("Positive numbers in the list: ", pos_count) 
print("Negative numbers in the list: ", neg_count) 


#chnage value of items using positions

list =["ritik","subarna","pranish"]
list[1] = ["subarna"]
print(list)