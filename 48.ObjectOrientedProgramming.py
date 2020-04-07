#Object has attributes & behaviour
#Human is an object, height, name are attributes
#Class is a Design/blueprint & Objects are instances(real entities)

class Computer:
    def config(self):     #self is the object name which you are passing in the method config()
        print("i5,16gb,1TB")

x=9
print(type(x))

y="Sankarsan"
print(type(y))
a=5
a.bit_length()

#Creating an object comp1 of COmputer class
comp1=Computer() #It is a constructor

#Creating nother object
comp2=Computer()

print(type(comp1))

#Call the method config by sending the object comp1 as parameter
Computer.config(comp1)
Computer.config(comp2)

#This is another way of calling the method with the object comp1 & comp2
#In this below line config() method will accept object comp1 and pass it into self parameter
comp1.config()
comp2.config()