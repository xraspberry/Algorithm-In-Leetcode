class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        i = 0
        j = len(s) - 1
        slist = list(s)
        while i < j:
            if slist[i].lower() not in vowels:
                i += 1
                continue
            if slist[j].lower() not in vowels:
                j -= 1
                continue
            slist[i], slist[j] = slist[j], slist[i]
            i += 1
            j -= 1
        return "".join(slist)


if __name__ == '__main__':
    s = "leetcode"
    res = Solution().reverseVowels(s)
    print(res)
