'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

https://leetcode.com/problems/counting-bits/#/description

铁定用位运算了,主要是要发现规律,找到这个递推公式,用动态规划也是显而易见的

dp[0] = 0 0
dp[1] = 1 01
dp[2] = 1 10
dp[3] = 2 11
dp[4] = 1 100
dp[5] = 2 101
dp[6] = 2 110
dp[7] = 3 111

从0推到1,已知条件,0,1的二进制,0中包含1的个数,可以看出来当1和0进行与运算后的值加上0的结果就是 1中包含1的个数,另外因为与这种运算肯定不会超过现在出现过的最大值

从1推到2,dp[(2 & 1)] + 1 = 1
从2推到3,dp[(3 & 2)] + 1 = 2
...

感觉吧,也许没什么特定的含义,但是有规律可言,找到已知条件,运用什么方法,基本就OK了
'''


class Solution(object):
    def count_bits_iter(self, num):
        """
        :type num: int
        :rtype: List[int]
        Runtime: 189 ms
        Your runtime beats 88.26 % of python submissions
        """
        cache = {0: 0}
        for i in range(1, num+1):
            cache[i] = cache[(i & (i-1))] + 1
        return list(cache.values())

    def count_bits_rec(self, num):
        '''
        没有cache的时候
        Runtime: 518 ms
        Your runtime beats 4.50 % of python submissions.
        有cache的时候
        Runtime: 329 ms
        Your runtime beats 13.18 % of python submissions.
        :param num:
        :return:
        '''
        from functools import update_wrapper

        def memo_cache(f):
            cache = {}

            def wrapper(*args):
                if args not in cache:
                    cache[args] = f(*args)
                return cache[args]
            return update_wrapper(wrapper, f)

        @memo_cache
        def dp_solution(num):
            if num == 0:
                return 0
            res = dp_solution((num-1) & num)
            return res + 1

        return [dp_solution(i) for i in range(num+1)]


if __name__ == "__main__":
    s = Solution()
    print(s.count_bits_iter(7))
    print(s.count_bits_rec(7))
