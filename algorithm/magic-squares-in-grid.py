class Solution(object):
    def is_magic_squre(self, i, j, grid):
        for iter_i in range(i, i+3):
            for iter_j in range(j, j+3):
                if grid[iter_i][iter_j] > 9 or grid[iter_i][iter_j] < 1 :
                    return False
        res = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        if grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] != res:
            return False
        if grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] != res:
            return False
        if grid[i][j] + grid[i+1][j] + grid[i+2][j] != res:
            return False
        if grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] != res:
            return False
        if grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] != res:
            return False
        if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != res:
            return False
        if grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2] != res:
            return False
        return True

    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(0, len(grid)-2):
            for j in range(0, len(grid[0])-2):
                if self.is_magic_squre(i, j, grid):
                    count += 1
        return count


if __name__ == '__main__':
    grid = [[4, 3, 8, 4],
            [9, 5, 1, 9],
            [2, 7, 6, 2]]
    res = Solution().numMagicSquaresInside(grid)
    print(res)
    assert res == 1

    grid = [[10, 3, 5],
            [1, 6, 11],
            [7, 9, 2]]
    res = Solution().numMagicSquaresInside(grid)
    print(res)
    assert res == 0
