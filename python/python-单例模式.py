import threading
import time


class A:
    _instance = None
    lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls.lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class B:
    pass


def m(i):
    time.sleep(1)
    a = A()
    a.i = i
    print(id(a), ":", a.i)
    time.sleep(1)
    return


if __name__ == "__main__":
    task_list = []
    for one in range(100):
        t = threading.Thread(target=m, args=[one])
        t.start()
        print(threading.active_count())
    # a = A()
    # b = A()
    # print(id(a))
    # print(id(b))
