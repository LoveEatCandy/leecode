class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def front_sort(root: TreeNode):
    # 前序：根结点 ---> 左子树 ---> 右子树
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


def front_sort2(root: TreeNode):
    r = []

    def do(cur: TreeNode):
        if cur:
            r.append(cur.val)
            do(cur.left)
            do(cur.right)
    do(root)
    return r


def middle_sort(root: TreeNode):
    # 中序：左子树 ---> 根结点 ---> 右子树
    r = []
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            r.append(root.val)
            root = root.right
    return r


def middle_sort2(root: TreeNode):
    r = []

    def do(cur: TreeNode):
        if cur:
            do(cur.left)
            r.append(cur.val)
            do(cur.right)
    do(root)
    return r


def back_sort(root: TreeNode):
    # 后序：左子树 ---> 右子树 ---> 根结点
    stack1 = [root]
    stack2 = []
    r = []
    while stack1:
        cur = stack1.pop()
        if cur.left:
            stack1.append(cur.left)
        if cur.right:
            stack1.append(cur.right)
        stack2.append(cur)
    while stack2:
        n = stack2.pop()
        r.append(n.val)
    return r


def back_sort2(root: TreeNode):
    r = []

    def do(cur: TreeNode):
        if cur:
            do(cur.left)
            do(cur.right)
            r.append(cur.val)
    do(root)
    return r


i = 0
a = TreeNode(0)
l1, r1 = TreeNode(1), TreeNode(2)
ll, lr, rl, rr = TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
l1.left = ll
l1.right = lr
r1.left = rl
r1.right = rr
a.left = l1
a.right = r1


print(back_sort(a))
print(back_sort2(a))


