# 这种被内部引用的模块, 需要根据运行入口的相对路径来引用 (但用相对路径)
from .util2_2 import add_some

def print_some():
    print(add_some(4, 6))