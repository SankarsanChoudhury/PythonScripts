

f=open("D://Photos_Sankarsan//22.JPG",'rb')
f1=open("MyPicture.JPG",'wb')

for i in f:
    f1.write(i)