#0 1 1 2 3 5 8 13 21 34
#we have to add the last number & 2nd last numbber to get a new number

def fib(n):
    a=0
    b=1

    if n==1:
        print(a)
    elif n<=0:
        print("Please enter a number which is greater than or equal to 1")
    else:
       print(a)
       print(b)

       for i in range(2,n):
          c=a+b
          a=b
          b=c
          print(c)

fib(5)