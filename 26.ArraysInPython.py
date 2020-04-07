#All the data should be of same type
#Arrays in Python dont have specific size. SO you can expand it as per your wish.

#import array as arr
from array import *

#Here we have created an array() and assigned it to vals
#When we mention the data type , the memory size is defined based on the data type
#Here i is the address
vals=array('i',[5,9,8,4,2])

#It will print array('i', [5, 9, 8, 4, 2])
print(vals)

#It will throw an error as we can't inject float value inside integer type.TypeError: integer argument expected, got float
#vals1=array('i',[5,9,8.5,4.3,2])

#It will print array('i', [5, 9, -8, -4, 2]) as i stands for signed integer
vals2=array('i',[5,9,-8,-4,2])
print(vals2)

#It will throw an error stating -OverflowError: can't convert negative value to unsigned int
#vals4=array('I',[5,9,-8,-4,2])

#buffer_info() gives you the sise of your array
#It will print (15652096, 5)
print(vals2.buffer_info())

print(vals2.typecode)

print(vals2.reverse())

print(vals2)

for i in range(len(vals2)):
    print(vals2[i])

print(vals2[0])


#It will print characters - array('u', 'sank')
vals3=array('u',['s','a','n','k'])
print(vals3)

#Creating a new array from an old array
newArr=array(vals.typecode, (a for a in vals))
newArr1=array(vals.typecode, (a*a for a in vals))
print(newArr)
print(newArr1)

#while loop in array
i=0                   #initialisation
while i<len(newArr1):  #condition
    print(newArr1[i])
    i=i+1
