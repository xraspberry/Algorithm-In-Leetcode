# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def traverse(self, node):
        if not node:
            return []
        res = [node.val]
        res += self.traverse(node.left)
        res += self.traverse(node.right)
        return res

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """
            2
           / \
          2   5
             / \
            5   7
        5
        """
        values = set(self.traverse(root))
        if len(values) <= 1:
            return -1
        else:
            return sorted(values)[1]


class Solution1:

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """
            2
           / \
          2   5
             / \
            5   7
        5
        """
        if not root:
            return -1
        stack = [root]
        first, second = root.val, -1
        while stack:
            node = stack.pop()
            if node.val < first:
                first = node.val
            elif first < node.val and (node.val < second or second == -1):
                second = node.val
            if node.left:
                stack.append(node.left)
                stack.append(node.right)
        return second
