
# decorator without parameter
def decorator_1(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper


# decorator with parameter
def decorator_2(name, age):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"before: {name} - {age}")
            result = func(*args, **kwargs)
            print("after")
            return result
        return wrapper
    return decorator


@decorator_1
def do_something_1():
    print("do something 1")


@decorator_2("zhangsan", 18)    # 相当于先执行了一个 func, func 返回了一个 decorator
def do_something_2():
    print("do something 2")


# ==============  定义装饰器类  =================

# Without argument
class DecoratorClassWithoutArg:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("before")
        result = self.func(*args, **kwargs)
        print("after")
        return result


# With argument (这个本质上是函数装饰器, 是调用的类的 __call__ 方法返回了一个 wrapper 函数)
class DecoratorClassWithArg:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"before: {self.name} - {self.age}")
            result = func(*args, **kwargs)
            print("after")
            return result
        return wrapper

@DecoratorClassWithoutArg
def some_func():
    print("some func")


@DecoratorClassWithArg("zhangsan", 18)
def some_func_2():
    print("some func 2")



# ==============  定义一个给类使用的装饰器函数  =================
def decorator_class(cls):
    def wrapper(*args, **kwargs):
        print("before")
        result = cls(*args, **kwargs)
        print("after")
        return result
    return wrapper

@decorator_class
class SomeClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Running
if __name__ == '__main__':
    print('---------- decorator function ----------')
    do_something_1()
    print('--' * 10)
    do_something_2()

    print('---------- decorator class ----------')
    some_func()
    print('--' * 10)
    some_func_2()

    print('----------  class decorator ----------')
    obj = SomeClass("zhangsan", 18)