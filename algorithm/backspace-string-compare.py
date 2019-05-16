class Solution:

    def build_string(self, string):
        stack = []
        for s in string:
            if s != '#':
                stack.append(s)
            elif s == '#' and stack:
                stack.pop()
        return ''.join(stack)

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # 两个栈，入栈，并且遇到#出栈，最后比较字符串是否相等
        s = self.build_string(S)
        t = self.build_string(T)
        return s == t

if __name__ == '__main__':
    S = "a#c"
    T = "ad#c"
    res = Solution().backspaceCompare(S, T)
    print(res)

