from numpy import *

arr1=array([1,2,3])
arr2=arr1+5
print(arr2)

arr3=array([2,3,4])
result=arr1+arr3
print(result)

print(sqrt(result))
print(min(result))
print(max(result))
print(sort(result))
#print(concatenate([arr1,arr3])


#Here both arr3 & arr4 will be having same address
arr4=arr3
print(id(arr3))
print(id(arr4))

#Copying an array

arr5=arr3.view()
print("Program for shallow copy")
print(arr3)
print(arr5)
#If you copy an array using shallow copy then if you assign a value in one array then same value will be applied to the copied array
#Here 7 will be applied to both arr3 & arr5
arr3[0]=7
print(arr3)
print(arr5)
#-------------------------------------------------------
print("Program for deep copy")

arr6=arr3.copy()
arr3[0]=5
print(arr3)
print(arr6)