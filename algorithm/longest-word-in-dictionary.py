class Node:
    ENDOF = '#'

    def __init__(self, depth, parent, val=None):
        self.depth = depth
        self.val = val
        self.parent = parent
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node(depth=0, parent=None, val="root")
        self.size = 0
        self.count = None

    def add(self, key):
        self.size += 1
        node = self.root
        # 将单词key中的每一个字添加到树中
        for ele in key:
            if ele not in node.children:
                node.children[ele] = Node(node.depth + 1, node, ele)
            node = node.children[ele]
        else:
            node.children[Node.ENDOF] = Node(node.depth + 1, node, Node.ENDOF)
        return self.root

    def has_prefix(self, word):
        node = self.root

        for ele in word:
            node = node.children[ele]
            if Node.ENDOF not in node.children:
                return False
        else:
            return True


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = Trie()
        for word in words:
            trie.add(word)

        def _sort_func(x, y):
            if len(y) - len(x) == 0:
                if x < y:
                    return -1
                elif x > y:
                    return 1
                else:
                    return 0
            else:
                return len(y) - len(x)

        from functools import cmp_to_key
        words = sorted(words, key=cmp_to_key(_sort_func))
        for word in words:
            if trie.has_prefix(word):
                return word


if __name__ == '__main__':
    words = ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]
    res = Solution().longestWord(words)
    print(res)
    assert res == "yodn"
