'''

添加不难，但是坑很多，而且刚开始没有完全理解题意，错了好几次，好方

主要在 depth=1，即在root前面插入
depth在最后，即在最后插入

Runtime: 78 ms
Your runtime beats 56.96 % of python submissions.

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """

        def tranverse(node, depth):
            if not node:
                return
            if depth == d - 1:
                # 到了要插入的深度的时候
                if node.left:
                    ori = node.left
                    node.left = TreeNode(v)
                    node.left.left = ori
                else:
                    node.left = TreeNode(v)
                if node.right:
                    ori = node.right
                    node.right = TreeNode(v)
                    node.right.right = ori
                else:
                    node.right = TreeNode(v)
            tranverse(node.left, depth + 1)
            tranverse(node.right, depth + 1)

        if d == 1:
            tmp_node = root
            root = TreeNode(v)
            root.left = tmp_node
        else:
            tranverse(root, 1)

        return root

