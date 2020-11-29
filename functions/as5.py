lis = [{ "name" : "Subarna", "age" : 20},{ "name" : "krishna", "age" : 20 },          
{ "name" : "ashim" , "age" : 19 },{ "name" : "Ritik", "age" : 18 }] 

print ("The list printed sorting by age and name: ")
print (sorted(lis, key = lambda i: (i['age'], i['name'])))