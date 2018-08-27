class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        from collections import defaultdict
        res = []
        for a in A:
            a_len = len(a)
            odd = defaultdict(int)
            even = defaultdict(int)
            for i in range(0, a_len, 2):
                odd[a[i]] += 1
            for i in range(1, a_len, 2):
                even[a[i]] += 1
            counter = {
                'odd': odd,
                'even': even
            }
            if counter not in res:
                res.append({
                    'odd': odd,
                    'even': even
                })
        return len(res)


if __name__ == '__main__':
    A = ["aa", "bb", "ab", "ba"]
    res = Solution().numSpecialEquivGroups(A)
    print(res)
    assert res == 4

    A = ["abc", "acb", "bac", "bca", "cab", "cba"]
    res = Solution().numSpecialEquivGroups(A)
    print(res)
    assert res == 3

    A = ["abcd", "cdab", "adcb", "cbad"]
    res = Solution().numSpecialEquivGroups(A)
    print(res)
    assert res == 1

    A = ["a", "b", "c", "a", "c", "c"]
    res = Solution().numSpecialEquivGroups(A)
    print(res)
    assert res == 3
