from typing import List


class Solution:
    def maxSumWithLeftRight(self, A, L, R):
        max_L = sum(A[:L])
        res = max_L
        for i in range(L, len(A)-R+1):
            max_L = max(max_L, sum(A[i-L:i]))
            res = max(res, max_L + sum(A[i:i+R]))
            print(A[i-L:i], A[i:i+R], max_L, res)
        return res

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        return max(self.maxSumWithLeftRight(A, L, M), self.maxSumWithLeftRight(A, M, L))


print(Solution().maxSumTwoNoOverlap([1, 0, 3], 1, 2))

20
