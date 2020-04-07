def person(name,*data):
    print(name)
    print(data)

person("Sankarsan",28,"Pune",9892915980)

print("==============================================")
print("Program for Keyword Variable Length Arguments: ")

def person1(name1,**data1):
    print("name:",name1)
    for i,j in data1.items():
        print(i,j)

person1("SankarsanChoudhury",age=38,city="Pune",mob=9892915980)