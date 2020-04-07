#You can create object of inner class inside the outer class
# OR you can create object of inner class outside the outer class provided you use outer clas name to call it


class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student("Sankarsan",100)
s2=Student("Subhasmita",200)

s1.show()
#s1.Laptop.brand

#lap1=Student.Laptop()