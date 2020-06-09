from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        输入：tasks = ["A","A","A","B","B","B"], n = 2
        输出：8
        解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
        '''
        if n == 0:
            return len(tasks)
        n += 1
        c = Counter(tasks)
        i = 0
        while len(c.keys()) > n:
            tmp = c.most_common(n)[-1][1]
            i += tmp
            for k, v in c.most_common(n):
                c[k] -= tmp
                if c[k] <= 0:
                    c.pop(k)
        _max = c.most_common(1)[0][1]
        m = 0
        return (_max - 1) * n + i + m


class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ct = Counter(tasks)
        nbucket = ct.most_common(1)[0][1]
        last_bucket_size = list(ct.values()).count(nbucket)
        res = (nbucket - 1) * (n + 1) + last_bucket_size
        return max(res, len(tasks))


o = Solution2()
print(o.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
