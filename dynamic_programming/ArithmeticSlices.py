'''

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

https://leetcode.com/problems/arithmetic-slices/#/description

错了2次，用的是动态规划的思路，但是最后超时，是因为没有加缓存吗？

Time Limit Exceeded
'''


class SolutionA(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        def judge(s):
            if len(s) < 3:
                return False
            equal = 0
            len_S = len(s)
            for i in range(1, len_S):
                if i == 1:
                    equal = s[i] - s[0]
                    continue
                if s[i] - s[i - 1] == equal:
                    continue
                else:
                    return False
            return True

        count = [0]

        def find_slices(S):
            if len(S) <= 3:
                if judge(S):
                    count[0] += 1
                return
            for j in range(len(S) - 3, -1, -1):
                if judge(S[j:]):
                    count[0] += 1
            find_slices(S[:-1])

        find_slices(A)
        return count[0]


'''
Runtime: 38 ms
Your runtime beats 63.96 % of python submissions.

'''


class SolutionB(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 我去，典型的动态规划，我居然没有想到从头往尾来考虑，只是想着从尾到头递归了

        cache = {
            0: 0,
            1: 0
        }
        i = 1
        for j in range(2, len(A)):
            if A[j] - A[j - 1] == A[j - 1] - A[j - 2]:
                cache[j] = cache[j - 1] + i
                i += 1
            else:
                cache[j] = cache[j - 1]
                i = 1

        return cache[len(A) - 1] if (len(A) - 1) in cache else 0
