class A:
    def __init__(self):
        print("from the A constructor")

    def feat1(self):
        print("from A")
    def feat2(self):
        print("from A feat2")

class B(A):
    def feat3(self):
        print("from B")


class C(B):
    pass
class D:
    def featd(self):
        print("from D")

class F(A,D):

    pass

c=C()
c.feat3()
f=F()
f.featd()