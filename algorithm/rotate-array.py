class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        nums_len = len(nums)
        nums[:nums_len-k] = nums[:nums_len-k][::-1]
        nums[nums_len-k:] = nums[nums_len-k:][::-1]
        nums[:] = nums[::-1]


class Solution1(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        nums[:] = nums[nums_len-k:] + nums[:nums_len-k]


class Solution3:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        new_nums = nums.copy()
        for i in range(len(nums)):
            new_nums[(i+k) % nums_len] = nums[i]
        nums[:] = new_nums