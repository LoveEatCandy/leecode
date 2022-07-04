class A:
    a = 1


class B:
    def __init__(self):
        self.a = 1


m = A()
n = A()
print(m.a, n.a)
m.a = 2
print(m.a, n.a)
