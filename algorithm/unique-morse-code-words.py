class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet_morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                          "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_morse_dict = {alphabet: morse for alphabet, morse in zip(alphabets, alphabet_morse)}
        res = set()
        for word in words:
            res.add(''.join(alphabet_morse_dict[w] for w in word))
        return len(res)


if __name__ == '__main__':
    print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
