'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

https://leetcode.com/problems/maximum-subarray/#/description

主要原理:

动态规划

最优子结构,重叠子问题

主要是判断前一个位置的最大子数组之和是正还是负,正则加上当前位置的元素,然后解决后面元素
'''


class Solution(object):
    def max_subarray_iter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {
            0: nums[0]
        }
        res = cache[0]
        for i in range(1, len(nums)):
            if cache[i-1] > 0:
                cache[i] = cache[i - 1] + nums[i]
            else:
                cache[i] = nums[i]
            res = max(cache[i], res)
        return res

    def max_subarray_rec(self, nums):
        from functools import wraps

        def memo_cache(f):
            cache = {}

            @wraps(f)
            def dec(*args):
                if args not in cache:
                    cache[args] = f(*args)
                return cache[args]

            return dec

        @memo_cache
        def dp_solution(i):
            if i == 0:
                return nums[0]
            dp_res = dp_solution(i-1)
            if dp_res > 0:
                res = dp_res + nums[i]
            else:
                res = nums[i]
            return res

        return max(dp_solution(i) for i in range(0, len(nums)))


if __name__ == "__main__":
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.max_subarray_iter(nums))
    print(s.max_subarray_rec(nums))
