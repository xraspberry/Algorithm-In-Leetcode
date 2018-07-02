class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort()
        res = ''
        for word in d:
            i = j = 0
            while j < len(word):
                if i >= len(s):
                    break
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            else:
                if len(word) > len(res):
                    res = word
        return res


if __name__ == '__main__':
    s = "bab"
    d = ["ba", "ab", "a", "b"]
    res = Solution().findLongestWord(s, d)
    print(res)
