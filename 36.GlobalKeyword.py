#Program1==============================

a=10

def something():
    #Local function
    a=15
    print("Inside the FUnction: ",a)

something()
print("Outside the Function: ",a)

#Program2
#Author: Sankarsan Choudhury
print("=======================================")

a=10

def something():
    #Local function
    print("Inside the FUnction: ",a)

something()
print("Outside the Function: ",a)

#===========================================================
#Program3
print("===================================================")

a=10

def program3():
    global a
    a=15
    #Local function
    print("Inside the FUnction: ",a)

program3()
print("Outside the Function: ",a)