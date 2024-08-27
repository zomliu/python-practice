from queue import Queue, Empty
from threading import Thread, Lock, Condition

import time

q = Queue(4)

def producer():
    for i in range(10):
        q.put("cat", block=True)
        print('put value: cat \n')
        time.sleep(0.3)

def consumer():
    while True:
        try:
            val = q.get(timeout=0.4)
            print(f'get value: {val} \n')
        except Empty:
            print('queue is empty')
            break

if __name__ == '__main__':
    Thread(target=consumer).start()
    p = Thread(target=producer)
    p.setDaemon(True)
    p.start()
    