"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

from collections import defaultdict
class Solution(object):

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        """
        [
             [1],
             [3,2,4],
             [5,6]
        ]
        """
        if not root:
            return []
        queue = [(root, 0)]
        res = defaultdict(list)
        while queue:
            node, level = queue.pop(0)
            res[level].append(node.val)
            for child in node.children:
                queue.append((child, level+1))
        return [res[key] for key in sorted(res.keys())]
