#array() linspace() logspace() arrange() zeros() ones()
from numpy import *
arr=array([1,2,3,4,5])

print(arr.dtype)

arr1=array([1,2,3,4.5])
print(arr1.dtype)

#It explictly converts an integer array to float
arr3=array([1,2,3],float)
print(arr3.dtype)


# no of parts. it will break into 10 parts
arr4=linspace(0,16,10)
print(arr4)

# it will break as defined in steps 2.
arr5=arange(1,15,2)
print(arr5)

arr6=logspace(1,40,5)
print(arr6)
print('%.2f' %arr6[0])

#Will create an array with default value as 0
arr7=zeros(5,int)
print(arr7)

#Will create an array with default value as 1
arr8=ones(5,int)
print(arr8)