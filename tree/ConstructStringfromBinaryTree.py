'''

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

由两点，首先分解问题，问题可以变成，根结点(左子树)(右子树)，那么就递归的处理好了
另外左子树是否出现还与是否由右子树有关，所以判断的时候需要加上右子树是否为空
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def tranverse(node):
            if not node:
                return ''
            lf = "({})".format(tranverse(node.left)) if node.left or node.right else ''
            rt = "({})".format(tranverse(node.right)) if node.right else ''
            return "{}{}{}".format(node.val, lf, rt)

        return tranverse(t)