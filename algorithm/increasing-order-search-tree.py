# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def insert_bst(self, node, val):
        if node.val < val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self.insert_bst(node.left, val)
        else:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self.insert_bst(node.right, val)

    def traverse(self, root, values):
        if not root:
            return
        self.traverse(root.left, values)
        values.append(root.val)
        self.traverse(root.right, values)

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        values = []
        self.traverse(root, values)
        bst_root = TreeNode(values[0])
        node = bst_root
        for value in values[1:]:
            node.right = TreeNode(value)
            node = node.right
        return bst_root
