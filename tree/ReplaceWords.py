'''
https://leetcode.com/problems/replace-words/#/description

用了最low的遍历，当然是可以完成工作的，但是效率嘛。。。

Runtime: 349 ms
'''


class SolutionA:
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

'''

正则表达式还是有点慢。。。
'''


class SolutionB:
    def replaceWords(self, word_dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        import re
        for wd in word_dict:
            reg = r"\b{}\w+".format(wd)
            sentence = re.sub(reg, wd, sentence)

        return sentence


'''
使用单词查找树
Runtime: 289 ms
Your runtime beats 42.29 % of python submissions.

'''

END_OF = '#'


class Node(object):
    def __init__(self, depth, parent, val=None):
        self.val = val
        self.depth = depth
        self.parent = parent
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = Node(depth=0, parent=None, val="root")
        self.size = 0
        self.count = None

    def add(self, key):
        self.size += 1
        node = self.root
        for ele in key:
            if ele not in node.children:
                node.children[ele] = Node(node.depth + 1, node, ele)
            node = node.children[ele]
        else:
            node.children[END_OF] = Node(node.depth + 1, node, END_OF)
        return self.root

    def get_prefix(self, word):
        cur = self.root
        ans = ''
        for w in word:
            if w in cur.children:
                cur = cur.children[w]
                ans += w
                if END_OF in cur.children:
                    return ans
            else:
                break
        return word


class SolutionC:
    def replaceWords(self, word_dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for wd in word_dict:
            trie.add(wd)
        sl = sentence.split()
        res = []
        for s in sl:
            res.append(trie.get_prefix(s))
        return ' '.join(res)