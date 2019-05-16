class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        counter = Counter(nums)
        max_len = 0
        for key, value in counter.items():
            if key + 1 in counter:
                max_len = max(max_len, value + counter[key + 1])
        return max_len


if __name__ == '__main__':
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    res = Solution().findLHS(nums)
    print(res)
    assert res == 5
