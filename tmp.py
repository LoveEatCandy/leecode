class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return matrix
        if len(matrix) == 1:
            r = []
            cur_l = [matrix[0][0]]
            for i in range(matrix[0][1:]):
                if i > cur_l[-1]:
                    cur_l.append(i)
                else:
                    r = cur_l if len(cur_l) > len(r) else r
                    cur_l = [i]
            return r
        l_j = len(matrix)
        l_i = len(matrix[0])

        dp = [[0] * l_i for _ in range(l_j)]
        r = 1
        for j in range(l_j):
            for i in range(l_i):
                cur_count = 1
                if j > 0:
                    if matrix[j - 1][i] < matrix[j][i]:
                        cur_count = max(cur_count, dp[j - 1][i] + 1)
                if i > 0:
                    if matrix[j][i - 1] < matrix[j][i]:
                        cur_count = max(cur_count, dp[j][i - 1] + 1)
                if j < l_j - 1:
                    if matrix[j + 1][i] < matrix[j][i]:
                        cur_count = max(cur_count, dp[j + 1][i] + 1)
                if i < l_i - 1:
                    if matrix[j][i + 1] < matrix[j][i]:
                        cur_count = max(cur_count, dp[j][i + 1] + 1)
                r = max(r, cur_count)
                dp[j][i] = cur_count

        dp = [[0] * l_i for _ in range(l_j)]
        for j in range(l_j - 1, -1, -1):
            for i in range(l_i - 1, -1, -1):
                cur_count = 1
                if j > 0:
                    if matrix[j - 1][i] < matrix[j][i]:
                        cur_count = max(cur_count, dp[j - 1][i] + 1)
                if i > 0:
                    if matrix[j][i - 1] < matrix[j][i]:
                        cur_count = max(cur_count, dp[j][i - 1] + 1)
                if j < l_j - 1:
                    if matrix[j + 1][i] < matrix[j][i]:
                        cur_count = max(cur_count, dp[j + 1][i] + 1)
                if i < l_i - 1:
                    if matrix[j][i + 1] < matrix[j][i]:
                        cur_count = max(cur_count, dp[j][i + 1] + 1)
                r = max(r, cur_count)
                dp[j][i] = cur_count

        return r
