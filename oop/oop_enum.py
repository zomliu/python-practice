from enum import Enum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# 枚举类中可以定义 value 相同的成员, value 相同的成员其实指向的是同一个内存地址, 因此用 == 或者 is 比较返回 True
# 如果要避免重复可以用 @enum.unique 来修饰枚举类
class Status1(Enum):
    SUCCESS = 200
    OK = 200
    NOT_FOUND = 404

class Color2(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

def access_enum_member():
    print(Color.RED)
    print(Color.RED.name)
    print(Color.RED.value)
    print(Color(1))      # 圆括号里面使用枚举成员的值来转换成枚举对象
    print(Color['RED'])  # 方括号里面使用枚举成员的名字来转换成枚举对象
    
    for member in Color:
        print(member)
        
    print('----------')
    for c2 in Color2:
        print(c2)


if __name__ == '__main__':
    access_enum_member()