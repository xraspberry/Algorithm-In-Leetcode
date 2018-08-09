class Solution1:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        min_num = min(nums)
        max_num = max(nums)
        num_map = {num: 0 for num in range(min_num, max_num+1)}
        res = [None, None]
        for num in nums:
            if num_map[num] == 1:
                res[0] = num
            else:
                num_map[num] = 1
        for num, value in num_map.items():
            if value == 0:
                res[1] = num
                break
        else:
            res[1] = 1 if min_num != 1 else max_num + 1
        return res


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # set一下，可以得到n为set的长度加一，这样就知道总和
        # 减去set的和，就知道少了什么元素，拿未set的数据和减set的和，就知道多了什么
        num_set = set(nums)
        set_sum = sum(num_set)
        n = len(num_set) + 1
        return [sum(nums) - set_sum, n * (n+1) / 2 - set_sum]


if __name__ == '__main__':
    nums = [1, 2, 2, 4]
    res = Solution().findErrorNums(nums)
    print(res)
    assert res == [2, 3]
