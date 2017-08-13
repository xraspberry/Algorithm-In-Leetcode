'''

Given a list of positive integers, the adjacent integers will perform the float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations. You should find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format. Your expression should NOT contain redundant parenthesis.

呃，遇到一道2b题。分析：不论如何第一个数字都是被除数，这个很明显。那么就相当于求从第2个元素开始后面元素的最小值，那么最小值就是，第二个元素依次将后面元素都除掉

那么答案就很明显了，就是括号从第二个元素开始，一直到最后一个元素

注意要处理边界情况，比如只有一个元素，两个元素，就不需要括号了
'''


class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        if len(nums) <= 2:
            return '/'.join(nums)
        return "{}/({})".format(nums[0], '/'.join(nums[1:]))