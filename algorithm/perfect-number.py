class Solution1(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        i = 1
        total = 0
        half_num = num // 2
        while i <= half_num:
            if num % i == 0:
                total += i
            i += 1
        if total == num:
            return True
        return False


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        if num <= 0:
            return False
        i = 1
        total = 0
        s_num = int(math.sqrt(num))
        if s_num == num:
            return False
        while i <= s_num:
            if num % i == 0:
                total += i + num / i
            i += 1
        if total != 2 * num:
            return False
        return True


if __name__ == '__main__':
    num = 28
    res = Solution().checkPerfectNumber(num)
    print(res)
    assert res

    num = 13466917
    res = Solution().checkPerfectNumber(num)
    print(res)
    assert not res
