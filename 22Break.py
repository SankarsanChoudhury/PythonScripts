#Designing a vending machine
availableCandy=5
x=int(input("How many candies do you want? "))

i=1
while i<=x:
    if i>availableCandy:
        break
    print("Candy")
    i+=1

print("Out of stock. There is no candy left.)"



