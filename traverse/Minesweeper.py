'''

https://leetcode.com/problems/minesweeper/#/description

遇到这种问题，深度优先遍历，妥妥的，关键是要找到不同情况的不同处理

这里，首先必须得获取到一个节点周围的格子，以及上面的元素，这是肯定的
接下来，如果判断元素，如果是M，则变为X，返回，如果是在M周围的元素，那么将其变成数字，返回，如果不是在周围，那么就将周围的节点加入遍历，并将其变成B

这样就解决了问题

Runtime: 85 ms
Your runtime beats 40.18 % of python submissions.

'''


class Solution(object):
    def updateBoard(self, A, click):
        click = tuple(click)
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            # 一共有8种可能
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if (dr or dc) and 0 <= r + dr < R and 0 <= c + dc < C:
                        yield r + dr, c + dc

        stack = [click]
        seen = {click}
        while stack:
            r, c = stack.pop()
            if A[r][c] == 'M':
                A[r][c] = 'X'
            else:
                mines_adj = sum( A[nr][nc] in 'MX' for nr, nc in neighbors(r, c) )
                if mines_adj:
                    A[r][c] = str(mines_adj)
                else:
                    A[r][c] = 'B'
                    for nei in neighbors(r, c):
                        if A[nei[0]][nei[1]] in 'ME' and nei not in seen:
                            stack.append(nei)
                            seen.add(nei)
        return A