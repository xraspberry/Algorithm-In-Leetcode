"""
1.     1
2.     11
3.     21
4.     1211
5.     111221
6.     2111121211
7.     12212112111221
"""


class Solution:
    def build(self, string):
        current = '#'
        count = 0
        res = ''
        for i in string:
            # 如果遍历字符和current记录中的不一样，则有可能是刚开始，也可能是一串相等数字的结束，
            # 如果是结束，则current就不等于#，这样将上一串数字结果加入到res
            # 然后将current置为当前数字，并且count置为1
            if i != current:
                if current != '#':
                    res += str(count) + current
                current = i
                count = 1
            else:
                count += 1
        res += str(count) + current
        return res

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = '1'
        for i in range(2, n+1):
            string = self.build(string)
        return string


if __name__ == '__main__':
    n = 10
    res = Solution().countAndSay(n)
    print(res)
