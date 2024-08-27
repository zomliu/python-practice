# metaclass 高级用法 Reference: https://www.youtube.com/watch?v=dFoZ0Sux8pI&list=PLvQDgAXJ4ADMzlySkwIGomEA9j1Vgq5uS&index=6

# 声明一个类是, 默认会用 type 作为 metaclass, 例如
class MyClass(object, metaclass=type):
    pass


# 特定场景下, 可能需要对某些子类做些通用的属性处理, 这种场景就可以使用自定义 metaclass
class MyMeta(type):
    def __new__(cls, *args, **kwargs):
        print('MyMeta.__new__')
        clzz = super().__new__(cls, *args)
        if kwargs:
            for key, value in kwargs.items():
                setattr(clzz, key, value)
        return clzz
    
class MyClass(metaclass=MyMeta, class_name='MyClass'):
    pass

mc = MyClass()
print(mc.class_name)