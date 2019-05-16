class Solution:
    def traverse(self, node):
        if not node:
            return []
        res = [node]
        res += self.traverse(node.left)
        res += self.traverse(node.right)
        return res

    def search(self, node, target):
        if not node:
            return
        if node.val == target:
            return node
        elif node.val < target:
            return self.search(node.right, target)
        else:
            return self.search(node.left, target)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # 遍历tree，随便拿一个元素，然后在bst中找另一个元素
        for ele in self.traverse(root):
            another = k - ele.val
            node = self.search(root, another)
            if node is None or node == ele:
                continue
            else:
                return True
        return False


if __name__ == '__main__':
    pass

    """
    输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
"""