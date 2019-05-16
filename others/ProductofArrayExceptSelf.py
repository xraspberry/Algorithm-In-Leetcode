'''
https://leetcode.com/problems/product-of-array-except-self/description/

小小一道题居然有这么多坑，哎，还好，超越了70%的提交，但是代码写的烂啊
'''


'''
最开始的提交，自以为写的很吊，超时，原因是做了很多无用功
'''


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from operator import mul
        from functools import reduce
        return list(map(lambda x: reduce(mul, nums[:x] + nums[x+1:]), range(len(nums))))


'''
accepted，但是代码很烂

Runtime: 159 ms
Your runtime beats 70.35 % of python submissions.

'''


class SolutionB(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        from operator import mul
        from functools import reduce
        if nums.count(0) > 1:
            return [0 for i in range(len(nums))]

        without_0 = [num for num in nums if num != 0]
        if without_0:
            all_result_except_0 = reduce(mul, without_0)
        else:
            all_result_except_0 = 0
        all_result = reduce(mul, nums)
        res = []
        for index, num in enumerate(nums):
            if num == 0:
                res.append(all_result_except_0)
            else:
                ret = all_result / num
                res.append(ret)
        return res


'''
分析了一下，也就四种情况，nums为空，nums里面多于1个0，nums只有一个0，nums没有0

分情况处理呗

Runtime: 149 ms
Your runtime beats 92.75 % of python submissions.

'''


class SolutionC(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        elif nums.count(0) > 1:
            return [0 for i in range(len(nums))]
        elif nums.count(0) == 1:
            from operator import mul
            from functools import reduce
            # 如果只含有一个0，那么0的位置的乘积就是其他非0元素的乘积，其他位置都是0
            pos = nums.index(0)
            res = [0 for i in range(len(nums))]
            res[pos] = reduce(mul, [num for num in nums if num != 0])
            return res
        else:
            from operator import mul
            from functools import reduce

            all_result = reduce(mul, nums)
            res = []
            for index, num in enumerate(nums):
                ret = all_result / num
                res.append(ret)
            return res
