from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        quene = [root]
        r = []
        left = True
        while quene:
            tmp = []
            cur = []
            for node in quene:
                cur.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if not left:
                cur.reverse()
            r.append(cur)
            left = not left
            quene = tmp
        return r
