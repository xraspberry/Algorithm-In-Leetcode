'''
https://leetcode.com/problems/range-addition-ii/description/

哈哈，看到了这道题的诀窍哈哈哈哈

其实出现最多的肯定是左上角的元素，那么怎么统计个数呢，画一个图就知道了

重叠最多的数目就是最小的长乘以最小的宽嘛

Runtime: 38 ms
Your runtime beats 91.38 % of python submissions.

'''


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        min_row = min(ops, key=lambda a: a[0])[0]
        min_col = min(ops, key=lambda a: a[1])[1]
        return min_row * min_col
