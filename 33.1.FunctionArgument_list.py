#list is mutable

def update(lst):
    print(id(lst))

    lst[1]=25
    print(id(lst))
    print("X: ", lst)

lst=[10,20,30]
print(id(lst))
update(lst)
print("List: ",lst)