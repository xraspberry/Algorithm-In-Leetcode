from collections import Counter


class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count_a = Counter(A.split(' '))
        count_b = Counter(B.split(' '))
        a_eles = [ele for ele, count in count_a.items() if count == 1]
        b_eles = [ele for ele, count in count_b.items() if count == 1]
        res = []
        for a_ele in a_eles:
            if a_ele not in count_b:
                res.append(a_ele)
        for b_ele in b_eles:
            if b_ele not in count_a:
                res.append(b_ele)
        return res


if __name__ == '__main__':
    A = "this apple is sweet"
    B = "this apple is sour"
    res = Solution().uncommonFromSentences(A, B)
    print(res)
    assert res == ["sweet", "sour"]

    A = "apple apple"
    B = "banana"
    res = Solution().uncommonFromSentences(A, B)
    print(res)
    assert res == ["banana"]

    A = "s z z z s"
    B = "s z ejt"
    res = Solution().uncommonFromSentences(A, B)
    print(res)
    assert res == ["ejt"]
