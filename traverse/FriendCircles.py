'''
https://leetcode.com/problems/friend-circles/description/

深度优先遍历在处理这种链接问题简直太容易，核心就是

将所有节点遍历一遍，条件是如果该节点没有在seen集合中出现过，
然后遍历的时候如果找到1的话，就继续搜索，加入seen，直到结束，就把所有能加入的加入了

Runtime: 82 ms
Your runtime beats 35.54 % of python submissions.

'''


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        # 对于每一个节点开始进行遍历，dfs搜索，只要可以链接上的，就放入已经遍历过的节点集合中，遍历的时候也要判断是否已经在集合中了，简直太简单。

        def dfs(node):
            for index, i in enumerate(M[node]):
                if i and index not in seen:
                    seen.add(index)
                    dfs(index)

        seen = set()

        rows = len(M)
        ans = 0
        for i in range(rows):
            if i not in seen:
                dfs(i)
                ans += 1

        return ans
