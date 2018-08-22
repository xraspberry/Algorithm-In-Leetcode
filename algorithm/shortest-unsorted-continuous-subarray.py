class Solution1(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        start = 0
        # 找到第一个下降的
        while i < len(nums):
            if nums[i] < nums[i - 1]:
                break
            elif nums[i] > nums[i - 1]:
                start = i
            i += 1
        if start >= len(nums):
            return 0
        # 找到第一个上升的
        j = len(nums) - 2
        end = len(nums) - 1
        while j >= 0:
            if nums[j] > nums[j + 1]:
                break
            elif nums[j] < nums[j + 1]:
                end = j
            j -= 1
        if start >= end or nums[start] == nums[end]:
            return 0
        return end - start + 1


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        i, j = 0, len(nums) - 1
        while i < len(nums):
            if nums[i] != sorted_nums[i]:
                break
            i += 1
        if i >= len(nums):
            return 0
        while j >= 0:
            if nums[j] != sorted_nums[j]:
                break
            j -= 1
        if i >= j:
            return 0
        return j - i + 1

if __name__ == '__main__':
    nums = [1, 2, 4, 5, 3]
    res = Solution().findUnsortedSubarray(nums)
    print(res)
    assert res == 3

    nums = [1, 1]
    res = Solution().findUnsortedSubarray(nums)
    print(res)
    assert res == 0

    nums = [2, 6, 4, 8, 10, 9, 15]
    res = Solution().findUnsortedSubarray(nums)
    print(res)
    assert res == 5

    nums = [1, 2, 3, 4]
    res = Solution().findUnsortedSubarray(nums)
    print(res)
    assert res == 0

    nums = [2, 1]
    res = Solution().findUnsortedSubarray(nums)
    print(res)
    assert res == 2

    nums = [1, 3, 2, 2, 2]
    res = Solution().findUnsortedSubarray(nums)
    print(res)
    assert res == 4

    nums = [1, 3, 2, 3, 3]
    res = Solution().findUnsortedSubarray(nums)
    print(res)
    assert res == 2
