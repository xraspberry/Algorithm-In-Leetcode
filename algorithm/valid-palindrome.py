class Solution1(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j > 0 and not s[j].isalnum():
                j -= 1
            if i > j:
                return True
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        for ele in s:
            if ele.isalnum():
                res.append(ele.lower())
        return res == res[::-1]

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    res = Solution().isPalindrome(s)
    print(res)
    assert res

    s = ".,"
    res = Solution().isPalindrome(s)
    print(res)
    assert res

