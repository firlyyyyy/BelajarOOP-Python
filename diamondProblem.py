""" ==>> DIAMOND PROBLEM <<== """

class A:
    
    def show(self):
        print("class A")

class B(A):
    
    def show(self):
        print("class B")

class C(A):
    
    def show(self):
        print("class C")
    
class D(B, C):
    pass

objek = D()
help(objek)
objek.show()