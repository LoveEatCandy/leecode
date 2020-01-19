'''
给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。

 

示例 1：

输入：nums = [3,6,5,1,8]
输出：18
解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
示例 2：

输入：nums = [4]
输出：0
解释：4 不能被 3 整除，所以无法选出数字，返回 0。
示例 3：

输入：nums = [1,2,3,4,4]
输出：12
解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。
 

提示：

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/greatest-sum-divisible-by-three
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 动态规划
class Solution:
    def maxSumDivThree(self, nums: 'List[int]') -> int:
        r = [0, -1, -1]
        for num in nums:
            g = r[:]
            for i in range(3):
                if r[i] != -1:
                    g[(i + num % 3) % 3] = max(g[(i + num % 3) % 3], r[i] + num)
            r = g
        return r[0]


# 贪心 + 正向思维
class Solution1:
    def maxSumDivThree(self, nums: 'List[int]') -> int:
        a = [x for x in nums if x % 3 == 0]
        b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        c = sorted([x for x in nums if x % 3 == 2], reverse=True)

        ans = 0
        lb, lc = len(b), len(c)
        for j0 in [lb - 2, lb - 1, lb]:
            if j0 >= 0:
                for k0 in [lc - 2, lc - 1, lc]:
                    if k0 >= 0 and j0 % 3 == k0 % 3:
                        ans = max(ans, sum(b[:j0]) + sum(c[:k0]))
        return ans + sum(a)


# 贪心 + 逆向思维
class Solution2:
    def maxSumDivThree(self, nums: 'List[int]') -> int:
        b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        c = sorted([x for x in nums if x % 3 == 2], reverse=True)
        tot = sum(nums)
        ans = 0

        if tot % 3 == 0:
            ans = tot
        if tot % 3 == 1:
            if len(b) >= 1:
                ans = max(ans, tot - b[-1])
            if len(c) >= 2:
                ans = max(ans, tot - sum(c[-2:]))
        elif tot % 3 == 2:
            if len(b) >= 2:
                ans = max(ans, tot - sum(b[-2:]))
            if len(c) >= 1:
                ans = max(ans, tot - c[-1])

        return ans

