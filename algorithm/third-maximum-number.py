class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        nums = sorted(set(nums), reverse=True)
        if len(nums) < 3:
            return nums[0]
        else:
            return nums[2]

if __name__ == '__main__':
    nums = [3, 2, 1]
    res = Solution().thirdMax(nums)
    print(res)
    assert res == 1

    nums = [1, 2]
    res = Solution().thirdMax(nums)
    print(res)
    assert res == 2

    nums = [2, 2, 3, 1]
    res = Solution().thirdMax(nums)
    print(res)
    assert res == 1
