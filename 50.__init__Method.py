class Computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print("Inside init")#__init__ is called automatically

    def config(self):     #self is the object name which you are passing in the method config()
        print("Config is",self.cpu,self.ram)



comp1=Computer('i5',16)
comp2=Computer('i6',8)

comp1.config()
comp2.config()