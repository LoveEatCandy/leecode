import threading


# Method 1: A decorator
def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class MyClass:
    pass


"""
优点：装饰器的添加方式通常比多重继承更直观。
缺点：使用MyClass（）创建的对象将是真正的单例对象，而MyClass本身是一个实例，而不是一个类，因此您不能从中调用类方法。
"""


# Method 2: A base class
class Singleton2:
    _instance = None
    lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls.lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance


class MyClass2(Singleton2):
    pass


"""
优点：是一个真是的类。
缺点：多重继承，有可能被覆盖。
"""

from abc import ABCMeta


# Method 3: A metaclass
class Singleton3(ABCMeta):
    _instances = {}
    lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls.lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass3(metaclass=Singleton3):
    pass


"""
优点：是一个真实的类，避免多重继承覆盖。
缺点：无。
"""


# Method 4: import
class MyClass4:
    pass


my_class4 = MyClass4()
# import my_class4
