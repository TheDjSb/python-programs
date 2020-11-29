#	Write a Python program to reverse a string.


def reverse(string): 
    string = string[::-1] 
    return string 
  
s = "Shardauniversity"
  
print ("The original string  is : ",end="") 
print (s) 
print ("The reversed string(using extended slice syntax) is : ",end="") 
print (reverse(s)) 