'''

Given a binary tree, find the leftmost value in the last row of the tree.

https://leetcode.com/problems/find-bottom-left-tree-value/#/description

看清题意很重要哈，是最后一行中最左的数字，刚开始以为是左子节点中最大的。。。看来是困了

那问题就变得简单了，首先找出最后一行的数字，当然找的时候使用中序遍历，这样就可以找到最左边的节点了

Runtime: 76 ms
Your runtime beats 48.44 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionA(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import defaultdict
        res = defaultdict(list)

        def tranverse(node, l):
            if not node:
                return
            tranverse(node.left, l + 1)
            res[l].append(node.val)
            tranverse(node.right, l + 1)

        tranverse(root, 1)
        return res[max(res.keys())][0]


'''
另外看到一个解法，和我的思路差不多，他是遍历每一层，一直到最后一层，最后一层的节点都按从左到右的顺序添加进来

所以最左的那个就是答案
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionB(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        while True:
            newqueue = []
            for item in queue:
                if item.left is not None: newqueue.append(item.left)
                if item.right is not None: newqueue.append(item.right)
            if not newqueue:
                break
            queue = newqueue
        return queue[0].val
