# Context Manager
# applicable to:
# 1. Operate a file
# 2. Operate a database
# 3. Operate a network connection
# 4. Operate a process
# 5. Operate a thread
# 6. Operate a Lock / Semaphore / Switch 

# Typical Usage: Operate a file
# with open('decorator.py', 'r') as f:
#     print(f.read())


# Customize Context Manager
import time
class Timer:
    def __init__(self):
        self.duration = 0
    
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.duration = self.end - self.start

# 执行顺序就是先执行 __enter__, 再执行 __exit__
with Timer() as t:   # 这个 t 并不一定是 Timer 的实例, 它是 __enter__(self) 的返回值
    time.sleep(1)

print(t.duration)  # 这个必须要在 with 语句块结束后才能访问