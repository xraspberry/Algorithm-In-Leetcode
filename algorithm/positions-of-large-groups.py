class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        i = 0
        res = []
        while i < len(S):
            j = i + 1
            while j < len(S) and S[j] == S[i]:
                j += 1
            if j - i >= 3:
                res.append([i, j-1])
            i = j
        return res


if __name__ == '__main__':
    s = "abbxxxxzzy"
    res = Solution().largeGroupPositions(s)
    print(res)
    assert res == [[3, 6]]

    s = "abc"
    res = Solution().largeGroupPositions(s)
    print(res)
    assert res == []

    s = "abcdddeeeeaabbbcd"
    res = Solution().largeGroupPositions(s)
    print(res)
    assert res == [[3, 5], [6, 9], [12, 14]]
