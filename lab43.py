
#	Write a Python function that checks whether a passed string is palindrome or not.
# function which return reverse of a string 
def reverse(s): 
	return s[::-1] 
def isPalindrome(s): 
	rev = reverse(s) 

	if (s == rev): 
		return True
	return False

s = input("enter any word to check palindrome or not")
ans = isPalindrome(s) 

if ans == 1: 
	print("{0} :This is Palindrome".format(s)) 
else: 
	print("{0} :This is not Palindrome".format(s))
