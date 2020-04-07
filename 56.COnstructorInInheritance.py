#MRO(Method Resolution Order)
#Super class can not access any features of Sub class
#However a sub class can access all the features of SUper class

#when you create object of sub class it will call __init__ of sub class first.
#If you call super then it will call __init__ of super class first.

class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):

    def __init__(self):
        super().__init__()   # Using super() yoi can access the parent class constructor __init__()
        print("in B init")
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")



a1=B()  # Here it will call the constructor of B class if it has a constuctor. If B is not having any constructor then it will call constructor of A class



'''
a1=A()


a1.feature1()
a1.feature2()

b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

'''

