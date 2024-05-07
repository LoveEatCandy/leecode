"""
给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。

 

示例：

给出如下 3x6 的高度图:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

返回 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        M, N = len(heightMap), len(heightMap[0])
        handled = [[0] * N for _ in range(M)]
        board = []
        for n in range(N):
            heapq.heappush(board, (heightMap[0][n], 0, n))
            heapq.heappush(board, (heightMap[M - 1][n], M - 1, n))
            handled[0][n] = 1
            handled[M - 1][n] = 1
        for m in range(1, M - 1):
            heapq.heappush(board, (heightMap[m][0], m, 0))
            heapq.heappush(board, (heightMap[m][N - 1], m, N - 1))
            handled[m][0] = 1
            handled[m][N - 1] = 1
        res = 0
        while board:
            h, m, n = heapq.heappop(board)
            neib = []
            if m + 1 < M and not handled[m + 1][n]:
                neib.append((m + 1, n))
            if m - 1 >= 0 and not handled[m - 1][n]:
                neib.append((m - 1, n))
            if n + 1 < N and not handled[m][n + 1]:
                neib.append((m, n + 1))
            if n - 1 < N and not handled[m][n - 1]:
                neib.append((m, n - 1))
            for i, j in neib:
                dif = h - heightMap[i][j]
                if dif > 0:
                    res += dif
                handled[i][j] = 1
                heapq.heappush(board, (h if dif > 0 else heightMap[i][j], i, j))
        return res
