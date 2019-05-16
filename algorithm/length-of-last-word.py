class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.strip().split(' ')
        return len(words[-1]) if words else 0


if __name__ == '__main__':
    s = "Hello World"
    res = Solution().lengthOfLastWord(s)
    print(res)
    assert res == 5
