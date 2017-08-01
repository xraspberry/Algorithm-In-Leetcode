'''
https://leetcode.com/problems/top-k-frequent-elements/description/

这道题完美的使用了Counter

当然也可以自己写字典计数
Runtime: 66 ms
Your runtime beats 69.38 % of python submissions.

'''


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        c = Counter(nums)
        return [ele[0] for ele in c.most_common(k)]