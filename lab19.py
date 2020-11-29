#Python program to accept two no. Check whether 1st no. Is largest, second no. is largest or both are equal.


noa=int(input("Enter first no"))
nob=int(input("Enter second no"))
if(noa==nob):
       print("Both Numbers  {0} and {1} are equal".format(noa,nob))
elif(noa<nob):
    print("Second Number is largest :{0} >2 {1}".format(nob,noa))
elif(noa>nob):
    print("First Number is Largest :{0} > {1}".format(noa,nob))
else:
    print("Please Enter Valid Number")
    