class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        i = 0
        while i < len(B):
            if B[i] == A[0] and B[i:] + B[:i] == A:
                return True
            i += 1
        return False


if __name__ == '__main__':
    A = 'abcde'
    B = 'cdeab'
    res = Solution().rotateString(A, B)
    print(res)
    assert res

    A = 'abcde'
    B = 'abced'
    res = Solution().rotateString(A, B)
    print(res)
    assert not res
