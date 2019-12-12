'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        o = len(nums)

        def do(father, other, l):
            if len(father) == l:
                res.append(father)
            for i, w in enumerate(other):
                cur = father + [w]
                k = other[:i] + other[i+1:]
                do(cur, k, l)
        do([], nums, o)
        return res


# 时间空间 n!

