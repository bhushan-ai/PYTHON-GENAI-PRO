# method resolution order
class A:
    lable = "A: Base Class"

class B(A):
    lable = "B: Masala blend"

class C(A):
    lable = "C: Herbal blend"

class D(B, C):
    pass

cup = D()
print(cup.lable)
print(D.__mro__)
