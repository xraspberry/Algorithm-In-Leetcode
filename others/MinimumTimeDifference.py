'''

https://leetcode.com/problems/minimum-time-difference/discuss/

最主要的是首尾要进行比较，否则可能不会发现最小的

Runtime: 102 ms
Your runtime beats 53.49 % of python submissions.

'''


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        # 先将其转换成可以操作的time类型，然后排序，然后按顺序判断就好了
        def convert(time_str):
            # 直接将其转换成距0点的数字好了
            tl = time_str.split(':')
            ret = int(tl[0]) * 60 + int(tl[1])
            return ret

        timePoints = map(convert, timePoints)
        timePoints.sort()
        # 最小的肯定是紧邻的元素,最后会将首尾元素进行比较
        return min((y - x) % (24 * 60) for x, y in zip(timePoints, timePoints[1:] + timePoints[:1]))


