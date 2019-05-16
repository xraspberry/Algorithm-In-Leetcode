
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_tree(pre_seq, mid_seq, tree, left):
    """前序遍历第一个节点就是根节点，在中序遍历里面，1左边的节点都是左子树的节点，右边是右子树的节点
    那么根据相应的前序遍历结果确定左子树和右子树，递归处理"""
    if not pre_seq or not mid_seq:
        return

    root_val = pre_seq[0]
    _next = Node(root_val)
    if left:
        tree.left = _next
    else:
        tree.right = _next

    root_pos = mid_seq.index(root_val)
    left_mid_seq = mid_seq[:root_pos]
    right_mid_seq = mid_seq[root_pos+1:]

    left_pre_seq = pre_seq[1:len(left_mid_seq)+1]
    right_pre_seq = pre_seq[len(left_mid_seq)+1:]

    construct_tree(left_pre_seq, left_mid_seq, _next, left=True)
    construct_tree(right_pre_seq, right_mid_seq, _next, left=False)


if __name__ == "__main__":
    pre_seq = [1, 2, 4, 7, 3, 5, 6, 8]
    mid_seq = [4, 7, 2, 1, 5, 3, 8, 6]

    tree = Node(pre_seq[0])
    root_pos = mid_seq.index(pre_seq[0])
    left_mid_seq = mid_seq[:root_pos]
    right_mid_seq = mid_seq[root_pos + 1:]

    left_pre_seq = pre_seq[1:len(left_mid_seq)+1]
    right_pre_seq = pre_seq[len(left_mid_seq) + 1:]
    construct_tree(left_pre_seq, left_mid_seq, tree, left=True)
    construct_tree(right_pre_seq, right_mid_seq, tree, left=False)

    print("pre order")

    # 前序遍历
    def traverse_pre(root):
        if root is None:
            return
        print(root.val)
        traverse_pre(root.left)
        traverse_pre(root.right)

    traverse_pre(tree)

    print("mid order")

    # 中序遍历
    def traverse_mid(root):
        if root is None:
            return
        traverse_mid(root.left)
        print(root.val)
        traverse_mid(root.right)

    traverse_mid(tree)

    print("post order")

    # 后序遍历
    def traverse_post(root):
        if root is None:
            return
        traverse_post(root.left)
        traverse_post(root.right)
        print(root.val)

    traverse_post(tree)

