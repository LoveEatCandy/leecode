'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
 

提示：

数组长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def helper(nums):
            if len(nums) <= 1:
                return True
            root = nums[-1]
            mid = 0
            for i in range(len(nums)):
                if nums[i] > root:
                    mid = i
                    break
            for j in range(i, len(nums)-1):
                if nums[j] < root:
                    return False
            return helper(nums[:i]) and helper(nums[i:-1])

        if not postorder:
            return True
        return helper(postorder)
