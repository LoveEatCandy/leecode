"""
给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/pseudo-palindromic-paths-in-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        """
        1. n ^ n = 0
        2. n & (n - 1) = 0
        """

        def traverse(node: TreeNode, counter):
            if not node:
                return 0
            counter ^= 1 << node.val
            if node.left or node.right:
                l = r = 0
                if node.left:
                    l = traverse(node.left, counter)
                if node.right:
                    r = traverse(node.right, counter)
                count = l + r
            else:
                if counter == 0 or counter & (counter - 1) == 0:
                    count = 1
                else:
                    count = 0
            return count

        return traverse(root, 0)
