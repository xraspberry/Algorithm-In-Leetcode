class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        pos = {alphabet: idx for idx, alphabet in enumerate("abcdefghijklmnopqrstuvwxyz")}
        idx = row = col = 0
        while idx < len(S):
            expected = col + widths[pos[S[idx]]]
            if expected > 100:
                row += 1
                col = 0
            else:
                col += widths[pos[S[idx]]]
                idx += 1
        return [row+1, col]


if __name__ == '__main__':
    widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    S = "bbbcccdddaaa"
    print(Solution().numberOfLines(widths, S))
