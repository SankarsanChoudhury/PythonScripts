class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2-A working")


class B:

    def __init__(self):
        print("in B init")

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")

    def feat(self):
        super().feature2()


a1=C()  # Here it will call the constructor of C class if it has a constuctor. Then it will call constructor of A class followed by B

a1.feature1()
a1.feat()





