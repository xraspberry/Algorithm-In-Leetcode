"""
在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。

给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

返回可以通过分割得到的平衡字符串的最大数量。

 

示例 1：

输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
示例 2：

输入：s = "RLLLLRRRLR"
输出：3
解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。
示例 3：

输入：s = "LLLLRRRR"
输出：1
解释：s 只能保持原样 "LLLLRRRR".
 

提示：

1 <= s.length <= 1000
s[i] = 'L' 或 'R'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-a-string-in-balanced-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_c = r_c = 0
        res = 0
        for item in s:
            if item == 'L':
                l_c += 1
            else:
                r_c += 1
            if l_c == r_c and l_c != 0:
                l_c = r_c = 0
                res += 1
        return res


if __name__ == '__main__':
    res = Solution().balancedStringSplit("RLRRLLRLRL")
    assert res == 4
    res = Solution().balancedStringSplit("RLLLLRRRLR")
    assert res == 3
    res = Solution().balancedStringSplit("LLLLRRRR")
    assert res == 1

