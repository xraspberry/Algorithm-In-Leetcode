class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # 双指针法，左边从0开始，右边从sqrt(c)开始
        if c < 0:
            return False
        import math
        sqrt_c = int(math.sqrt(c))
        if sqrt_c ** 2 == c:
            return True
        i, j = 0, sqrt_c
        while i <= j:
            try_res = i ** 2 + j ** 2
            if try_res == c:
                return True
            elif try_res < c:
                i += 1
            else:
                j -= 1
        return False


if __name__ == '__main__':
    c = 6
    res = Solution().judgeSquareSum(c)
    print(res)
    assert res
