class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s_map = {
            ']': '[',
            ')': '(',
            "}": '{'
        }
        # 栈 依次入栈 出栈
        stack = [s[0]]
        i = 1
        while i < len(s):
            if s[i] not in s_map:
                stack.append(s[i])
            else:
                if not stack or s_map[s[i]] != stack.pop(-1):
                    return False
            i += 1
        return True if len(stack) == 0 else False


if __name__ == '__main__':
    # s = "()[]{}"
    # res = Solution().isValid(s)
    # print(res)
    # assert res

    s = "["
    res = Solution().isValid(s)
    print(res)
    assert not res
