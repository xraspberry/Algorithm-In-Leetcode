# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def dfs(self, node):
        res = []
        leaf = True
        if node.left:
            leaf = False
            res.extend(self.dfs(node.left))
        if node.right:
            leaf = False
            res.extend(self.dfs(node.right))
        if leaf:
            res.append(node.val)
        return res

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf_nodes_1 = self.dfs(root1)
        leaf_nodes_2 = self.dfs(root2)
        return leaf_nodes_1 == leaf_nodes_2

