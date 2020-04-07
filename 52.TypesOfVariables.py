#instance variable
#Class OR static variable

#namespace is an area where you create and store object/variable
#class namespace
#object/instance namespace

class Car:

    wheels=4

    def __init__(self):
        self.mil=10
        self.com="BMW"

c1=Car()
c2=Car()

c1.mil=8

#If we change the value of class variable it will have impact on all the object
Car.wheels=8

print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)