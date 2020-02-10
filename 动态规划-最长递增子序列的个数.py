'''
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 1:
            return l
        length = [0] * l
        count = [1] * l
        for j in range(l):
            for i in range(j):
                if nums[j] > nums[i]:
                    if length[i] >= length[j]:
                        length[j] = length[i] + 1
                        count[j] = count[i]
                    elif length[i] + 1 == length[j]:
                        count[j] += count[i]
        longest = max(length)
        return sum(count[i] for i in range(l) if length[i] == longest)
