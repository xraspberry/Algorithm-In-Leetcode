class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        stop = len(cost)
        dp = {
            0: 0,
            1: 0
        }
        for i in range(2, stop+1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[stop]



if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    res = Solution().minCostClimbingStairs(cost)
    print(res)
    assert res == 6

    cost = [10, 15, 20]
    res = Solution().minCostClimbingStairs(cost)
    print(res)
    assert res == 15
