'''

https://leetcode.com/problems/count-numbers-with-unique-digits/description/

使用了动态规划，居然也才击败了18%的人，并且跑测试的时候，答案根本输出不出来好伐

Runtime: 42 ms
Your runtime beats 18.05 % of python submissions.

'''


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        dp = {
            1: 10
        }

        from functools import wraps

        def memo(func):
            cache = {}

            @wraps(func)
            def helper(*args):
                if args in cache:
                    return cache[args]
                res = func(*args)
                cache[args] = res
                return res

            return helper

        @memo
        def get_factor(n, time):
            if time <= 0:
                return 1
            return n * get_factor(n - 1, time - 1)

        for i in range(2, n + 1):
            res = 9 * get_factor(9, i - 1)
            dp[i] = res + dp[i - 1]

        return dp[n]


'''
根据题意有很多值得优化的地方，比如阶乘可以直接转成迭代计算，不要用递归
然后最大也不会超过10
'''


class SolutionB(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        dp = {
            1: 10
        }

        cache = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        from operator import mul

        for i in range(2, min(11, n + 1)):
            res = reduce(mul, cache[:i])
            dp[i] = res + dp[i - 1]

        return dp[n]

