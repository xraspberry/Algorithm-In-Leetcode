# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def _dfs(self, node, value, seen):
        if not node:
            return 0
        seen.add(node)
        if node.val == value:
            count = 1
            left_count = self._dfs(node.left, value, seen)
            right_count = self._dfs(node.right, value, seen)
            count += max(left_count, right_count)
            return count
        return 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
              5
             / \
            4   5
           / \   \
          1   1   5
        2
              1
             / \
            4   5
           / \   \
          4   4   5
        2
        """
        # 从根节点开始找，只要找到与根节点元素相等的值，就加一即可
        if not root:
            return 0
        max_count = 0
        stack = [root]
        seen = set()
        while stack:
            node = stack.pop()
            if node not in seen:
                count = self._dfs(node.left, node.val, seen)
                count += self._dfs(node.right, node.val, seen)
                max_count = max(max_count, count)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return max_count


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):

    def _dfs(self, node, value, seen):
        if not node:
            return 0
        if node.val == value:
            seen.add(node)
            count = 1
            left_count = self._dfs(node.left, value, seen)
            right_count = self._dfs(node.right, value, seen)
            count += max(left_count, right_count)
            return count
        return 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
              5
             / \
            4   5
           / \   \
          1   1   5
        2
              1
             / \
            4   5
           / \   \
          4   4   5
        2
        """
        # 从根节点开始找，只要找到与根节点元素相等的值，就加一即可
        if not root:
            return 0
        max_count = 0
        stack = [root]
        seen = set()
        while stack:
            node = stack.pop()
            if node not in seen:
                count = self._dfs(node.left, node.val, seen)
                count += self._dfs(node.right, node.val, seen)
                max_count = max(max_count, count)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return max_count



