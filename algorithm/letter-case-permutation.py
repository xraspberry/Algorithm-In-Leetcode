class Solution(object):

    def back_tracking(self, s, index, res):
        if index >= len(s):
            res.append(''.join(s))
            return
        if s[index].isalpha():
            s[index] = s[index].lower()
            self.back_tracking(s, index+1, res)
            s[index] = s[index].upper()
            self.back_tracking(s, index+1, res)
        else:
            self.back_tracking(s, index + 1, res)

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # 回溯
        """
            root
          a      A
          1      1
        b   B   b   B
        2   2   2   2
        """
        res = []
        self.back_tracking(list(S), 0, res)
        return res


if __name__ == '__main__':
    S = "a1b2"
    res = Solution().letterCasePermutation(S)
    print(res)
    assert res == ["a1b2", "a1B2", "A1b2", "A1B2"]
