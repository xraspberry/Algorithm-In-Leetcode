'''

https://leetcode.com/problems/binary-tree-inorder-traversal/description/

最近的题是越来越简单了吗？中序遍历，10s中完成

Runtime: 36 ms
Your runtime beats 58.04 % of python submissions.

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def tranverse(node):
            if node is None:
                return
            tranverse(node.left)
            res.append(node.val)
            tranverse(node.right)

        tranverse(root)
        return res


'''
题目还说是要用迭代的方法处理，无非就是加一个栈，因为递归也是自己有一个栈嘛
Runtime: 29 ms
Your runtime beats 98.07 % of python submissions.

我擦，迭代的效率不知道高到哪里去了，以后还是尽量不要用递归，能用迭代就用迭代。。。虽然不好写，不如递归容易理解
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = []
        while 1:
            # 一直添加左侧节点,因为是中序遍历，所以首先来遍历左节点
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            # 取出最后一个左节点，加入res
            node = stack.pop()
            res.append(node.val)
            # 然后开始找最后一个左节点的右节点，因为最后一个左节点的左节点是None，也就相当于它是根节点
            root = node.right
