"""
下面是3道位运算的题目（模板是数组中除了target其余数字出现多少次，找target）
异或的性质：两个数字异或的结果a ^ b是将
a
和
b
的二进制每一位进行运算，得出的数字。 运算的逻辑是
如果同一位的数字相同则为
0，不同则为
1

异或的规律：任何数和本身异或则为0，任何数和
0
异或是本身

[56 * -在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了2次。请找出那个只出现一次的数字。]
思路1(数学法)：return (sum(set(nums)) * 2 - sum(nums))
第一项是所有数求和乘2，第二项是nums求和（除了target出现一次，其余出现2次）。所以相减就可以得到我们的目标。

思路2（位运算）：所有元素异或运算，由于交换律和任何数和
0
异或是本身，最后直接可以得到结果

[56 * -在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。]
思路1（数学法）：return (sum(set(nums)) * 3 - sum(nums)) / 2
第一项是所有数求和乘3，第二项是nums求和（除了target出现一次，其余出现3次）。所以除以2就可以得到我们的目标。之所以 // 是因为直接除法会出现小数点。

思路2(位运算)：从题目已知最大32位，那我们的思路就是从000..
.000
一位一位的恢复出来这个数。每一位判断有几个1，然后如果cnt % 3 != 0
就说明这个bit上我们寻找的target也是1, res = res | bit(按位或操作)。判断完32个位置之后得到结果
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            cnt = 0
            idx = 1 << i
            for num in nums:
                if num & idx != 0:
                    cnt = cnt + 1
            if cnt % 3 == 1:
                res = res | idx
        return res


"""
[56 - 数组中除了两个元素只出现一次，剩下所有元素出现了两次，找到这两个元素]
我们进行一次全员异或操作，得到的结果就是那两个只出现一次的不同的数字的异或结果。

我们刚才讲了异或的规律中有一个任何数和本身异或则为0， 因此我们的思路是能不能将这两个不同的数字分成两组
A
和
B。分组需要满足两个条件.(1)
两个只出现一次的数字分成不同组(2)
相同的数字分成相同组。这样每一组的数据进行异或即可得到那两个数字。

问题的关键点是我们怎么进行分组呢：由于异或的性质是，同一位相同则为
0，不同则为
1.
我们将所有数字异或的结果一定不是
0，也就是说至少有一位是
1.
我们从右向左找到第一个1出现的位置
idx = 1; while idx & res == 0: idx = idx << 1，分组的依据就来了，遍历nums，你取的那一位是
0
分成
1
组，那一位是
1
的分成一组。这样肯定能保证
相同的数字分成相同组, 不同的那两个数字也会被分成不同组。
"""


class Solution2:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = 0
        for i in nums:
            res = res ^ i

        idx = 1
        while idx & res == 0:
            idx = idx << 1

        a, b = 0, 0
        for i in nums:
            if i & idx == 0:
                a = a ^ i
            else:
                b = b ^ i
        return [a, b]


"""
作者：jichenyeung
链接：https: // leetcode - cn.com / problems / shu - zu - zhong - shu - zi - chu - xian - de - ci - shu - ii - lcof / solution / xiang - xi - zong - jie - kan - bu - dong - ni - gen - wo - xing - xi - 2 /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
