from abc import ABC, abstractmethod

# 抽象类, 继承 abc.ABC, 并且类中有抽象方法(使用@abstractmethod装饰的方法)

class Base(ABC):
    
    @abstractmethod
    def action(self):
        pass


class Cat(Base):
    def action(self):
        print("cat action")


class Dog(Base):
    def action(self):
        print("dog action")


def test_abs(base: Base):
    base.action()


if __name__ == "__main__":
    cat = Cat()
    dog = Dog()

    test_abs(cat)
    test_abs(dog)