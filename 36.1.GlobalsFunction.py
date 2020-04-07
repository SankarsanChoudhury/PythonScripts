#using globals() function we can access the global variable address
a=10
print(id(a))

def something():
    a=9

    x=globals()['a']  # when we mention globals(), it will return all the global variable.Here we need only address of a.
    print(id(x))
    print("Initial value of a is: ",x)
    print("in fun",a)

    globals()['a']=15   #Here we are changing the global variable without affecting local variable
something()

print("outside",a)