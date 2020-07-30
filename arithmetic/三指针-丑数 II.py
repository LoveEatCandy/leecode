'''
编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from heapq import heappop, heappush


class Ugly:
    def __init__(self):
        seen = {1, }
        self.nums = nums = []
        heap = []
        heappush(heap, 1)

        for _ in range(1690):
            curr_ugly = heappop(heap)
            nums.append(curr_ugly)
            for i in [2, 3, 5]:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)


class Solution:
    u = Ugly()

    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]


class Solution2:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2 = i3 = i5 = 0
        for _ in range(n - 1):
            v = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(v)

            while nums[i2] * 2 <= v:
                i2 += 1
            while nums[i3] * 3 <= v:
                i3 += 1
            while nums[i5] * 5 <= v:
                i5 += 1
        return nums[-1]
