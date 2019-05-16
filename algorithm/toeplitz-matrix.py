class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return True
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if row + 1 < rows and col + 1 < cols:
                    if matrix[row][col] != matrix[row+1][col+1]:
                        return False
        return True


if __name__ == '__main__':
    matrix = [
        [1, 2],
        [2, 2]
    ]
    res = Solution().isToeplitzMatrix(matrix)
    print(res)
