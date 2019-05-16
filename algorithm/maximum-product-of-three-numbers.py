class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from functools import reduce
        positive_nums = [num for num in nums if num > 0]
        negative_nums = [num for num in nums if num < 0]
        if len(negative_nums) % 2 == 0:
            res = negative_nums + positive_nums
        else:
            res = sorted(negative_nums)[:-1] + positive_nums
        return reduce(lambda x, y: x * y, res) if res else 0


if __name__ == '__main__':
    nums = [1, 2, 3]
    res = Solution().maximumProduct(nums)
    print(res)
    assert res == 6

    nums = [1, 2, 3, 4, -3, -4, -5]
    res = Solution().maximumProduct(nums)
    print(res)
    assert res == 24
