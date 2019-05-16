class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        j = int(c ** 0.5)
        while i <= j:
            sum_of = i ** 2 + j ** 2
            if sum_of == c:
                return True
            elif sum_of < c:
                i += 1
            else:
                j -= 1
        return False


if __name__ == '__main__':
    target = 10000000
    res = Solution().judgeSquareSum(target)
    print(res)
