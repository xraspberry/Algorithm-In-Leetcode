"""
给定一个整数数组 A，对于每个整数 A[i]，我们可以选择任意 x 满足 -K <= x <= K，并将 x 加到 A[i] 中。

在此过程之后，我们得到一些数组 B。

返回 B 的最大值和 B 的最小值之间可能存在的最小差值。



示例 1：

输入：A = [1], K = 0
输出：0
解释：B = [1]
示例 2：

输入：A = [0,10], K = 2
-2-2 8-12
输出：6
解释：B = [2,8]
示例 3：

输入：A = [1,3,6], K = 3
-2-4 0-6 3-9
输出：0
解释：B = [3,3,3] 或 B = [4,4,4]
"""


class Solution:
    """
    也就是说最大值最小，最小值最大，主要是一个数组中有多个数，难以控制哪个会是最终的最大值和最小值
    但是根据分析可以看出只要数组中的数分别加上k，仍然保持交集，那么说明结果就是0，这个也就是说数组最大值和最小值之差不大于2×K，这样就能有交集
    如果没有交集，那么最大值减去K，最小值加上K，两者的差就是最小的差，因为中间的数总能加上一个K到达中间位置。
    """
    def smallestRangeI(self, A, K: int) -> int:
        max_a = max(A)
        min_a = min(A)
        if max_a - min_a < 2 * K:
            return 0
        else:
            return max_a - K - (min_a + K)


if __name__ == '__main__':
    examples = [
        ([1], 0, 0),
        ([0,10], 2, 6),
        ([1,3,6], 3, 0)
    ]
    for example in examples:
        res = Solution().smallestRangeI(example[0], example[1])
        assert res == example[2]
