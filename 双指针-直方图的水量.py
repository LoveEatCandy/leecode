'''
给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。


上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/volume-of-histogram-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def trap(self, height: 'List[int]') -> int:
        if not height:
            return 0
        n = len(height)
        left, right = [0] * n, [0] * n
        left[0], right[-1] = height[0], height[-1]
        for i in range(1, n):
            left[i] = max(height[i], left[i - 1])
        for i in reversed(range(n - 1)):
            right[i] = max(height[i], right[i + 1])
        return sum(min(l, r) - h for l, r, h in zip(left, right, height))
