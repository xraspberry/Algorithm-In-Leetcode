import math
import copy
class Solution:

    def gen_inner_result(self, row, col, col_len, count, value):
        count += 1
        value += M[row][col]
        if col - 1 >= 0:
            count += 1
            value += M[row][col - 1]
        if col + 1 < col_len:
            count += 1
            value += M[row][col + 1]
        return count, value

    def gen_result(self, row, col, row_len, col_len):
        count = value = 0
        if row - 1 >= 0:
            count, value = self.gen_inner_result(row-1, col, col_len, count, value)
        if row + 1 < row_len:
            count, value = self.gen_inner_result(row+1, col, col_len, count, value)
        count, value = self.gen_inner_result(row, col, col_len, count, value)
        return int(math.floor(value / count))

    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if not M:
            return M
        self.M = M
        res_M = copy.deepcopy(M)
        for row in range(len(M)):
            for col in range(len(M[0])):
                res_M[row][col] = self.gen_result(row, col, len(M), len(M[0]))
        return res_M

if __name__ == '__main__':
    M = [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]]
    res = Solution().imageSmoother(M)
    print(res)
    assert res == [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
