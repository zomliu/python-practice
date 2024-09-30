# type() 用法
# 1. 获取对象的类型
# 2. determine the type of an object
# 3. create a class from string

# Reference: https://www.youtube.com/watch?v=t_ijZ-IVX38&list=PLvQDgAXJ4ADMzlySkwIGomEA9j1Vgq5uS&index=5



print('type(1): ', type(1))  # obtain the type of an object

print('isinstance(1, int): ', isinstance(1, int)) # determine the type of an object


# 动态生成类
clas_body = """
def method_1(self):
    print("method_1")

def method_2(self, a: int, b: int) -> int:
    return a + b
"""

class_dict = {}
exec(clas_body, globals(), class_dict)

Customer = type("Customer", (object,), class_dict)

c = Customer()

print('type(Customer())', type(c))
c.method_1()
print(c.method_2(1, 2))


# 动态生成类
print('---' * 3)
def p1(self):
    print("p1")

Class_A = type('Class_A', (), {'field_name': 'f_name', 'p1': p1})

ca = Class_A()
print(ca.field_name)
ca.p1()