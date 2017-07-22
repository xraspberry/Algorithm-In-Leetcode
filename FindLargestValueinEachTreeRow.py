'''

You need to find the largest value in each row of a binary tree.

题目很简单，但是细节处理需要注意
Runtime: 105 ms
Your runtime beats 20.17 % of python submissions.

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionA(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import defaultdict
        import sys

        # 需要取到系统最小值进行比较，但是常规思路不就是将树里面的值赋值，然后和其它的比较，拿到最大值么，，，
        # 哎，学到了
        def missing():
            return -sys.maxint

        max_ = defaultdict(missing)

        def tranverse(node, level):
            if not node:
                return
            if node.val > max_[level]:
                max_[level] = node.val
            tranverse(node.left, level + 1)
            tranverse(node.right, level + 1)

        tranverse(root, 0)
        levels = sorted(list(max_.keys()))
        res = []
        for level in levels:
            res.append(max_[level])
        return res

'''
Runtime: 88 ms
Your runtime beats 35.99 % of python submissions.

'''


class SolutionB(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        max_ = {}

        def tranverse(node, level):
            if not node:
                return
            if level not in max_:
                max_[level] = node.val
            elif node.val > max_[level]:
                max_[level] = node.val
            tranverse(node.left, level + 1)
            tranverse(node.right, level + 1)

        tranverse(root, 0)
        levels = sorted(list(max_.keys()))
        res = []
        for level in levels:
            res.append(max_[level])
        return res