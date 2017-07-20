'''

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

这个问题也就是统计频率，可以自己实现字典来搞，也可以使用Counter来搞，相当于Counter直接就形成了最终的字典

但是题目所说不用额外的空间，并且最多只会出现两次，那么可以先对序列进行排序，然后再进行比较，所以对于序列，排序是一个比较好的思路了

Runtime: 382 ms
Your runtime beats 34.73 % of python submissions.
'''


class SolutionA(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        c = Counter(nums)
        res = [ele for ele in c if c[ele] > 1]
        return res


'''
Runtime: 345 ms
Your runtime beats 54.75 % of python submissions.
'''


class SolutionB(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                res.append(nums[i])
        return res

