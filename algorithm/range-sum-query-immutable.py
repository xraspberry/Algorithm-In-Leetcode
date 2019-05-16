class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._dp = {}
        sums = 0
        for idx, num in enumerate(nums):
            sums += num
            self._dp[idx] = sums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self._dp[j]
        return self._dp[j] - self._dp[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    res = obj.sumRange(2, 5)
    print(res)
