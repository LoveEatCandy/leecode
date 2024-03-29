"""
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# dfs
class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        def DFS(s, p, memo):
            if not p:
                return not s
            if (s, p) in memo:
                return memo[(s, p)]
            # 第一个字母匹配上
            first_match = len(s) > 0 and len(p) > 0 and (p[0] == s[0] or p[0] == ".")
            # 如果是“*”:可以匹配0个或多个前面字母
            if len(p) > 1 and p[1] == "*":
                result = DFS(s, p[2:], memo) or (first_match and DFS(s[1:], p, memo))
            else:  # 不是“*”时，处理第一个字母匹配上的情形
                result = first_match and DFS(s[1:], p[1:], memo)
            memo[(s, p)] = result
            return result

        memo = {}
        res = DFS(s, p, memo)
        return res


# 动态规划
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        # 初始化首行
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == "*"
        # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == "*":
                    if dp[i][j - 2]:
                        dp[i][j] = True  # 1.
                    elif dp[i][j - 1]:
                        dp[i][j] = True  # 2.
                    elif dp[i - 1][j] and s[i - 1] == p[j - 2]:
                        dp[i][j] = True  # 3.
                    elif dp[i - 1][j] and p[j - 2] == ".":
                        dp[i][j] = True  # 4.
                else:
                    if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]:
                        dp[i][j] = True  # 1.
                    elif dp[i - 1][j - 1] and p[j - 1] == ".":
                        dp[i][j] = True  # 2.
        return dp[-1][-1]


"""
作者：jyd
链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/jian-zhi-offer-19-zheng-ze-biao-da-shi-pi-pei-dong/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
