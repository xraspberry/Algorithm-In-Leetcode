class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        if str_x.startswith('-'):
            res = '-' + str_x[1:][::-1].lstrip('0')
        else:
            res = str_x[::-1].lstrip('0')
        res = int(res)
        if -2147483648 > res or res > 2147483647:
            return 0
        return res

if __name__ == '__main__':
    x = 123
    res = Solution().reverse(x)
    print(res)
    assert res == 321

    x = -123
    res = Solution().reverse(x)
    print(res)
    assert res == -321

    x = -120
    res = Solution().reverse(x)
    print(res)
    assert res == -21

    x = 1534236469
    res = Solution().reverse(x)
    print(res)
    assert res == 0
