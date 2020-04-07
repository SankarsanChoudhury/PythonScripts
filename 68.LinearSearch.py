def search(list1,n):
    i=0

    while i<len(list1):
        if list1[i]==n:
            return True
    return False


list1=[5,8,4,6,9,2]
n=9

if search(list1,n):
    print("Found)
else:
    print("Not Found")
