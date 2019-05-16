class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pos = {}
        for idx, num in enumerate(nums):
            if num in pos:
                if idx - pos[num] <= k:
                    return True
            pos[num] = idx
        return False


if __name__ == '__main__':
    nums = [99, 99]
    k = 2
    res = Solution().containsNearbyDuplicate(nums, k)
    print(res)
    assert res

    nums = [1, 2, 3, 1]
    k = 3
    res = Solution().containsNearbyDuplicate(nums, k)
    print(res)
    assert res

    nums = [1, 0, 1, 1]
    k = 1
    res = Solution().containsNearbyDuplicate(nums, k)
    print(res)
    assert res

    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    res = Solution().containsNearbyDuplicate(nums, k)
    print(res)
    assert not res
