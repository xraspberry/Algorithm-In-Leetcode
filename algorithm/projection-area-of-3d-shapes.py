class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 俯视图 应该是grid中元素大于1的个数
        # 主视图 应该是grid中纵列中的最大值
        # 侧视图 应该是grid中行的最大值
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        res += sum(max(grid[row]) for row in range(rows))
        res += sum(max(grid[row][col] for row in range(rows)) for col in range(cols))
        res += sum(1 for row in range(rows) for col in range(cols) if grid[row][col])
        return res


if __name__ == '__main__':
    grid = [[1, 0], [0, 2]]
    res = Solution().projectionArea(grid)
    print(res)
    assert res == 8

    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    res = Solution().projectionArea(grid)
    print(res)
    assert res == 14

    grid = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
    res = Solution().projectionArea(grid)
    print(res)
    assert res == 21
