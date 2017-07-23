'''
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

找到中间值即可，问题的转换很重要

Runtime: 52 ms
Your runtime beats 54.45 % of python submissions.

'''


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 首先找到中间元素，也就是值处于中间的
        nums.sort()
        mid = len(nums) // 2
        count = 0
        for ele in nums[:mid] + nums[mid+1:]:
            count += abs(ele - nums[mid])
        return count
