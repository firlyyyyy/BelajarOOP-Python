""" ==>> MULTIPLE INHERITANCE <<== """

class A:
    
    def method(self):
        print("ini method A")
        
class B:
    
    def method(self):
        print("ini method B")
        
class Multiple(A, B):
    pass

objek = Multiple()

objek.method()
objek.method()
help(objek)


""" ==>> METHOD RESOLUTION ORDER <<== """

