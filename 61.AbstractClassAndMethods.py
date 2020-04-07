#ABC-Abstract Base CLasses module supports abstact classes in python
#Python by default does not support abstract classes

from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Its running")

class Whiteboard:
    def write(self):
        print("Its writing")

class Programmer:
    def work(self,com):
        print("Solving Bugs")

#com=Computer()     #TypeError: Can't instantiate abstract class Computer with abstract methods process
#com.process()

com1=Laptop()

prog1=Programmer()
prog1.work()

com1.process()