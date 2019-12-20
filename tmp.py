# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_father, q_father = None, None

        def get_node(cur, father_list):
            if cur == p:
                p_father = father_list
            elif cur == q:
                q_father = father_list
            if p_father and q_father:
                return
            else:
                if cur.left:
                    cur_list = father_list + [cur]
                    get_node(cur.left, cur_list)
                if cur.right:
                    cur_list = father_list + [cur]
                    get_node(cur.right, cur_list)
        get_node(root, [])

        i = 0
        last = None
        while True:
            if p_father[i] == q_father[i]:
                last = p_father[i]
            else:
                break
            i += 1
        return last

