class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 9 9*20 9*300
        if n < 10:
            return n
        digit_type = 1
        digit_num = 9
        while n > digit_num * digit_type:
            n -= digit_num * digit_type
            digit_type += 1
            digit_num *= 10
        # 第x个数字
        index_in_sub_range = (n - 1) // digit_type
        # 第x个数字第y位
        index_in_num = (n - 1) % digit_type
        # 因为x从0开始，所以从10**(digit_type-1)开始加
        return int(str(10 ** (digit_type - 1) + index_in_sub_range)[index_in_num])


if __name__ == '__main__':
    n = 102
    res = Solution().findNthDigit(n)
    print(res)
    assert res == 0
    # 12->11
    # 14->12
    # 16->13
    # 102
