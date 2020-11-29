
#Write a Python function to find the Max of three numbers.

def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )

print("The Max of three is :",max_of_three(3, 6, -5))