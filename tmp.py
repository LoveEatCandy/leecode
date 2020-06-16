import heapq


class Solution:

    def __init__(self):
        self.r = [1]
        a = b = c = 0
        for _ in range(1690):
            v = min(self.r[a] * 2, self.r[b] * 3, self.r[c] * 5)

            if self.r[a] * 2 == v:
                a += 1
            elif self.r[b] * 3 == v:
                b += 1
            else:
                c += 1
            self.r.append(v)

    def nthUglyNumber(self, n: int) -> int:
        return self.r[n-1]
