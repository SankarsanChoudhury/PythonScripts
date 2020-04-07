num=5

#id() is used to find the address
print(id(num))

a=10
b=a

#Since both a and b are having the same value, the address will be same. Here a,b are addressing to 10
print(id(a))
print(id(b))
print(id(10))

PI=3.14
print(type(PI))
num=10
print(type(num))