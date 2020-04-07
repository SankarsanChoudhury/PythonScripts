#Compile Time error OR Syntatical Error
#Logical error
#RUn time error

a=5
b=0

try:
    print(a/b)
except Exception:
    print("Hey,You cant divide a number by zero")

print("Bye")