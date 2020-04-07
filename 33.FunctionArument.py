#integer & string are immutable in python.

def update(x):
    print(id(x))

    x=8
    print(id(x))
    print("X: ", x)

a=10
print(id(a))
update(a)
print("a: ",a)