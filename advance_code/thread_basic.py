from threading import Thread
import time

def print_num(count :int):
    time.sleep(0.1)
    for i in range(count):
        print(str(i)+'\n', end='')

t1 = Thread(target=print_num, args=(10,))
t2 = Thread(target=print_num, args=(12,))
# t1.start()
# t2.start()


# inheritance from thread

class MyThread(Thread):
    def __init__(self, name: str, count: int):
        super().__init__()
        self.setName(name)
        self.count = count

        # 守护线程会在主线程结束时候自动结束
        # 主线程则需要等到所有非守护线程结束才能结束
        # 守护线程一般用于非关键性的线程，比如日志
        # self.setDaemon(True)

    def run(self):
        time.sleep(0.1)
        for i in range(self.count):
            print(self.name + ' ' + str(i)+'\n', end='')


t3 = MyThread('t3', 10)
t4 = MyThread('t4', 12)
t3.start()
t4.start()