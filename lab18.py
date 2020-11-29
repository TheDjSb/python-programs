#Python Program  To Print All Integers That Aren’t Divisible By Either 2 Or 3 And Lie Between 1 And 50  
v=0
for i in range(0,51):

    if(i%2!=0 and i%3!=0):

        print(i)
    