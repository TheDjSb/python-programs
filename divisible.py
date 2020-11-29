#Wap to check whether a no. is divisible by 3 & 5.

num=int(input("Enter a number:"))
if num%3==0:
  print("It is divisible by 3.")
elif num%5==0:
  print("It is divisible by 5.")
else:
  print("It is not divisible by 3 & 5.")
