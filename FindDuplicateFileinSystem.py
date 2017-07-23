'''

Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output:
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

完全没有难度，只是字符串操作罢了，无聊

Runtime: 246 ms
Your runtime beats 83.02 % of python submissions.

'''


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        # 这道题必须给个down
        from collections import defaultdict
        res = defaultdict(list)
        for ele in paths:
            eles = ele.split()
            root = eles[0]
            for f in eles[1:]:
                path, content = f.split('(')
                res[content[:-1]].append('/'.join([root, path]))

        return [value for value in res.values() if len(value) > 1]