class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        if len(nums) < 2:
            return 0
        i, j = 0, 1
        res = set()
        while i < len(nums) and j < len(nums):
            if i == j:
                j += 1
                continue
            while i < len(nums) and j < len(nums) and abs(nums[j] - nums[i]) < k:
                j += 1
            if j >= len(nums):
                break
            if abs(nums[j] - nums[i]) == k:
                res.add((nums[j], nums[i]))
            i += 1
        return len(res)


if __name__ == '__main__':
    nums = [3, 1, 4, 1, 5]
    k = 2
    res = Solution().findPairs(nums, k)
    print(res)
    assert res == 2

    nums = [1, 2, 3, 4, 5]
    k = 1
    res = Solution().findPairs(nums, k)
    print(res)
    assert res == 4

    nums = [1, 3, 1, 5, 4]
    k = 0
    res = Solution().findPairs(nums, k)
    print(res)
    assert res == 1

    nums = [1, 2, 3, 4, 5]
    k = 0
    res = Solution().findPairs(nums, k)
    print(res)
    assert res == 0
