# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
          4
        /   \
      2      6
     / \
    1   3

[90,69,null,49,89,null,52,null,null,null,null]
"""


class Solution:
    def find_max(self, node):
        while node.right:
            node = node.right
        return node.val

    def find_min(self, node):
        while node.left:
            node = node.left
        return node.val

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        left_max = abs(root.val - self.find_max(root.left)) if root.left else None
        right_min = abs(root.val - self.find_min(root.right)) if root.right else None

        left = self.minDiffInBST(root.left)
        right = self.minDiffInBST(root.right)
        seq = [ele for ele in [left_max, right_min, left, right] if ele is not None]
        if seq:
            return min(seq)


class AnotherSolution:

    def get_values(self, node):
        if not node:
            return []
        values = [node.val]
        values += self.get_values(node.left)
        values += self.get_values(node.right)
        return values

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tree_vals = self.get_values(root)
        dp = []
        tree_vals.sort()
        for i in range(1, len(tree_vals)):
            dp.append(abs(tree_vals[i] - tree_vals[i-1]))
        return min(dp)


if __name__ == '__main__':
    pass
