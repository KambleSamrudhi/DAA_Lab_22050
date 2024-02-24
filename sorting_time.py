import time
import random

def InsertionSort(array,n):
    #array[0]=int(input("Enter the first element in the array:"))
    for i in range(1,n):
        #key=int(input("Enter the element to be inserted:"))
        j=i-1
        key=array[i]
        while(int(j)>=0 and array[j]>key):
            array[j+1]=array[j]
            j=j-1
            array[j+1]=key

    return array
print()
print("Insertion Sort:")
print()
no_elements=int(input("Enter the no. of elements:"))
array=[]
for i in range(no_elements):
    array.append(random.randint(0,10000))
start=time.time()
ISort=InsertionSort(array,no_elements)
end=time.time()
print("Sorted array:",ISort)
print("Time taken:",(end-start),"s")


def SelectionSort(A,n):
    for i in range(0,n):
        Max=A[0]
        pos=0
        for j in range(0,n-i):
            if A[j]>=Max:
                Max=A[j]
                pos=j
        A[pos]=A[n-i-1]
        A[n-i-1]=Max
    return A
print()
print("Selection Sort:")
print()
no_elements=int(input("Enter the no. of elements:"))
#array=eval(input("Enter the elements in the array:"))
array=[]
for i in range(no_elements):
    array.append(random.randint(0,10000))
start=time.time()

SSort=SelectionSort(array,no_elements)
end=time.time()

print("Sorted array:",SSort)
print("Time taken:",(end-start),"s")



def BubbleSort(A,n):
    for i in range(0,n):
        for j in range(0,n-1-i):
            if(A[j]>A[j+1]):
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp
    return A
print()
print("Bubble Sort:")
print()
no_elements=int(input("Enter the no. of elements:"))
#array=eval(input("Enter the elements in the array:"))'''
array=[]
for i in range(no_elements):
    array.append(random.randint(0,10000))

start=time.time()

BSort=BubbleSort(array,no_elements)
end=time.time()

print("Sorted array:",BSort)
print("Time taken:",(end-start),"s")
        
