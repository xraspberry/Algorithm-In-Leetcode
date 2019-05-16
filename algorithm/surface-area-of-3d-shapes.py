class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 卧槽，中间有洞没有cover
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                # 上下表面
                if grid[row][col] > 0:
                    res += 2

                # 后表面
                # 后面有低于该正方体柱的
                if row - 1 >= 0 and grid[row-1][col] < grid[row][col]:
                    res += grid[row][col] - grid[row-1][col]
                elif row - 1 < 0:
                    res += grid[row][col]

                # 前表面
                if row + 1 < rows and grid[row+1][col] < grid[row][col]:
                    res += grid[row][col] - grid[row+1][col]
                elif row + 1 >= rows:
                    res += grid[row][col]

                # 左表面
                if col - 1 >= 0 and grid[row][col-1] < grid[row][col]:
                    res += grid[row][col] - grid[row][col-1]
                elif col - 1 < 0:
                    res += grid[row][col]

                # 右表面
                if col + 1 < cols and grid[row][col+1] < grid[row][col]:
                    res += grid[row][col] - grid[row][col+1]
                elif col + 1 >= cols:
                    res += grid[row][col]
        return res


if __name__ == '__main__':
    grid = [[0, 3, 4, 3], [4, 5, 0, 5], [0, 4, 2, 4], [4, 0, 0, 2]]
    res = Solution().surfaceArea(grid)
    print(res)
    assert res == 10
