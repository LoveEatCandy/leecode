"""
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        target = sum
        h = collections.defaultdict(int)
        self.countSum(root, 0, h, target)
        return self.count

    def countSum(self, root, cur_sum, h, target):
        if not root:
            return
        cur_sum += root.val
        if cur_sum == target:
            self.count += 1
        self.count += h[cur_sum - target]
        # print(self.count)
        h[cur_sum] += 1
        self.countSum(root.left, cur_sum, h, target)
        self.countSum(root.right, cur_sum, h, target)
        h[cur_sum] -= 1
