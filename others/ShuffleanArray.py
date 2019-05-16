'''
https://leetcode.com/problems/shuffle-an-array/description/

这道题同样很懵逼，leetcode出的题就是这么怪异

Runtime: 775 ms
Your runtime beats 68.83 % of python submissions.

'''

from random import shuffle


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self._nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        sf_nums = list(self._nums)
        shuffle(sf_nums)
        return sf_nums



        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()