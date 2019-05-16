class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 每个数字出现的次数
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        # 出现次数下所有的数字
        bucket = {}
        for key, value in frequency.items():
            if value not in bucket:
                bucket[value] = [key]
            else:
                bucket[value].append(key)

        top_k = []
        for key in sorted(bucket.keys(), reverse=True):
            for ele in bucket[key]:
                if len(top_k) >= k:
                    return top_k
                top_k.append(ele)
        return top_k


if __name__ == '__main__':
    nums = [1]
    k = 1
    res = Solution().topKFrequent(nums, k)
    print(res)
