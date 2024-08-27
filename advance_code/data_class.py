from dataclasses import dataclass, field
import operator


# @dataclass(order=True)  指定 order = True 后, 这个类的实例就支持 sort 操作, 排序规则按定义的第一个字段进行排序, 如果第一个字段相同, 则按第二个字段进行排序, 以此类推
@dataclass
class Cat:
    name: str
    color: str
    age: int = 2
    has_legs: bool = True
    legs: int = field(default=4, init=False)
    sound: str = field(default='meow', init=False, repr=False) # repr=False 表示不参与 repr 操作, init=False 表示不参与初始化参数

    def __post_init__(self):   # __post_init__ 方法会在实例初始化后被调用, 可以在这里进行一些初始化操作, 使用 dataclass 修饰的类可用
        self.legs = 4
        self.sound = 'meow'

c_1 = Cat('Tom', 'white', 3)
c_2 = Cat('Tom', 'yellow', 1)
c_3 = Cat('Tom', 'black')

cats = [c_3, c_1, c_2]

# 推荐排序方法, 自定义排序规则
# cats.sort(key=lambda x: (x.age, x.name), reverse=True)
cats.sort(key=operator.attrgetter('age', 'name'))
# cats.sort(key=operator.attrgetter('age', 'name'), reverse=True)

print(cats)
