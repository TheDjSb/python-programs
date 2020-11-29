#Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included). 

def my_function(n):
    list1=[]
    for i in range(1,n):
        a=i*i
        list1.append(a)
    print(list1)
        
my_function(30)