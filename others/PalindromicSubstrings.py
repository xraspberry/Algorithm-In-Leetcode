'''

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

做了一道新题，排名倒数第一
Runtime: 1246 ms

'''


class SolutionA(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def judge(s):
            return s == s[::-1]

        count = len(s)
        for index, ele in enumerate(s):
            for j in range(1, len(s[index:])):
                if judge(s[index:index + j + 1]):
                    count += 1

        return count

'''
修正了下，成了第一名了，但还是O(n2)算法
Runtime: 965 ms
Your runtime beats 100.00 % of python submissions.

'''


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = len(s)
        for index, ele in enumerate(s):
            for j in range(1, len(s[index:])):
                fs = s[index:index + j + 1]
                if fs[0] == fs[-1] and fs == fs[::-1]:
                    count += 1

        return count