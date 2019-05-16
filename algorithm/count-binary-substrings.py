class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 当前重复的数字种类的个数
        cur = 1
        # 上一种数字重复的次数
        pre = 0
        res = 0
        idx = 1
        while idx < len(s):
            if s[idx-1] == s[idx]:
                cur += 1
            else:
                pre = cur
                cur = 1
            if pre >= cur:
                res += 1
            idx += 1
        return res



if __name__ == '__main__':
    s = "10101"
    res = Solution().countBinarySubstrings(s)
    print(res)
