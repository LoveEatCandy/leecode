'''
给定一个表示分数的非负整数数组。 玩家1从数组任意一端拿取一个分数，随后玩家2继续从剩余数组任意一端拿取分数，然后玩家1拿，……。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。

给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

示例 1:

输入: [1, 5, 2]
输出: False
解释: 一开始，玩家1可以从1和2中进行选择。
如果他选择2（或者1），那么玩家2可以从1（或者2）和5中进行选择。如果玩家2选择了5，那么玩家1则只剩下1（或者2）可选。
所以，玩家1的最终分数为 1 + 2 = 3，而玩家2为 5。
因此，玩家1永远不会成为赢家，返回 False。
示例 2:

输入: [1, 5, 233, 7]
输出: True
解释: 玩家1一开始选择1。然后玩家2必须从5和7中进行选择。无论玩家2选择了哪个，玩家1都可以选择233。
最终，玩家1（234分）比玩家2（12分）获得更多的分数，所以返回 True，表示玩家1可以成为赢家。
注意:

1 <= 给定的数组长度 <= 20.
数组里所有分数都为非负数且不会大于10000000。
如果最终两个玩家的分数相等，那么玩家1仍为赢家。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/predict-the-winner
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 下面是代码实现：
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0 or n == 1:
            return True
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i - 1][j], nums[j] - dp[i][j - 1])

        return dp[-1][-1] >= 0


# 实际上可以简化为一维的dp：
class Solution2:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0 or n == 1:
            return True
        dp = [0] * n
        for i in reversed(range(n)):
            dp[i] = nums[i]
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0

'''
对于偶数个数字的数组，玩家1一定获胜。因为如果玩家1选择拿法A，玩家2选择拿法B，玩家1输了。则玩家1换一种拿法选择拿法B，因为玩家1是先手，所以玩家1一定可以获胜。

对于奇数个数字的数组，利用动态规划(dynamic programming)计算。 首先证明最优子结构性质。对于数组[1..n]中的子数组[i..j]，
假设玩家1在子数组[i..j]中的拿法是最优的，即拿的分数比玩家2多出最多。假设玩家1拿了i，则[i+1..j]中玩家1拿的方法也一定是最优的。
利用反证法证明：如果玩家1在[i+1..j]中有更优的拿法，即玩家1在[i+1...j]可以拿到更多的分数，则玩家在[i..j]中拿到的分数就会比假设的最优拿法拿到的分数更多，
显然矛盾。如果玩家1拿了j，同理可证矛盾。 所以当前问题的最优解包含的子问题的解一定也是子问题的最优解。

对于只有一个数字的子数组,即i=j，dp[i][i] = num[i]，因为玩家1先手拿了这一个分数，玩家2就没得拿了，所以是最优拿法。 
对于两个数字的子数组,即j-i=1，dp[i][j]=abs(num[i]-num[j]),玩家1先手拿两个数中大的一个，所以玩家1一定比玩家2多两个数字差的绝对值，为最优拿法。 
对于j-i>1的子数组，如果玩家1先手拿了i，则玩家1手里有num[i]分，则玩家2一定会按照[i+1..j]这个子数组中的最优拿法去拿，
于是玩家2此时手里相当于有dp[i+1][j]分，于是玩家1比玩家2多num[i]-dp[i+1][j]分。如果玩家1先手拿了j，则玩家1手里有num[j]分，
则玩家2一定会按照[i..j-1]这个子数组中的最优拿法去拿，于是玩家2此时手里相当于有dp[i][j-1]分，于是玩家1比玩家2多num[j]-dp[i][j-1]分。
数组的填充方向是从下往上，从左到右，最后填充的是dp[1][n]。
'''