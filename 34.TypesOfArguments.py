def add_sub(a,b):
    add=a+b
    sub=a-b
    print(add)
    print(sub)

add_sub(5,4)
result=add_sub(3,2)

#It will print None as the function does not return anything
print(result)

print("Program to write a function which returns some data")

def mul_div(a1,b1):  #Formal Arguments
    mul=a1*b1
    div=a1/b1
    return mul,div

mul_div(5,4)
result1,result2=mul_div(3,2)   #Actual Arguments
print(result1)
print(result2)