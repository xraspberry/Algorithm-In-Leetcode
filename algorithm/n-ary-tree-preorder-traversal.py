"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 前序遍历 递归版
        if not root:
            return []
        res = [root.val]
        for child in root.children:
            res.extend(self.preorder(child))
        return res


class Solution1(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 迭代版
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        return res
