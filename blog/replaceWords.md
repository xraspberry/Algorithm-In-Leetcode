[Replace Words](https://leetcode.com/problems/replace-words/#/description)

遍历替换
---

在Leetcode上遇到了这个问题，第一反应是遍历，只要找到以单词字典中的值开头的单词，就用单词字典中相应的值将其替换掉，然后再将最后的值组合成一个句子即可

```
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
```

正则表达式
-----

文本匹配替换什么的，用正则表达式都是可以完成的，只是效率不高，其中`\b`表示从单词匹配，如果后面加上`\b`，这样就可以完整的匹配一个单词了，因为`\w+`排除了空白字符，因此也可以匹配一个单词

```
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
```

单词查找树
-----

之前自己写了一个单词查找树，没想到在这里派上用场了，之前那个项目托管在Github上：[trie](https://github.com/Microndgt/trie)

其主要存储机制是这样的：首先从root节点开始，每个节点有一个children属性，是一个字典，键为该节点代表的字在单词的后面一个字，然后这个字也是一个节点，以此类推。节点除了记录子节点和值，还记录了深度和父节点，方便遍历。发现了一个规律，在实际生产中，貌似大部分都会使用双向链接，比如双向循环链表，会索引父节点的树

```
class Node(object):
    def __init__(self, depth, parent, val=None):
        self.val = val
        self.depth = depth
        self.parent = parent
        self.children = {}
```

创建一个单词查找树，需要创建root节点，然后向其添加值(节点)，添加的方法是如果该节点children没有该字，则将其存入children，然后将node切换成刚才创建的新的节点，直到将单词完全放完，为了和一些短的单词进行区分，会在单词插入末尾插入一个结束标记，比如`#`

```
def add(self, key):
    self.size += 1
    node = self.root
    for ele in key:
        if ele not in node.children:
            node.children[ele] = Node(node.depth+1, node, ele)
        node = node.children[ele]
    else:
        node.children[END_OF] = Node(node.depth+1, node, END_OF)
    return self.root
```

创建好树之后，如果只是解决这个问题，那么将所有单词字典的单词加入到树里面，然后再加入一个获取单词前缀的方法就行了，将要判断的单词每个字在树里面遍历，如果树里面的单词提前结束了，说明树里面的单词就是这个要判断单词的前缀，因此返回树里面的单词，如果不是的话，就找不到，所以返回原来的单词

```
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
```

接下来就可以使用这个树解决问题了：

```
class SolutionC:
    def replaceWords(self, word_dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        # 初始化树
        trie = Trie()
        # 添加单词字典里面的单词
        for wd in word_dict:
            trie.add(wd)
        sl = sentence.split()
        res = []
        # 判断sentence中的单词是不是有前缀
        for s in sl:
            res.append(trie.get_prefix(s))
        return ' '.join(res)
```