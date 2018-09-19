class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(A) - 1
        while i < j:
            while i < j and A[i] % 2 == 0:
                i += 1
            while i < j and A[j] % 2 != 0:
                j -= 1
            if i >= j:
                break
            A[i], A[j] = A[j], A[i]
        return A


if __name__ == '__main__':
    A = [3, 1, 2, 4]
    res = Solution().sortArrayByParity(A)
    print(res)
    assert res == [2, 4, 3, 1]
