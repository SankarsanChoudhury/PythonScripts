#4 types of actual Arguments
#Position
#Keyword
#Default
#Variable length

def person(name,age=18):
    print(name)
    print(age)

person("Sankarsan")

print("================Program2=======")
def person1(name1,age1=18):
    print(name1)
    print(age1)

person1("SankarsanChoudhury",28)

print("================Program3=======")
def sum(a,*b):
    print(a)
    print(b)
    c=a
    for i in b:
        c=c+i
    print(c)

sum(10,20,30,40)