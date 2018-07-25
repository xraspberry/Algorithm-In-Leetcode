class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        1 
            1
        2 
            1 1
            2
        3
            2
                1 2
            1
                1 1 1
                2 1
        4
            1
                1 1 1 1
                1 2 1
                2 1 1
            2
                1 1 2
                2 2
        """
        dp = {
            1: 1,
            2: 2
        }
        for i in range(3, n+1):
            # 其实就是上第i-1个台阶的不同方法加上 上第i-2个台阶的方法次数只和
            # 因为如果上到i-2，差两个台阶上到i的可能次数
            # 如果上到i-1，就是差一个台阶上到i的可能次数
            # 比如n=4，差一个台阶上来的可能性为，也就是说末尾数字是1，则可能有 1111 121 211 即n=3的可能性
            # 差两个台阶上来的可能性为，就是末尾数字是2，可能有 22 112 即为n=2的可能性
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
