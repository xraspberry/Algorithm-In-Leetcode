"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 左->右->中间
        if not root:
            return []
        res = []
        for child in root.children:
            res += self.postorder(child)
        res.append(root.val)
        return res

    def postorder_iter(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        # 迭代法就是自己模拟栈
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            for child in node.children:
                stack.append(child)
            # res添加的顺序正好和后序遍历相反
            # 即先进入节点值，再进入的是右边子节点，所以后面直接逆序即可
            res.append(node.val)
        return res[::-1]
