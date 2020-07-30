'''
我们提供了一个类：

public class Foo {
  public void one() { print("one"); }
  public void two() { print("two"); }
  public void three() { print("three"); }
}
三个不同的线程将会共用一个 Foo 实例。

线程 A 将会调用 one() 方法
线程 B 将会调用 two() 方法
线程 C 将会调用 three() 方法
请设计修改程序，以确保 two() 方法在 one() 方法之后被执行，three() 方法在 two() 方法之后被执行。

 

示例 1:

输入: [1,2,3]
输出: "onetwothree"
解释:
有三个线程会被异步启动。
输入 [1,2,3] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 two() 方法，线程 C 将会调用 three() 方法。
正确的输出是 "onetwothree"。
示例 2:

输入: [1,3,2]
输出: "onetwothree"
解释:
输入 [1,3,2] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 three() 方法，线程 C 将会调用 two() 方法。
正确的输出是 "onetwothree"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/print-in-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 方法一，while循环法（超时）：
#
# 可能是不懂多线程的同学最能够接受的基础解法，可以大体理解多线程的阻塞是什么意思。
#
# 就相当于先用某些方法卡住执行顺序，然后不断监控目标，直到目标符合条件时才跳出当前断点继续执行后续语句。
#
# 输出是正确的，只是因为没法像threading模块那样很好的监控线程，所以大概率会超时，其他语言或许可以用这种方法AC，但python相对较慢，大约只能过30 / 37
# 的数据。
#
# 对于单次阻塞来说，运行时间大约是threading模块时间的10 - 14
# 倍这样，整个程序平均时间差距就会在15 - 25
# 倍这样。


class Foo:
    def __init__(self):
        self.t = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.t = 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.t != 1:
            pass
        printSecond()
        self.t = 2

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.t != 2:
            pass
        printThird()


# 方法二，Condition条件对象法：
#
# threading模块里的Condition方法，后面五种的方法也都是调用这个模块和使用不同的方法了，方法就是启动wait_for来阻塞每个函数，
# 直到指示self.t为目标值的时候才释放线程，with是配合Condition方法常用的语法糖，主要是替代try语句的。
import threading


class Foo2:
    def __init__(self):
        self.c = threading.Condition()
        self.t = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.res(0, printFirst)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.res(1, printSecond)

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.res(2, printThird)

    def res(self, val: int, func: 'Callable[[], None]') -> None:
        with self.c:
            self.c.wait_for(lambda: val == self.t)  # 参数是函数对象，返回值是bool类型
            func()
            self.t += 1
            self.c.notify_all()


# 方法三，Lock锁对象法：
#
# 在这题里面功能都是类似的，就是添加阻塞，然后释放线程，只是类初始化的时候不能包含有参数，所以要写一句acquire进行阻塞，调用其他函数的时候按顺序release释放。
import threading


class Foo3:
    def __init__(self):
        self.l1 = threading.Lock()
        self.l1.acquire()
        self.l2 = threading.Lock()
        self.l2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.l1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.l1.acquire()
        printSecond()
        self.l2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.l2.acquire()
        printThird()


# 方法四，Semaphore信号量对象法：
#
# 和方法三是类似的，不过在类赋值的时候可以带有参数自带阻塞。
import threading


class Foo4:
    def __init__(self):
        self.s1 = threading.Semaphore(0)
        self.s2 = threading.Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.s1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.s1.acquire()
        printSecond()
        self.s2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.s2.acquire()
        printThird()


# 方法五，Event事件对象法：
#
# 原理同上，用wait方法作为阻塞，用set来释放线程，默认类赋值就是阻塞的。
import threading


class Foo5:
    def __init__(self):
        self.b1 = threading.Event()
        self.b2 = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.b1.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.b1.wait()
        printSecond()
        self.b2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.b2.wait()
        printThird()


# 方法六，Barrier栅栏对象法：
#
# Barrier初始化的时候定义了parties = 2
# 个等待线程，调用完了parties个wait就会释放线程。
import threading


class Foo6:
    def __init__(self):
        self.b1 = threading.Barrier(2)
        self.b2 = threading.Barrier(2)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.b1.wait()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.b1.wait()
        printSecond()
        self.b2.wait()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.b2.wait()
        printThird()


# 方法七，Queue队列法1：
#
# 直接使用多线程专用的阻塞队列，对于队列为空时，get方法就会自动阻塞，直到put使之非空才会释放进程。
import queue


class Foo7:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.put(0)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.get()
        printSecond()
        self.q2.put(0)

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.get()
        printThird()


# 方法八，Queue队列法2：
#
# 反过来，对于定容队列来说，如果队列满了，put方法也是阻塞。
import queue


class Foo8:
    def __init__(self):
        self.q1 = queue.Queue(1)
        self.q1.put(0)
        self.q2 = queue.Queue(1)
        self.q2.put(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.get()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.put(0)
        printSecond()
        self.q2.get()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.put(0)
        printThird()


# 作者：tuotuoli
# 链接：https: // leetcode - cn.com / problems / print - in -order / solution / 1114 - an - xu - da - yin - python3de - 5
# chong - jie - fa - by - tuotu /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。