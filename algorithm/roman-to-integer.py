"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        converter = {
            'I': 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s_list = list(s.upper())
        res = idx = 0
        s_list_len = len(s_list)
        while idx < s_list_len:
            ele = s_list[idx]
            if idx < s_list_len - 1:
                next_ele = s_list[idx+1]
                if converter[ele] < converter[next_ele]:
                    res += converter[next_ele] - converter[ele]
                    idx += 2
                    continue
            res += converter[ele]
            idx += 1
        return res


if __name__ == '__main__':
    s = "MCMXCIV"
    res = Solution().romanToInt(s)
    print(res)
    assert res == 9
