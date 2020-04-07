class A:
    def show(self):
        print("in A Show")

class B(A):
    #pass
    def show(self):
        print("in B show")    # Since show() is present in both A & B class here method in child class will override method in parent class


#a1=A()
a1=B()
a1.show()   # It will print in B show

