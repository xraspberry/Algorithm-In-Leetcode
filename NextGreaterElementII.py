'''
https://leetcode.com/problems/next-greater-element-ii/description/

还是遍历，但是两层n2算法扛不住啊
Time Limited
'''


class SolutionA(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 先找后面有没有比它大的，然后如果没有找前面有没有比它大的，如果没有返回-1
        def find_big(n, nums):
            for num in nums:
                if num > n:
                    return [num]
            return []

        res = []
        for index, num in enumerate(nums):
            post = find_big(num, nums[index + 1:])
            if not post:
                pre = find_big(num, nums[:index])
                if not pre:
                    res.append(-1)
                else:
                    res.append(pre[0])
            else:
                res.append(post[0])
        return res


'''
采取了栈这种数据结构，是为了更好的拼接，发现了以下问题

1. 在循环中进行列表的合并 + 操作是非常耗时的

拼接完，但是对于最坏情况其时间复杂度仍然是n2的
'''


class SolutionB(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 先找后面有没有比它大的，然后如果没有找前面有没有比它大的，如果没有返回-1
        def find_big(n, nums):
            for num in nums:
                if num > n:
                    return [num]
            return []

        res = [-1] * len(nums)
        tmp_list = list(nums)
        for index, num in enumerate(nums):
            tmp_list.pop(0)
            ret = find_big(num, tmp_list)
            if ret:
                res[index] = ret[0]
            tmp_list.append(num)
        return res


'''

新的思路，就是用一个栈来保存暂时还没有找到下一个更大元素的元素，其实隐含的意思就是这个栈所保存元素的顺序是按值递减的
要不然就已经找到了，也不会放进来了
Runtime: 295 ms
Your runtime beats 66.67 % of python submissions.

'''


class SolutionC(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 另外一种思路就是，将暂时没有找到比它大的元素先存起来，然后取后面的元素逐渐的去比较
        # 从最近的一个元素进行比较，如果是，则将其从存储的元素去除，然后更新结果集，不用比较前面的，因为最近一个元素肯定是这些元素中最小的了
        # 但是得遍历2倍长度，因为可能需要循环

        res = [-1] * len(nums)
        stack = []
        for i in list(range(len(nums))) * 2:
            # 如果栈里面有元素，则进行比较
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res
