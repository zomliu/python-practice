from threading import Thread, Lock, Condition


lock = Lock()

def task():
    global lock
    lock.acquire()
    print("task step 1 ...")
    print("task step 2 ...")
    lock.release()


class CustomQueue():
    def __init__(self, size: int) -> None:
        self.__bucket = list()
        self.__size = size
        self.__lock = Condition()

    def put(self, item):
        with self.__lock:   # __lock.acquire()    ==> lock.realease()
            while len(self.__bucket) == self.__size:
                self.__lock.wait()
            
            self.__bucket.insert(0, item)
            self.__lock.notify_all()

    def get(self):
        with self.__lock:
            while len(self.__bucket) == 0:
                self.__lock.wait()

            result = self.__bucket.pop()
            self.__lock.notify_all()
            return result