class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2


    #def sum(self,a,b,c):
        #s=a+b+c
        #return s


    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
           s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s


s1=Student(10,20)

print(s1.sum(30,40,50))
print(s1.sum(30,40))
print(s1.sum(30))