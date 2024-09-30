
# 类变量的默认值所有成员变量共享, 但是如果某个实例对象对类变量进行了值变动, 则就变量就会变成这个实例对象的实例变量了

class Student:
    name = "default"
    age = 0
    
def class_field():
    print(getattr(Student, "name"))
    setattr(Student, "name", "Tom")

    print(getattr(Student, "not_exist", "default"))  # 尝试获取可能不存在的属性, 可以给一个默认值
    print(id(Student.name))

    s1 = Student()
    print(id(s1.name))
    s1.name = "Jack"
    print(id(s1.name))
    print(id(Student.name))

    s2 = Student()
    print(id(s2.name))


    # 使用直接赋值方式增加属性
    Student.sex = "Male"
    # 删除属性
    del Student.sex
    delattr(Student, "age")


    # 类属性都放在了类的__dict__中
    print(Student.__dict__)


# 私有方法和私有属性(使用一个下划线开头或者两个下划线开头, 一个下划线开头时, 外部能访问但不推荐, 两个下划线开头时, 只能在类的内部访问)
class MyClass:
    def __init__(self):
        self.__secret = "secret"
        self._public = "public"
    
    def __private_method(self):
        print("private method")
    
    def public_method(self):
        print("public method")
        self.__private_method()


def access_private_attribute():
    m1 = MyClass()
    
    print(m1.__secret)          # AttributeError 不能访问, 语法上可以用下面方式访问, 但是不推荐
    print(m1._MyClass__secret)
    
    print(m1._MyClass__private_method())
    m1.public_method()


# property 代理属性访问
class Person:
    def __init__(self, name):
        self._name = name
        
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name + '_suffix'

    name = property(get_name, set_name)


def property_demo():
    p1 = Person("Jack")
    print(p1.name)
    p1.name = "Tom"
    print(p1.name)



if __name__ == "__main__":
    # access_private_attribute()
    property_demo()