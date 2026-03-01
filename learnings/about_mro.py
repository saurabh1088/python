# MRO - Method Resolution Order

class A:
    def method(self):
        print("Method in class A")

class B(A):
    def method(self):
        print("Method in class B")

class C(A):
    def method(self):
        print("Method in class C")

class D(B, C):
    pass

d = D()
d.method()  # This will call the method in class B due to MRO
print(D.__mro__)  # This will show the method resolution order for class D
