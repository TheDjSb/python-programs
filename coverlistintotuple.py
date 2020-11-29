#change tuple value 

list = [('A', 2), ('B', 4), ('c', 6)] 
  
x = [item for t in list for item in t] 
var=tuple(list)
print(var) 