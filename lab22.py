#Write a Python program to multiplies all the items in a list. 
def multiply_list(items):
    tot = 1
    for i in items:
        tot *= i
    return tot
print(multiply_list([4,8,12,34]))