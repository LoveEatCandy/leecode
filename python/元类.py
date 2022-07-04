from abc import ABCMeta


class Meta(ABCMeta):
    def __new__(mcs, name, bases, namespace, **kwargs):
        print("entering Meta.__new__()")
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)
        print("exiting Meta.__new__(): ", cls)
        return cls

    def __init__(cls, *args, **kwargs):
        print("entering Meta.__init__()")
        super().__init__(*args, **kwargs)
        print("exiting Meta.__init__(): ", cls)
        pass

    def __call__(cls, *args, **kwargs):
        print("entering Meta.__call__()")
        ins = super().__call__(*args, **kwargs)
        print("exiting Meta.__call__(): ", ins)
        return ins


class Foo(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print("entering Class.__new__()")
        rv = super().__new__(cls)
        print("exiting Class.__new__()")
        return rv

    def __init__(self, *args, **kwargs):
        print("executing Class.__init__()")
        super().__init__(*args, **kwargs)


a = Foo()
