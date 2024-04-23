""" Program to implement bubble sort using recursion """

def bubblesort(n,length):
    for i in range(length-1):
        if n[i] > n[i+1]:
            n[i],n[i+1] = n[i+1],n[i]
        if length - 1 > 1:
            bubblesort(n,length-1)


a = [2,1,4,8,5,3]
length= len(a)
bubblesort(a,length)
print(a)