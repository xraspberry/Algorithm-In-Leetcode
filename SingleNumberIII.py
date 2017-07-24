'''

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

Runtime: 62 ms
Your runtime beats 16.87 % of python submissions.

利用集合就可以完成，没有被删除的元素就是只出现了一次的元素
'''


class SolutionA(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        single = set()
        for num in nums:
            if num in single:
                single.remove(num)
            else:
                single.add(num)

        return list(single)

'''
另一种方法就是计数，当数目等于2的时候，将其加入结果
Runtime: 56 ms
Your runtime beats 25.18 % of python submissions.

'''


class SolutionB(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        c = Counter(nums)
        res = []
        for key, value in c.items():
            if value == 1:
                res.append(key)

        return res

'''
另一种使用集合的运算，对称差集，t^s，项在t或者s中，不可能同时存在其中，因此相同的元素会存在其中
只出现一次的元素就不会出现在其中
Runtime: 52 ms
Your runtime beats 35.45 % of python submissions.

'''


class SolutionC(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        snums = set(nums)
        osnums = snums.copy()
        for num in nums:
            snums ^= {num}
        return list(osnums - snums)


if __name__ == "__main__":
    print(SolutionC().singleNumber([1, 2, 1, 3, 2, 5]))
    xor = 0
    for num in [1, 2, 1, 3, 2, 5]:
        xor ^= num
    mask = 1
    while xor & mask == 0:
        mask = mask << 1
    print(mask)
    print(xor)