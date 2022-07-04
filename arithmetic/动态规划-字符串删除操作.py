"""
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例 1:

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
说明:

给定单词的长度不超过500。
给定单词中的字符只含有小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))
        for i in range(m):
            ndp = [i + 1] + [0] * n
            for j in range(n):
                if word1[i] == word2[j]:
                    ndp[j + 1] = dp[j]
                else:
                    ndp[j + 1] = min(ndp[j], dp[j + 1]) + 1
            dp = ndp
        return dp[-1]


class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(m + 1):
                if word1[j - 1] == word2[i - 1]:
                    d[i][j] = d[i - 1][j - 1] + 1
                else:
                    d[i][j] = max(d[i - 1][j], d[i][j - 1])
        return m + n - 2 * d[n][m]
