class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        count = 1
        res = 0
        while i < len(nums):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                res = max(res, count)
                count = 1
            i += 1
        else:
            res = max(res, count)
        return res


if __name__ == '__main__':
    nums = [1, 3, 5, 4, 2, 3, 4, 5]
    res = Solution().findLengthOfLCIS(nums)
    print(res)
    assert res == 3

    nums = [2, 2, 2, 2, 2]
    res = Solution().findLengthOfLCIS(nums)
    print(res)
    assert res == 1
