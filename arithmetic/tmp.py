class Solution:

    def __init__(self):
        self.cache = [1] * 59
        self.cache[0] = 0 
        self.cache[1] = 1
        i = 2
        while i <= 58:
            self.cache[i] = max(self.cache[i // 2], i // 2) * \
                max(self.cache[i - i // 2], i - i//2)
            i += 1

    def cuttingRope(self, n: int) -> int:
        return self.cache[n]


a = Solution()
print(a.cuttingRope(8))
import math

math.sqrt()