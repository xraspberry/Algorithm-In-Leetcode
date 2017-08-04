'''

居然惨遭 内存limited， = =！
'''


class SolutionA(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # 先将两两集合的元素分别加起来，最后就是两个集合的元素相加了
        AB = [a + b for a in A for b in B]
        # 保持原来的符号
        CD = [c + d for c in C for d in D]
        return len([0 for ab in AB for cd in CD if ab + cd == 0])


'''

使用生成器而不是列表，TimeLimited = = !
分析以下，时间复杂度应该是n2的
并且内层生成器是在不断的重新制造中，所以是有问题的，但是又不能直接拿出来，因为用一次就用不了了。

所以得另想一个办法
'''


class SolutionB(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # 先将两两集合的元素分别加起来，最后就是两个集合的元素相加了
        # 保持原来的符号
        count = 0
        for ab in (a + b for a in A for b in B):
            for cd in (c + d for c in C for d in D):
                if ab + cd == 0:
                    count += 1
        return count


'''

另一种方法，其实是做了一个优化，就是避免重复的值，只需要将其统计起来就行了
Runtime: 756 ms
Your runtime beats 33.56 % of python submissions.

'''


class SolutionC(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # 先将两两集合的元素分别加起来，最后就是两个集合的元素相加了
        # 保持原来的符号
        count = 0
        # 大部分的值会是重复的，因此只要找到一个，后面跟一个出现了多少次就行了，使用Counter
        # Counter有一个特性，就是没有出现的值，默认值都是0，所以可以直接使用
        from collections import Counter
        AB = Counter(a + b for a in A for b in B)
        # 这个就统计出来CD中是AB的相反数的值，因此只要统计一下和就行了
        return sum(AB[-c - d] for c in C for d in D)

