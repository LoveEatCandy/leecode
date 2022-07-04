"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：

0 <= 节点个数 <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.dic = {}
        self.po = preorder
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.recur(0, 0, len(inorder) - 1)

    def recur(self, pre_root, in_left, in_right):
        if in_left > in_right:
            return
        root = TreeNode(self.po[pre_root])
        i = self.dic[self.po[pre_root]]
        root.left = self.recur(pre_root + 1, in_left, i - 1)
        root.right = self.recur(pre_root + 1 + i - in_left, i + 1, in_right)
        return root


class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        head = TreeNode(preorder[0])
        head_idx = inorder.index(preorder[0])
        head.left = self.buildTree(preorder[1:head_idx], inorder[: head_idx + 1])
        head.right = self.buildTree(preorder[head_idx + 1 :], inorder[head_idx + 1 :])
        return head
