'''
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

还是一种动态规划的思想吧，从头开始判断，如果前一个元素和当前元素相等，则将两个都置为True，如果不相等，则置为False

最后找到False的key，就是不同元素的位置，当然需要优化，毕竟从value找key，再找元素有点麻烦

Runtime: 42 ms
Your runtime beats 36.83 % of python submissions.

'''


class SolutionA(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cache = {
            0: False
        }
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                cache[i - 1] = True
                cache[i] = True
            else:
                cache[i] = False

        return nums[[key for key, val in cache.items() if not val][0]]

'''
优化的版本，直接在循环时候就判断，特殊情况是最后一个元素是不同的

Runtime: 42 ms
Your runtime beats 36.83 % of python submissions.

'''

class SolutionB(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cache = {
            nums[0]: False
        }
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                cache[nums[i-1]] = True
                cache[nums[i]] = True
            else:
                cache[nums[i]] = False
            if not cache[nums[i]] and not cache[nums[i-1]]:
                return nums[i-1]
        return nums[-1]