"""
import threading

class DiningPhilosophers:

    def __init__(self):
        self.l = threading.Lock()

    def wantsToEat(self, philosopher, *actions):
        self.l.acquire()
        [*map(lambda func: func(), actions)]
        self.l.release()

作者：tuotuoli
链接：https://leetcode-cn.com/problems/the-dining-philosophers/solution/1226-zhe-xue-jia-jin-can-lun-liu-chi-mian-by-tuotu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

from threading import Lock


class DiningPhilosophers:
    def __init__(self):
        self.get = Lock()
        self.forks = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork: "Callable[[], None]",
        pickRightFork: "Callable[[], None]",
        eat: "Callable[[], None]",
        putLeftFork: "Callable[[], None]",
        putRightFork: "Callable[[], None]",
    ) -> None:
        with self.get:  # 下面原子
            left = (philosopher + 1) % 5  # 顺时针
            right = philosopher
            self.forks[left].acquire()  # 拿走左叉
            self.forks[right].acquire()  # 拿走右叉

            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
            self.forks[left].release()  # 还回左叉
            self.forks[right].release()  # 还回右叉


"""
作者：yuhan - huang
链接：https: // leetcode - cn.com / problems / the - dining - philosophers / solution / pythonliang - chong - jie - fa - by - yuhan - huang /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
