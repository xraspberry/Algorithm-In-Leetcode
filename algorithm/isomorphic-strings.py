class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        alphabet_map = {}
        used = set()
        for s_ele, t_ele in zip(s, t):
            if s_ele not in alphabet_map and t_ele not in used:
                alphabet_map[s_ele] = t_ele
                used.add(t_ele)
            if alphabet_map.get(s_ele) != t_ele:
                return False
        return True


if __name__ == '__main__':
    s = "egg"
    t = "add"
    res = Solution().isIsomorphic(s, t)
    print(res)
    assert res

    s = "foo"
    t = "bar"
    res = Solution().isIsomorphic(s, t)
    print(res)
    assert not res

    s = "paper"
    t = "title"
    res = Solution().isIsomorphic(s, t)
    print(res)
    assert res

    s = "ab"
    t = "aa"
    res = Solution().isIsomorphic(s, t)
    print(res)
    assert not res
