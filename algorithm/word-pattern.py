class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strings = str.split(' ')
        if len(strings) != len(pattern):
            return False
        word_map = {}
        used = set()
        for idx, ele in enumerate(pattern):
            if ele not in word_map and strings[idx] not in used:
                word_map[ele] = strings[idx]
                used.add(strings[idx])
            if word_map.get(ele) != strings[idx]:
                return False
        return True


if __name__ == '__main__':
    pattern = "abba"
    str = "dog dog dog dog"
    res = Solution().wordPattern(pattern, str)
    print(res)
    assert not res

    pattern = "abba"
    str = "dog cat cat dog"
    res = Solution().wordPattern(pattern, str)
    print(res)
    assert res

    pattern = "jquery"
    str = "jquery"
    res = Solution().wordPattern(pattern, str)
    print(res)
    assert not res

    pattern = "aaa"
    str = "aa aa aa aa"
    res = Solution().wordPattern(pattern, str)
    print(res)
    assert not res
