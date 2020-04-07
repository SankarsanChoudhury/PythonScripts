f=open("MyData.txt",'r')  #r is the mode. To read a file we may acheive multi threading but to write it is single thread
#Read the data present in a file
print(f.read())
# r mode is to read a file
# w mode is to write a file
#a mode is to append a file

#readline() method will print the data on console one by one
#print(f.readline(),end='#')
#print(f.readline(),end='#')
#print(f.readline())

for data in f:
    print(data)



#It will create a  file named NewFile is the file is not present
f1=open("NewFile.txt",'w')
f1.write("Something")

f1=open("NewTestFile.txt",'a')
#f1.write("Sankarsan")
#f1.write("Subhasmita")





