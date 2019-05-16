class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        d = {'A', 'E', 'I', 'O', 'U'}
        for idx, word in enumerate(S.split(' '), 1):
            if word[0].upper() in d:
                word += 'ma'
            else:
                first_alphabet = word[0]
                word = word[1:] + first_alphabet + 'ma'

            word += 'a' * idx
            res.append(word)
        return ' '.join(res)


if __name__ == '__main__':
    S = "I speak Goat Latin"
    correct = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    res = Solution().toGoatLatin(S)
    print(res)
    assert res == correct
