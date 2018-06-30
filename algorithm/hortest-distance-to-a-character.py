class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c_pos_in_S = []
        for idx, s in enumerate(S):
            if s == C:
                c_pos_in_S.append(idx)
        if not c_pos_in_S:
            return []
        c_lft_pos = c_pos_in_S.pop(0)
        c_rgt_pos = c_pos_in_S.pop(0) if c_pos_in_S else c_lft_pos
        pos = 0
        res = []
        while pos < len(S):
            if pos <= c_lft_pos:
                res.append(c_lft_pos - pos)
            elif c_lft_pos < pos < c_rgt_pos:
                res.append(min([c_rgt_pos - pos, pos - c_lft_pos]))
            elif pos == c_rgt_pos:
                # 在等于右边界的时候调整边界位置
                res.append(c_rgt_pos - pos)
                c_lft_pos = c_rgt_pos
                c_rgt_pos = c_pos_in_S.pop(0) if c_pos_in_S else c_lft_pos
            else:
                res.append(pos - c_rgt_pos)
            pos += 1
        return res


if __name__ == '__main__':
    S = "aaba"
    C = 'b'
    result = Solution().shortestToChar(S, C)
    print(result)
    assert result == [2, 1, 0, -1]
