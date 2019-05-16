'''

In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.

两种情况，一种是起点加上duration小于第二个时间点，那么全部计入，如果大于则总时间减去第二个时间点
Runtime: 109 ms
Your runtime beats 35.40 % of python submissions.

'''


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries or duration <= 0:
            return 0
        count = 0
        for i in range(len(timeSeries)):
            if i == len(timeSeries) - 1:
                count += duration
                return count
            if timeSeries[i] + duration <= timeSeries[i+1]:
                count += duration
            else:
                count += timeSeries[i+1] - timeSeries[i]

