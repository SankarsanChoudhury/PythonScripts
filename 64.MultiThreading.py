#Thread is a class. threading is a module
#Main Thread will run all the statements
#We specified that both Hi & Hellow will inheret Thread class
#time is a module and sleep is a method

from time import sleep
from threading  import *

class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)



class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            sleep(1)

t1=Hello()
t2=Hi()

#t1.run()
#t2.run()

t1.start()
sleep(0.2)
t2.start()

print("Bye")