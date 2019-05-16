class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A:
            return []
        rows, cols = len(A), len(A[0])
        B = [[0 for _ in range(rows)] for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                if row != col:
                    B[col][row] = A[row][col]
                else:
                    B[row][col] = A[row][col]
        return B

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6]]
    B = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    res = Solution().transpose(A)
    print(res)
    assert res == B
