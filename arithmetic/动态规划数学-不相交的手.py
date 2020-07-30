'''
偶数 个人站成一个圆，总人数为 num_people 。每个人与除自己外的一个人握手，所以总共会有 num_people / 2 次握手。

将握手的人之间连线，请你返回连线不会相交的握手方案数。

由于结果可能会很大，请你返回答案 模 10^9+7 后的结果。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/handshakes-that-dont-cross
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# DP
class Solution:
    def numberOfWays(self, num_people: int) -> int:
        dp = [0] * (num_people + 1)
        dp[0] = 1
        dp[2] = 1
        for i in range(2, num_people // 2 + 1):
            for j in range(i):
                dp[i * 2] += dp[j * 2] * dp[i * 2 - 2 - j * 2]
        return dp[num_people] % (1000000000 + 7)


# 数学
class Solution2:
    def numberOfWays(self, num_people: int) -> int:
        n = num_people // 2
        from math import factorial
        return (factorial(2 * n) // factorial(n) // factorial(n) // (n + 1)) % (10 ** 9 + 7)


'''
作者：weak-chicken
链接：https://leetcode-cn.com/problems/handshakes-that-dont-cross/solution/zhi-jie-yong-qia-te-lan-shu-gong-shi-ke-yi-yi-xing/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

思路很简单，假设以1号为桩点，那么和1号握手的人只能是2，4，6...，n,此时1与i号握手所连成的线会把图分为左右两部分（之前的两个子问题），
之所以不能和奇数人握手是因为会分割成奇数的两部分，两部分均无解，所有两部分的可能性乘积的和既为答案
'''
