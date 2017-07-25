'''
https://leetcode.com/problems/replace-words/#/description

用了最low的遍历，当然是可以完成工作的，但是效率嘛。。。

Runtime: 349 ms
'''


class Solution:
    def replaceWords(self, word_dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        res = []
        for word in sentence.split():
            for wd in word_dict:
                if word.startswith(wd):
                    res.append(wd)
                    break
            else:
                res.append(word)
        return ' '.join(res)

