'''
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

示例 1:

输入: k = 5

输出: 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/get-kth-magic-number-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        x3, x5, x7 = 0, 0, 0
        result = [1]
        for _ in range(1, k):
            result.append(min(3 * result[x3], 5 * result[x5], 7 * result[x7]))
            if result[-1] == 3 * result[x3]:
                x3 += 1
            if result[-1] == 5 * result[x5]:
                x5 += 1
            if result[-1] == 7 * result[x7]:
                x7 += 1
        return result[-1]


'''
作者：echosun
链接：https://leetcode-cn.com/problems/get-kth-magic-number-lcci/solution/mian-shi-ti-1709-di-k-ge-shu-ti-jie-by-echosun/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
