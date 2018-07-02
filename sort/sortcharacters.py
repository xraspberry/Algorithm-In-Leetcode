class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequency = {}
        for ele in s:
            if ele in frequency:
                frequency[ele] += 1
            else:
                frequency[ele] = 1

        bucket = {}
        for key, value in frequency.items():
            bucket.setdefault(value, []).append(key)

        ret = []
        for key in sorted(bucket.keys(), reverse=True):
            for item in bucket[key]:
                ret.append(item*key)
        return ''.join(ret)


if __name__ == '__main__':
    s = 'Aabb'
    res = Solution().frequencySort(s)
    print(res)
