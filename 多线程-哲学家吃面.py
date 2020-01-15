'''
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
'''