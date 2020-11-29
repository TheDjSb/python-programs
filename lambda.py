 
test_tup1 = (10, 4, 5) 
test_tup2 = (2, 5, 18) 
  
print("The original tuple 1 : " + str(test_tup1)) 
print("The original tuple 2 : " + str(test_tup2)) 
  
res = tuple(map(lambda i, j: i + j, test_tup1, test_tup2)) 
  

print("sum : " + str(res)) 