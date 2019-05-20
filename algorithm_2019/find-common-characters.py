"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。



示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：

输入：["cool","lock","cook"]
输出：["c","o"]


提示：

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母
"""

from collections import Counter


class Solution:
    def commonChars(self, A):
        char_sets = [Counter(a) for a in A[1:]]
        ret = []
        for ele in A[0]:
            for char_set in char_sets:
                if ele not in char_set or char_set[ele] <= 0:
                    break
            else:
                for char_set in char_sets:
                    char_set.subtract({ele: 1})
                ret.append(ele)
        return ret


if __name__ == '__main__':
    examples = [
        (["bella","label","roller"], ["e","l","l"]),
        (["cool","lock","cook"], ["c","o"])
    ]
    for example in examples:
        res = Solution().commonChars(example[0])
        assert res == example[1]
