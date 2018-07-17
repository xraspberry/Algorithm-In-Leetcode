class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = []
        for s in str:
            ord_s = ord(s)
            if 65 <= ord_s <= 90:
                res.append(chr(ord_s + 32))
            else:
                res.append(s)
        return ''.join(res)


if __name__ == '__main__':
    string = 'Lovely'
    res = Solution().toLowerCase(string)
    print(res)
