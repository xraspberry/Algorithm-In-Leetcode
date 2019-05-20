"""
有效括号字符串为空 ("")、"(" + A + ")" 或 A + B，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。

如果有效字符串 S 非空，且不存在将其拆分为 S = A+B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。

给出一个非空有效字符串 S，考虑将其进行原语化分解，使得：S = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。

对 S 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 S 。
"""


class Solution:
    """
    其实就是拿到一个完整的括号，那么显而易见使用栈来实现，找到最外层的括号，保留里面的内容，再拼到一起

    """
    def removeOuterParentheses(self, S: str) -> str:
        stack = [S[0]]
        start = 0
        res = ""
        for i, ele in enumerate(S[1:], 1):
            if not stack:
                res += S[start+1:i-1]
                start = i
                stack.append(ele)
            elif stack[-1] == '(' and ele == ')':
                stack.pop(-1)
            else:
                stack.append(ele)
        res += S[start+1:len(S)-1]
        return res


if __name__ == '__main__':
    examples = [
        ("(()())(())", "()()()"),
        ("(()())(())(()(()))", "()()()()(())"),
        ("()()", "")
    ]
    for example in examples:
        ret = Solution().removeOuterParentheses(example[0])
        assert ret == example[1]
