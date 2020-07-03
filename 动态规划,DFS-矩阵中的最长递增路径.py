'''
给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
输出: 4
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:

输入: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
输出: 4
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from functools import reduce


# DP
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        all_nums = []
        if matrix == []:
            return 0
        if matrix == [[]]:
            return 0
        width = len(matrix[0])
        height = len(matrix)
        for y in range(height):
            for x in range(width):
                all_nums.append((y, x, matrix[y][x]))
        matrix.append([0] * width)
        for row in matrix:
            row.append(0)
        saving_matrix = [[1 for _ in range(width)] for _ in range(height)]
        all_nums = sorted(all_nums, key=lambda x: x[2], reverse=True)

        while all_nums:
            y, x, num = all_nums.pop()
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ny = y + dy
                nx = x + dx
                if matrix[ny][nx] > num:
                    saving_matrix[ny][nx] = max(saving_matrix[ny][nx], saving_matrix[y][x] + 1)
        return max(reduce(lambda a, b: a + b, saving_matrix))


# DFS
class Solution2:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0

        row = len(matrix)
        col = len(matrix[0])
        lookup = [[0] * col for _ in range(row)]

        def dfs(i, j):
            if lookup[i][j] != 0:
                return lookup[i][j]
            res = 1
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and matrix[tmp_i][tmp_j] > matrix[i][j]:
                    res = max(res, 1 + dfs(tmp_i, tmp_j))
            lookup[i][j] = max(res, lookup[i][j])
            return lookup[i][j]

        return max(dfs(i, j) for i in range(row) for j in range(col))
