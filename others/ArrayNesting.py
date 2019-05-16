'''
https://leetcode.com/problems/array-nesting/#/description

有一个关键点一定要领悟到，就是这种一定是循环的，所以可以跳过之后的许多次遍历, 所以要有一种标记表明这个元素已经被用过了
如果没有用过然后再遍历

Runtime: 152 ms
'''


class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = [False] * len(nums)
        max_ = 0
        for index, i in enumerate(nums):
            res = set()
            pos = index
            start = nums[pos]
            while not seen[pos]:
                seen[pos] = True
                res.add(start)
                pos = start
                start = nums[start]
            max_ = max(max_, len(res))

        return max_

if __name__ == "__main__":
    b = Solution().arrayNesting([5,4,0,3,1,6,2])
    print(b)
