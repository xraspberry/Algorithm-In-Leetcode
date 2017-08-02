'''
https://leetcode.com/problems/total-hamming-distance/description/

同样，排列组合，Time Limited

得出一个规律，所有用排列组合的算法，不会accepted，下一次如果有这种思路，直接pass
'''


class SolutionA(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def get_hamming_distance(pair):
            return bin(pair[0] ^ pair[1]).count('1')

        from itertools import combinations
        res = combinations(nums, 2)

        ans = 0
        for pair in res:
            ans += get_hamming_distance(pair)
        return ans

'''
新的算法，仔细考虑下，就能看出来，其实结果相当于独立每一个位的不同的次数之和
比如 110 和 001 每一个位的都有一次不同，所以汉明距离就是3

比如 110, 101, 001 第一个位有1个1，2个0，那么组合起来就是2个不同，第二位同样2个不同，第三位2个1，1个0，也是2个不同

所以综上 6个不同

Runtime: 552 ms
Your runtime beats 40.75 % of python submissions.

'''


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 32位整数
        nums_len = len(nums)
        ans = 0
        ones = [0 for i in range(32)]

        for num in nums:
            zos = bin(num).split('b')[-1]
            for index, zo in enumerate(zos[::-1]):
                if zo == '1':
                    ones[index] += 1
        for o in ones:
            ans += o * (nums_len - o)
        return ans
