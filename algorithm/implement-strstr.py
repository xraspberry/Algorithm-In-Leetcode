class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        i = j = 0
        while i < len(haystack) and len(needle) <= len(haystack) - i:
            if haystack[i] != needle[0]:
                i += 1
            else:
                inner_i = i
                while j < len(needle):
                    if haystack[inner_i] == needle[j]:
                        inner_i += 1
                        j += 1
                    else:
                        j = 0
                        i += 1
                        break
                else:
                    return i
        return -1


if __name__ == '__main__':
    haystack = "mississippi"
    needle = "issip"
    res = Solution().strStr(haystack, needle)
    print(res)
    assert res == 2

    haystack = "aaaaa"
    needle = "bba"
    res = Solution().strStr(haystack, needle)
    print(res)
    assert res == -1
