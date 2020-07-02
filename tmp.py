from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(root: TreeNode) -> List[int]:
    r = []

    def do(cur):
        r.append(cur.val)
        if cur.left:
            do(cur.left)
        if cur.right:
            do(cur.right)
        return

    do(root)
    return r


def dfs2(root: TreeNode) -> List[int]:
    stack = []
    r = []

    while root or stack:
        if root:
            r.append(root.val)
            if root.right:
                stack.append(root.right)
            root = root.left
        else:
            root = stack.pop()
    return r


def bfs(root: TreeNode) -> List[int]:
    cache = [root]
    r = []

    while cache:
        tmp = []
        for cur in cache:
            r.append(cur.val)
            if cur.left:
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)
        cache = tmp

    return r


a = TreeNode(0)
a.left = TreeNode(1)
a.right = TreeNode(2)
a.left.left = TreeNode(3)
a.left.right = TreeNode(4)
a.right.left = TreeNode(5)
a.right.right = TreeNode(6)
print(dfs(a))
print(dfs2(a))

