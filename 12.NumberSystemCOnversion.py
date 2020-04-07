#Octal- base 8- 0 to 7
#HexaDecimal- base 16- 0 to 9  and a-f

#It will print 0b11001
print(bin(25))

#It will print 0o31
print(oct(25))

#It will print 0x19
print(hex(25))

# It will print 25
print(0x19)

#Swap 2 variables in python
a=int(input("Enter the first number: "))
b=int(input("ENter the second number: "))

temp=a
a=b
b=temp
print("Value of a is ",a)
print("Value of b is ",b)

#Swap 2 numbers in another way
x=5
y=6
x=x+y  #x=5+6=11
y=x-y  #y=11-6=5
x=x-y  #x=11-5=6

#Swap 2 numbers in another way. XOR will not waste extra bit. Caret sign  ^ is used for XOR.

x=5
y=6
x=x^y  #x=5+6=11
y=x^y  #y=11-6=5
x=x^y  #x=11-5=6

#Swap 2 numbers in another way.
a1=10
b1=20
a1,b1=b1,a1
print(a1)
print(b1)