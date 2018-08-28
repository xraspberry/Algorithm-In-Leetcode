class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 26进制？
        col_map = {num: alpha for num, alpha in zip(range(1, 27), [chr(i) for i in range(65, 91)])}
        res = []
        while n > 26:
            n, remain = divmod(n, 26)
            if remain == 0:
                res.append('Z')
                n -= 1
            else:
                res.append(col_map[remain])
        res.append(col_map[n])
        return ''.join(reversed(res))


if __name__ == '__main__':
    n = 52
    res = Solution().convertToTitle(n)
    print(res)
    assert res == "AZ"

    n = 1
    res = Solution().convertToTitle(n)
    print(res)
    assert res == "A"

    n = 28
    res = Solution().convertToTitle(n)
    print(res)
    assert res == "AB"

    n = 701
    res = Solution().convertToTitle(n)
    print(res)
    assert res == "ZY"
