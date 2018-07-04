class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = None
        while n != 0:
            n, remain = divmod(n, 2)
            if last is not None:
                if remain == last:
                    return False
            last = remain
        return True


if __name__ == '__main__':
    print(Solution().hasAlternatingBits(3))
