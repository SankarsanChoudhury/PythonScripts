from functools import reduce


#Program1 for filter() function
def is_even(n):
    return n%2==0


nums=[1,2,3,4,5,6,7,8]
evens=list(filter(is_even,nums))   #first parameter is the function & 2nd parameter is sequence
print(evens)

#----------------------lambda function-----------------------------------------
nums1=[11,22,33,44,55,66,77,88]
evens1=list(filter(lambda n:n%2==0,nums1))
print(evens1)

#-------------------------map() function--Find the even numbers and add 2 to the numbers----------------------------
#def update(n):
    #return n+2


nums2=[11,22,33,44,55,66,77,88]
evens2=list(filter(lambda n:n%2==0,nums2))

doubles=list(map(lambda  n:n+2,evens2))

print(doubles)
#------------------------------------------reduce()----------------------------

#def add_all(a,b):
    #return a+b


nums3=[11,22,33,44,55,66,77,88]
evens3=list(filter(lambda n:n%2==0,nums3))

doubles1=list(map(lambda  n:n+2,evens3))

sum=reduce(lambda a1,b1:a1+b1,doubles1)
print(sum)