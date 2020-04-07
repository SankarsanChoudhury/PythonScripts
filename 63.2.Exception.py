a=5
b=0

try:
    print("Resource open")
    print(a/b)

except Exception as e:
    print("Hey,You cant divide a number by zero ",e)
    print("Resource closed")

