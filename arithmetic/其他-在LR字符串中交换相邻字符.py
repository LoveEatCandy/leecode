'''
在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。
现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。

示例 :

输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
输出: True
解释:
我们可以通过以下几步将start转换成end:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
注意:

1 <= len(start) = len(end) <= 10000。
start和end中的字符串仅限于'L', 'R'和'X'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-adjacent-in-lr-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # 去掉X,两个字符串应该相等
        s = start.replace('X', '')
        if s != end.replace('X', ''):
            return False

        # start中R的索引要小于等于end的
        # start中L的索引要大于等于end的
        d1 = [ind for ind, i in enumerate(start) if i != 'X']
        d2 = [ind for ind, i in enumerate(end) if i != 'X']

        for ind, char in enumerate(s):
            # R 则start大于end的都是False
            if char == 'R' and d1[ind] > d2[ind]:
                return False
            if char == 'L' and d1[ind] < d2[ind]:
                return False

        return True
