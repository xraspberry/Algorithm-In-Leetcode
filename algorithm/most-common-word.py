from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        symbol = "!?',;."
        counter = Counter()
        for word in paragraph.split(' '):
            word = word.strip(symbol).lower()
            if word not in banned:
                counter[word] += 1
        return counter.most_common(1)[0][0]


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    res = Solution().mostCommonWord(paragraph, banned)
    print(res)
    assert res == "ball"
