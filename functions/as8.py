def power(x, y): 
  
    if (y == 0): return 1
    elif (int(y % 2) == 0): 
        return (power(x, int(y / 2)) *
               power(x, int(y / 2))) 
    else: 
        return (x * power(x, int(y / 2)) *
                   power(x, int(y / 2))) 
  
    

x = int(input("Enter the Number :")); y = int(input("Enter the Power of the Number :"))
print("Ans is :",power(x, y)) 