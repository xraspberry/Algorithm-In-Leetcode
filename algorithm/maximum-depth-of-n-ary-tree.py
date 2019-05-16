"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def dfs(self, node, depth):
        max_depth = depth
        for child in node.children:
            max_depth = max(max_depth, self.dfs(child, depth+1))

        return max_depth

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        depth = self.dfs(root, 1)
        return depth


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        if not root.children:
            return 1
        return max(map(self.maxDepth, root.children)) + 1


if __name__ == '__main__':
    pass
