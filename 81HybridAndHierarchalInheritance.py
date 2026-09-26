# hybrid inheritance
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
#  I --> 2,3    2,3 --> a
# hierarchial Inheritance (branching like tree)
#  I --> 2,3    2 --->a,b  3 --->c,d
class E:
    pass
class F(E):
    pass
class G(E):
    pass
class H(F):
    pass
class I(F):
    pass