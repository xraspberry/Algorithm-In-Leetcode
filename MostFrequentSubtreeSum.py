'''

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

使用遍历，然后超时
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionA(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        from collections import Counter
        cache = Counter()
        def tranverse(node):
            if not node:
                return 0
            sum_l = tranverse(node.left)
            sum_r = tranverse(node.right)
            s = sum_l + sum_r + node.val
            cache[s] += 1
            return s
        tranverse(root)
        return [key for key in cache.keys() if cache[key] == max(cache.values())]  # 这里有问题。。


'''
超时的原因是在列表推导式里面不断的去执行了一个操作max(cache.values()) 我的天！！
Runtime: 89 ms
Your runtime beats 65.02 % of python submissions.

教训就是减少赋值操作，减少循环里面执行的操作
'''


class SolutionB(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        from collections import Counter
        cache = Counter()
        def tranverse(node):
            if not node:
                return 0
            s = tranverse(node.left) + tranverse(node.right) + node.val
            cache[s] += 1
            return s
        tranverse(root)
        frequent = max(cache.values())
        return [key for key in cache.keys() if cache[key] == frequent]
