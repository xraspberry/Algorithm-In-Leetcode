"""
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

示例：

输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
 

提示：

1 <= S.length <= 20000
S 仅由小写英文字母组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import string


class Solution1:
    def removeDuplicates(self, S: str) -> str:
        point = 0
        len_s = len(S)
        if len_s <= 1:
            return S
        while point < len_s - 1:
            if S[point] == S[point+1]:
                S = S[:point] + S[point+2:]
                len_s = len(S)
                point = 0
            else:
                point += 1
        return S


class Solution2:
    def removeDuplicates(self, S: str) -> str:
        stack = [S[0]]
        S = list(S[1:])
        while S:
            s = S.pop(0)
            if stack and stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        return ''.join(stack)


class Solution:
    def removeDuplicates(self, S: str) -> str:
        dups = [item+item for item in string.ascii_lowercase]
        while True:
            found = False
            for dup in dups:
                old_S = S
                S = S.replace(dup, '')
                if S != old_S:
                    found = True
            if not found:
                break
        return S


if __name__ == '__main__':
    res = Solution().removeDuplicates("abbaca")
    assert res == 'ca'
