"""
给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。

二叉搜索树保证具有唯一的值。


示例 1：

输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
输出：32
示例 2：

输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
输出：23
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        if root.val < L:
            res = self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            res = self.rangeSumBST(root.left, L, R)
        else:
            left_res = self.rangeSumBST(root.left, L, root.val)
            right_res = self.rangeSumBST(root.right, root.val, R)
            res = left_res + right_res + root.val
        return res