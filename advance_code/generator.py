# 自定义生成器, 迭代器
# 迭代器: 可以使用for循环, 可以使用next()函数, 可以使用iter()函数, 可以使用list()函数, 可以使用tuple()函数, 可以使用set()函数, 可以使用dict()函数, 可以使用str()函数, 可以使用bytes()函数, 可以使用bytearray()函数, 可以使用memoryview()函数, 可以使用range()函数, 可以使用zip()函数, 可以使用enumerate()函数, 可以使用reversed()函数, 可以使用filter()函数, 可以使用map()函数, 可以使用reduce()函数, 可以使用sorted

# 每次 for 中执行或者调用 next() 等函数, 都会执行一次 yield 语句, 并且返回 yield 语句后面的值
def simple_generator():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3


for i in simple_generator():
    print('simple_generator' + str(i))


print('---' * 10)
def fibonacci(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for i in fibonacci(10):
    print('fibonacci : ' + str(i))

print('---' * 10)

def my_generator(n: int):
    for i in range(n):
        yield i


