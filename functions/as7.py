arrays = [2,5,6,4,3,8,1,7,5,6,9]
print("Given Arrays:")
print(arrays)
oddno = len(list(filter(lambda x: (x%2 != 0) , arrays)))
evenno = len(list(filter(lambda x: (x%2 == 0) , arrays)))
print("\nNumber of even numbers in the above array: ", evenno)
print("\nNumber of odd numbers in the above array: ", oddno)