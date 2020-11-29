
def binary_search(alist, key):

    start = 0
    end = len(alist)
    while start < end:
        mid = (start + end)//2
        if alist[mid] > key:
            end = mid
        elif alist[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1
 
 
alist = [1,2,2,5,4,12,15,14,19,41,8,23,]
key = int(input('The number to search for: '))
 
index = binary_search(alist, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))