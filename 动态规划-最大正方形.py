'''
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        large = 0
        for a in range(m):
            for b in range(n):
                if matrix[a][b] == '1':
                    dp[a][b] = min(dp[a - 1][b - 1], dp[a - 1][b], dp[a][b - 1]) + 1
                large = max(large, dp[a][b])
        return large ** 2


'''
以dp[i][j]为方形右下角点
'''
