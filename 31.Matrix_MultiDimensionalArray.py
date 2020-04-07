from numpy import *
arr1=array([
    [1,2,3],[4,5,6]
])

print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

print("======================================================")
print("How to convert a 2 dimension array to 1 dimension array")
arr2=arr1.flatten()
print(arr2)

print("======================================================")
print("How to convert a 2 dimensional array to 3 dimenional array")
arr3=array([
            [1,2,3,4,5,6],
            [7,8,9,10,11,12]
])

arr4=arr3.reshape(3,4)
print(arr4)

print("======================================================")
print("It will create 2 two dimnsiuon arrays. In each 2 dimension array we will have 2 rows & 3 colums")
arr5=arr3.reshape(2,2,3)
print(arr5)

print("======================================================")
Print("Program for convering a 2D array into  Matrices")

arrexample=array([
            [1,2,3,4,5,6],
            [7,8,9,10,11,12]
])

m= matrix





print(m)