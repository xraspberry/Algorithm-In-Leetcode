'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

https://leetcode.com/problems/average-of-levels-in-binary-tree/#/description

这道题涉及到层次，那么我的思路就是给一个变量，只要到下一层，这个变量值就加一，这样就可以知道元素是哪一层的了

然后给一个全局变量(字典)，记录每层有什么元素，使用列表存储，在遍历值的时候，添加进列表

然后到最后对字典中的每一层的列表求平均就可以了，注意sum(val) / len(val) 结果是整数，乘以1.0就可以得到小数了

当然是sum(val) * 1.0 / len(val)

Runtime: 75 ms
Your runtime beats 72.29 % of python submissions
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import defaultdict
        level = defaultdict(list)

        def tranverse(node, l):
            if node is None:
                return
            level[l].append(node.val)
            tranverse(node.left, l + 1)
            tranverse(node.right, l + 1)

        tranverse(root, 1)

        return list(sum(val) * 1.0 / len(val) for val in level.values())
