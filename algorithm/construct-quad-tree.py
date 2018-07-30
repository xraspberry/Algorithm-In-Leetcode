"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):

    def build_tree(self, rect):
        dup = set()
        row_len, col_len = len(rect), len(rect[0])
        row_mid, col_mid = row_len // 2, col_len // 2
        top_left_rect = []
        top_right_rect = []
        bottom_right_rect = []
        bottom_left_rect = []
        for row in range(row_mid):
            dup |= set(ele for ele in rect[row])
            top_left_rect.append(rect[row][0:col_mid])
            top_right_rect.append(rect[row][col_mid:])

        for row in range(row_mid, row_len):
            dup |= set(ele for ele in rect[row])
            bottom_left_rect.append(rect[row][0:col_mid])
            bottom_right_rect.append(rect[row][col_mid:])

        if len(dup) == 1:
            return Node(
                val=bool(dup.pop()), isLeaf=True, topLeft=None,
                topRight=None, bottomLeft=None, bottomRight=None
            )

        top_left = self.build_tree(top_left_rect)
        top_right = self.build_tree(top_right_rect)
        bottom_left = self.build_tree(bottom_left_rect)
        bottom_right = self.build_tree(bottom_right_rect)
        node = Node(
            val=True, isLeaf=False, topLeft=top_left,
            topRight=top_right, bottomLeft=bottom_left,
            bottomRight=bottom_right
        )
        return node

    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if not grid:
            return
        return self.build_tree(grid)

if __name__ == '__main__':
    grid = [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]
    res = Solution().construct(grid)
