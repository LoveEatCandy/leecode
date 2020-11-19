'''
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chou-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def get_nums():
    r = [1] * 1690
    a, b, c = 0, 0, 0
    for i in range(1, 1690):
        n1, n2, n3 = r[a] * 2, r[b] * 3, r[c] * 5
        r[i] = min(n1, n2, n3)
        if r[i] == n1:
            a += 1
        if r[i] == n2:
            b += 1
        if r[i] == n3:
            c += 1
    return r


class Solution:
    nums = get_nums()

    def nthUglyNumber(self, n: int) -> int:
        return self.nums[n - 1]
