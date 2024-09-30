# object.__new__(class, *args, **kwargs) , 这个方法是实例化对象的过程

# 完整的实例化一个实例的过程如下:
#       person = Person("Tom")
#       person =  object.__new__(Person, "Tom")
#       person.__init__("Tom")

# 使用场景: 

# 单例类 

# 元类: 通过继承 type 并重写 __new__ 方法，可以控制类的创建过程，实现一些高级特性，比如：
#       - 动态创建类
#       - 给类添加属性或方法
#       - 验证类定义

# 缓存: 对于一些计算开销较大的对象，可以将创建好的实例缓存起来，避免重复创建。
# 控制实例过程
# 基础类型的别名类

# 单例类
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# 元类
class Meta(type):
    def __new__(cls, name, bases, attrs):
        # 在这里可以对类进行一些修改，比如添加属性或方法
        attrs['add'] = lambda self, x, y: x + y
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=Meta):
    pass


# 缓存
class CachedObject:
    _cache = {}

    def __new__(cls, *args, **kwargs):
        key = (cls, args, tuple(kwargs.items()))
        if key not in cls._cache:
            cls._cache[key] = super().__new__(cls)
        return cls._cache[key]
    

# 控制实例化: 限制实例的创建：通过在 __new__ 中添加条件判断，可以限制实例的创建，比如限制实例的数量或者根据某些条件拒绝创建。
class LimitedInstance:
    _count = 0
    _max_count = 10

    def __new__(cls, *args, **kwargs):
        if cls._count >= cls._max_count:
            raise Exception("Instance limit reached")
        cls._count += 1
        return super().__new__(cls, *args, **kwargs)
    

# 基础类型的别名类
class Status(int):
    def __new__(cls, value):
        return super().__new__(cls, value)