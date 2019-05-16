class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 双指针判断，当出现不等的情况时，进行两种情况的判断，看是否通过删除一个元素可以形成回文
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.is_palindrome(s[i:j]) or self.is_palindrome(s[i+1:j+1])
            i += 1
            j -= 1
        return True

    def is_palindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    s = "abc"
    res = Solution().validPalindrome(s)
    print(res)