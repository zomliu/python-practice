# 基础语法

array = [5, 10, 30, -10, 1, 19]
min_val = array[0]
for v in array:
    if min_val > v:
        min_val = v

print(min_val)

print('--' * 10)
print('--------- two-dimension list -----------')
# find the min value in two-dimension list
list = [[10, 12, 3], [-4, 15, 6], [17, -8, 19]]
min_val = list[0][0]
for i in range(len(list)):
    for j in range(len(list[i])):
        if min_val > list[i][j]:
            min_val = list[i][j]

print(min_val)

print('--------- string format -----------')
other_str = 'python3.8'
data_str = f'there are serval python interpreters, like python2, python3, python3.5, python3.6, python3.7, {other_str}'
print(data_str)

data_str2 = '{} is a good language'.format(other_str)
print(data_str2)

print('--------- multiplication table -----------')
i, j = 1, 1
while i < 10:
    j = 1
    while j <= i:
        print(f'{j}*{i}={j*j}', end=' ')
        j += 1
    print()
    i += 1

print('--------- for loop -----------')
for d in range(1, 10, 2): # print 1, 3, 5, 7, 9
    print(d, end=' ')

data = ['a', 'b', 'c', 'd', 'e']
for idx in enumerate(data):  # only pint index
    print(idx)

for idx, v in enumerate(data):
    print(idx, v, end='|')

print()
m = {'a': 'A', 'b': 'B', 'c': 'C'}
for k, v in m.items():
    print(k, v, end='|')
print()
for v in m.values():
    print(v, end='|')
print()

print('--------- list gerenator -----------')
list_gen = [i*i for i in range(1, 10)]  # unpack list / tuple
print(list_gen)

def func_list(name : str, count: int):
    return f'{name} is {count} years old'

reesent = [func_list(name, count) for name in ['jack', 'rose', 'lily'] for count in range(1, 3)]

args_list = [('A', 10), ('B', 15), ('C', 100)]
reesent2 = [func_list(*args) for args in args_list]  # or
reesent3 = [func_list(name, count) for name, count in args_list if count > 10]

print('--------- function -----------')
def func(a, b=5):
    return a + b, a, b

funcResult1 = func(1, 2)  # return a tuple
fr1, fr2, fr3 = func(1, 2) # unpack tuple (each variable corresponds to a return value)

# function param with type hint (hint the type of the param)
def func2(a: int, b: int=4) -> int:
    return a + b

def is_iris_flower(num: int) -> bool:
    if num < 100 or num > 999:
        return False
    a = num // 100         #int(num / 100)
    b = num % 100 // 10
    c = num % 10
    return num == a ** 3  + b **3 + c **3

print(is_iris_flower(153))

print('--------- import specific function from a module -----------')
import math
from random import choice
print(math.fabs(-10))
print(choice([1, 2, 3, 4, 5]))

print('--------- list/dict can contains functioins -----------')
def pp(s):
    print(s)
func_list = [pp]
func_dict = {'a': pp}
func_dict['a']('haha')
func_list[0]('hehe')

print('--------- import customize module -----------')
#import util.math
from util.math import add
#from util import math   # import all functions in the module, call function with math.add()

print(add(1, 2))