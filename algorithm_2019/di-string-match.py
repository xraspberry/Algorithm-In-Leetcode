"""

周内下班后做，果然脑子不太好使。。。
其实思路很简单，就是遇到I的时候把小的数字插入，遇到D的时候把大的数字插入
最后数字肯定会多一个，将剩余的数字extend到列表中就行了
"""


class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        h = len(S)
        l = 0
        res = []
        for s in S:
            if s == 'I':
                res.append(l)
                l += 1
            elif s == 'D':
                res.append(h)
                h -= 1
        res.extend(list(range(l, h+1)))
        return res
