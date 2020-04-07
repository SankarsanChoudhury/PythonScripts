class Student:

    school="Telusko"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    def get_m1(self):     #getter or accessor method
        return self.m1

    def set_m1(self,value):  #setter or mutator method
        self.m1=value

    @classmethod
    def getSchool(cls):    #Class method to access the class variable
        return cls.school


    @staticmethod
    def info():
        print("This is student class in abc module")


s1=Student(10,20,30)
s2=Student(40,50,60)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())

Student.info()
