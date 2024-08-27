# couple approach to create singleton

# By using metaclass
class SingleMetaClass(type):

    # hasattr() is used to check if the class already has an attrbute
    # getattr() is used to get the attrbute of the class
    # setattr() is used to set the attrbute of the class
    # priciple: 一个类在 Python 运行环境中中存在一份, 利用上述 3 个方法可以通过读写类变量的特性来实现单例
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            setattr(cls, '__instance', super().__call__(*args, **kwargs))
        return getattr(cls, '__instance')


# decorator via closuse
# principle: 一个类在 Python 运行环境中中存在一份, 因此类被加载时会执行这个装饰器一次, 因此也就声明了一份 instance, 相当于一个共享的字典
def singleton(cls):
    instance = {}
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper


# decorator via class attribute
def singleton2(cls):
    def wrapper(*args, **kwargs):
        if not hasattr(cls, '__instance'):
            setattr(cls, '__instance', cls(*args, **kwargs))
        return getattr(cls, '__instance')
    return wrapper


# ------------------ 测试 ------------------

class Single1(metaclass=SingleMetaClass):
    pass

@singleton
class Single2:
    pass

@singleton2
class Single3:
    pass

if __name__ == '__main__':
    print(Single1() is Single1())
    print(Single2() is Single2())
    print(Single3() is Single3())