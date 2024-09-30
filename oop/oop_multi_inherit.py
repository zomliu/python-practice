
# 多继承, 如果父类中有重名方法, 子类方法中调用要注意方式


class P1():
    def __init__(self):
        pass

    def f1(self):
        print("P1 - f1")

class P2():
    def __init__(self):
        pass
    
    def f1(self):
        print("P2 - f1")

class Child(P1, P2):
    def __init__(self):
        # super().__init__()
        P1.__init__(self)
        P2.__init__(self)
        print("Child")

    def f3(self):
        P1.f1(self)
        P2.f1(self)


if __name__ == "__main__":
    c = Child()
    c.f3()