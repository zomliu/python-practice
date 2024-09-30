# 当前属性是私有的，无法直接访问，此时需要通过getter和setter方法来获取和设置属性值时, 需要使用property
# 两种方式: 
#   方式一: property(fget, fset, fdel, doc)
#   方式二: @property


# property 代理属性访问
class Person:
    def __init__(self, name):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name + '_suffix'

    name = property(get_name, set_name)


class Person2:
    def __init__(self, name):
        self._name = name
    
    # 相当于 name 的 getter 方法 (只有 getter 没有 setter 方法时, 相当于 name 是个只读属性)
    @property
    def name(self):
        return self._name
    
    # 相当于 name 的 setter 方法
    @name.setter
    def name(self, name):
        self._name = name + '_suffix'


    @name.deleter
    def name(self):
        print("delete name")

def property_demo1():
    p1 = Person("Jack")
    print(p1.name)
    p1.name = "Tom"
    print(p1.name)

def property_demo2():
    p2 = Person2("Jack")
    print(p2.name)
    p2.name = "Tom"
    print(p2.name)


if __name__ == '__main__':
    property_demo1()
    property_demo2()
