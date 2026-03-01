# MRO - Method Resolution Order

# ---- Example of MRO in Python ----
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


# ---- Example two of MRO in Python ----
#           Root
#          /    \
#         A      B
#         ↑      ↑
#         C      D
#          \    /
#            E
class Root:
    def talk(self): print("Root talking")

class RootA(Root):
    def talk(self): 
        print("A talking")
        super().talk()

class RootB(Root):
    def talk(self): 
        print("B talking")
        super().talk()

class RootC(RootA):
    def talk(self): 
        print("C talking")
        super().talk()

class RootD(RootB):
    def talk(self): 
        print("D talking")
        super().talk()

class RootE(RootC, RootD):
    def talk(self): 
        print("E talking")
        super().talk()

# Testing MRO

d = D()
d.method()  # This will call the method in class B due to MRO
print(D.__mro__)  # This will show the method resolution order for class D

e = RootE()
e.talk()
print(RootE.__mro__)  # This will show the method resolution order for class RootE
