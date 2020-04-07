import sys

sys.setrecursionlimit(1500)
print(sys.getrecursionlimit())  #The recursion limit is 1000

i=0
def greet():
    global i
    i+=1
    print("Hello ", i)
    greet()

greet()