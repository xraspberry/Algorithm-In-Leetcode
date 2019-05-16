'''

Given two binary trees and imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node. Otherwise,
the NOT null node will be used as the node of new tree.

首先不可能使用遍历这种会破坏树的结构，并且并不能通过比如先序遍历结果来还原唯一的一个树

所以必须在不破坏树结构的情况下来做，那么就很简单了，同时对两个树进行遍历：

1. 如果两边都有值，那么就将tree2的值加到tree1上
2. 如果tree1没有值，tree2有值，那么就把tree2的节点放到tree1上
3. 如果tree2没有值，tree1有值，那么保持tree1不变

同样的进行一次先序遍历即可完成

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        # 先将每个树遍历一遍，然后迭代之，itertools.longest
        # 但是一种遍历，比如前序遍历并不能唯一确定一个树，所以要在保持树的结构前提下来合并树

        def merge(tree1, tree2):
            if tree2 is None:
                return tree1
            if tree1 is None:
                return tree2
            if tree1 and tree2:
                tree1.val += tree2.val
            # tree1 和 tree2存在则更新tree1的值，否则将返回存在的节点
            tree1.left = merge(tree1.left, tree2.left)
            tree1.right = merge(tree1.right, tree2.right)
            return tree1

        t1 = merge(t1, t2)
        return t1
