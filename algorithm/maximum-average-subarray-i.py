class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i = k
        start_sum = sum(nums[:k])
        max_average = start_sum / k
        while i < len(nums):
            i = i + 1
            start_sum = start_sum - nums[i - k - 1] + nums[i - 1]
            max_average = max(start_sum / k, max_average)
        return max_average


if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    res = Solution().findMaxAverage(nums, k)
    print(res)
    assert res == 12.75

    nums = [4, 2, 1, 3, 3]
    k = 2
    res = Solution().findMaxAverage(nums, k)
    print(res)
    assert res == 3
