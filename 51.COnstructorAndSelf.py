# __init__ is an constructor of class


class Computer:
    pass
    #You can't keep an class emty. So you have to add pass statement.
    def __init__(self):
        self.name="Navin"
        self.age=38
    """   
    def update(self):
        self.age=30
    """

    def compare(self,c2):            #We have defind user defined function compare() here
        if self.age==c2.age:
            return True
        else:
            return False




#Inside Heap memory objects will take some space. Every space has some address.
#Evrytime we run the code we get different address
#Size of object depends on no of variables in a class
#Constructor decides the memory for the object. CLassName() is the constructor
#Here Computer() is the constructor. The constructor first calls __init__ method
c1=Computer()
print(id(c1))
c2=Computer()
print(id(c2))

if c1.compare(c2):
    print("They are same")

else:
    print("They are different")

#It will print None
#print(c1.update())

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)

#If you want to change the name variable then you can change like below
c1.name="Rashi"
c1.age=28

print(c1.name)
print(c1.age)

print
