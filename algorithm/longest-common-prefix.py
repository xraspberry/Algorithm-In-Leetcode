class Solution1(object):
    def same_prefix(self, a, b):
        length = min(len(a), len(b))
        for i in range(length):
            if a[i] == b[i]:
                i += 1
            else:
                return a[:i]
        return a[:length]

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = strs[0]
        for i in range(1, len(strs)):
            res = self.same_prefix(res, strs[i])
            if not res:
                return res
        return res


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        min_str = min(strs)
        max_str = max(strs)
        length = min(len(min_str), len(max_str))
        for i in range(length):
            if min_str[i] == max_str[i]:
                i += 1
            else:
                return min_str[:i]
        return min_str


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    res = Solution().longestCommonPrefix(strs)
    print(res)
    assert res == 'fl'

    strs = ["dog", "racecar", "car"]
    res = Solution().longestCommonPrefix(strs)
    print(res)
    assert res == ''
