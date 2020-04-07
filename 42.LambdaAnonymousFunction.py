#Anonymous Function:FUnction without a name which is called lambda
#functions are objects in python

def square(a):
    return a*a

x=5
result=square(x)
print("Square of {} is {}".format(x,result))

#===============================================================
f=lambda b : b*b
result1=f(10)
print(result1)

#==========================================
sum=lambda l, m: l+m
n1=5
n2=10
result2=sum(n1,n2)
print("Sum of {} and {} is {}".format(n1,n2,result2))