'''
Given a string, sort it in decreasing order based on the frequency of characters.

一如既往的计数，这次被Counter坑了一次，以为sorted(c.elements())会是按照个数大小排序，我错了。。。
Runtime: 99 ms
Your runtime beats 56.07 % of python submissions.

'''


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        c = Counter(s)
        return ''.join(list(map(lambda a: a[1] * a[0], sorted(c.items(), key=lambda s: s[1], reverse=True))))

