# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        """
                4
               / \
              2   7
             / \
            1   3
        
        和值: 2
        """
        if not root:
            return
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val == val:
                return node
            elif val < node.val and node.left:
                queue.append(node.left)
            elif val > node.val and node.right:
                queue.append(node.right)
