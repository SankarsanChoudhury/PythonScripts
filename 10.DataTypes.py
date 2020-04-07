#None in python . The same is null in other languages
#Numeric -int,float,complex,bool
#Range

num=6+9j
print(type(num))

a=5.6
b=int(a)
print(b)
print(type(b))

x=2
y=6
z=complex(x,y)
print(z)

bool=y>x
print(bool)

#It will print 1
print(int(True))

#It will print 0
print(int(False))

#It will print range(0, 10)
print(range(10))

#It will print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))

#It will print [2, 4, 6, 8]
print(list(range(2,10,2)))

D={"Sankarsan":100,"Subhasmita":200,"Manmita":300}
#It will print  dict_keys(['Sankarsan', 'Subhasmita', 'Manmita'])
print(D.keys())

#It will print dict_values([100, 200, 300])
print(D.values())
