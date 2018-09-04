class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if A[0] == A[-1]:
            for a in A[1:-1]:
                if a != A[0]:
                    return False
            return True
        elif A[0] < A[-1]:
            increase = True
        else:
            increase = False
        i = 1
        while i < len(A):
            if A[i] < A[i-1] and increase:
                return False
            elif A[i] > A[i-1] and not increase:
                return False
            i += 1
        return True


if __name__ == '__main__':
    A = [1, 2, 2, 3]
    res = Solution().isMonotonic(A)
    print(res)
    assert res
