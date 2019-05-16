class Solution1:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 1
        j = 0
        count = 1
        res = []
        while i < len(chars) + 1:
            if i < len(chars) and chars[i] == chars[j]:
                count += 1
                i += 1
                continue
            res.append(chars[j])
            if count > 1:
                res.extend([ele for ele in str(count)])
            count = 1
            j = i
            i += 1
        chars[:len(res)] = res
        return len(res)


class Solution2:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 1
        j = 0
        count = 1
        while i < len(chars) + 1:
            if i < len(chars) and chars[i] == chars[j]:
                count += 1
                i += 1
                continue
            data = [chars[j]]
            if count > 1:
                data.extend([ele for ele in str(count)])
            diff = len(chars[j:i]) - len(data)
            chars[j:i] = data
            i = i - diff
            count = 1
            j = i
            i += 1
        return len(chars)


class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        res, i = 0, 0
        while i < len(chars):
            current_char = chars[i]
            count = 0
            while i < len(chars) and chars[i] == current_char:
                i += 1
                count += 1

            chars[res] = current_char
            res += 1
            if count > 1:
                for char in str(count):
                    chars[res] = char
                    res += 1
        return res


if __name__ == '__main__':
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    res = Solution().compress(chars)
    print(res)
    assert res == 6

    chars = ["a", "b", "b", "b", "c", "c", "c"]
    res = Solution().compress(chars)
    print(res)
    assert res == 5

    chars = ["a"]
    res = Solution().compress(chars)
    print(res)
    assert res == 1

    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    res = Solution().compress(chars)
    print(res)
    assert res == 4
