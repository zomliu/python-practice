
class Animal:
    has_legs = True  # 类属性, 所有对象共享, 还可以通过对象直接修改
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)
    
    def sound(self):
        pass

    # 添加装饰器的方法可以直接 Animal.clazz_method() 调用, 类似 Java 的静态方法
    @classmethod    
    def clazz_method(self):
        print('clazz method')

class Dog(Animal):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print('wang wang')

class Cat(Animal):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print('miao miao')


def make_sound(aa: Animal):
    aa.sound()

d = Dog('wangcai', 'white')
c = Cat('miaomiao', 'black')

print('sub_class.has_legs: ', d.has_legs)

# -----------  自定义装饰器   -------------
# 修饰有返回值的自定义装饰器, 装饰器内打印原函数结果
def decorator1(func):
    def wrapper(*args, **kwargs):
        print('wrapper')
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

# 修饰不带返回值的自定义装饰器
def decorator2(func):
    def wrapper(*args, **kwargs):
        print('wrapper')
        func(*args, **kwargs)
    return wrapper
