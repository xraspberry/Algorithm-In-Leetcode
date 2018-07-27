class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        max_num = second_max_num = None
        i = 0
        while i < len(nums):
            if max_num is None:
                max_num = nums[i], i
            elif nums[i] > max_num[0]:
                second_max_num = max_num
                max_num = nums[i], i
            elif second_max_num is None:
                second_max_num = nums[i], i
            elif nums[i] > second_max_num[0]:
                second_max_num = nums[i], i
            i += 1
        if second_max_num[0] == 0 or max_num[0] / second_max_num[0] >= 2:
            return max_num[1]
        else:
            return -1


if __name__ == '__main__':
    nums = [1]
    res = Solution().dominantIndex(nums)
    print(res)
    assert res == 1
