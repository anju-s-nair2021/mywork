""" Program To Find A Value from a List """

def binary_search(list_1,number,low,high):
    """ Return index of search number """
    if high >= low:
        mid = (low+high) // 2
        if list_1[mid] == number:
            return mid
        elif list_1[mid] > number:
            return binary_search(list_1,number,low,mid-1)
        elif list_1[mid] < number:
            return binary_search(list_1,number,mid+1,high)
    else:
        return False


# Main Program
list = [1,2,5,7,9]
find = 1
low=0
max1 = len(list)-1
index = binary_search(list,find,low,max1)
if index is False:
    print("invalid element")
else:
    print(f"{find} is present at index {index}")