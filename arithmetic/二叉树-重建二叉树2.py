'''
输入某二叉树的后序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

后序遍历 post_order =[9,15,7,20,3]
中序遍历 in_order = [9,3,15,20,7]
如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

返回层级遍历结果：[3, 9, 20, 15, 7]
'''


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(post_order, in_order):
    if not post_order:
        return None
    head = Node(post_order[0])
    head_idx = in_order.index(post_order[0])
    post_head_idx = len(post_order) - head_idx
    head.left = build_tree(post_order[1:post_head_idx], in_order[head_idx + 1:])
    head.right = build_tree(post_order[post_head_idx:], in_order[:head_idx])
    return head


def get_traverse(root):
    r = []
    stack = [root]
    while stack:
        node = stack.pop()
        r.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return r


def main(post_order, in_order):
    root = build_tree(post_order[::-1], in_order)
    return get_traverse(root)


if __name__ == '__main__':
    print(main([9, 15, 7, 20, 3], [9, 3, 15, 20, 7]))
