'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cache = []
        cur_list = [root]
        r = []
        cur = 0
        tmp = []

        while cur_list or cache:

            if cur_list:
                if cur == 0:
                    node = cur_list.pop(0)
                    if node.left:
                        cache.append(node.left)
                    if node.right:
                        cache.append(node.right)
                else:
                    node = cur_list.pop()
                    if node.right:
                        cache.insert(0, node.right)
                    if node.left:
                        cache.insert(0, node.left)
                tmp.append(node.val)
            else:
                r.append(tmp)
                cur_list, cache, tmp = cache, [], []
                cur = 1 if cur == 0 else 0
        return r