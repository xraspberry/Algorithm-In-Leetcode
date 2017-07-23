'''

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

首先思路就是直接找到所有元素，然后在遍历树的时候将比该节点元素大的值求个和加上去就ok，但是超时

没有用到二分搜索树这个条件

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionA(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        values = []

        def get_values(node):
            if not node:
                return
            values.append(node.val)
            get_values(node.left)
            get_values(node.right)

        def tranverse(node):
            if not node:
                return
            tranverse(node.left)
            tranverse(node.right)
            node.val += sum(val for val in values if val > node.val)

        get_values(root)
        tranverse(root)
        return root


'''
下面将从二叉搜索树获取的数据排序，然后在改变节点值的时候，使用了二分搜索，提交accepted了，但是结果感人。。

Runtime: 742 ms
Your runtime beats 3.37 % of python submissions.

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionB(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        import bisect as bi
        values = []

        def get_values(node):
            if not node:
                return
            values.append(node.val)
            get_values(node.left)
            get_values(node.right)

        def tranverse(node):
            if not node:
                return
            tranverse(node.left)
            tranverse(node.right)
            node.val += sum(values[bi.bisect(values, node.val):])

        get_values(root)
        values.sort()
        tranverse(root)
        return root


'''
另外一种思路，就是因为是二分搜索树，所以最右边的节点肯定是最大的，是不需要加的
然后其根节点只需要加上右边节点的值，而左边节点只需要加上根节点的值
在上面的根结点只需要加上上一次左节点的值就可以了
依次递归即可

Runtime: 129 ms
Your runtime beats 49.56 % of python submissions.

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def tranverse(node, s):
            if not node:
                return s
            # 先遍历右边的，最右边的节点是最大的
            rs = tranverse(node.right, s)
            node.val += rs
            # 左侧节点的值，是右侧和根结点值的和
            ls = tranverse(node.left, node.val)
            # 返回右侧子树一堆节点的和
            return ls

        tranverse(root, 0)
        return root


