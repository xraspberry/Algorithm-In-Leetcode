'''

赶英超美不是梦。。。卧槽

主要思路就是 找到了下标的规律，但是久经挫折啊

下标的规律就是 比如第0个是(0,0) 第1个对角线的下标是 (0,1)(1,0) 第2个是(2,0)(1,1)(0,2)

看出来了吧，但是有几点需要注意：

1. 偶数的时候和奇数下标排列是反的
2. 列数=总行数-目前的行数，但是因为列数可能没那么多，所以行数迭代的时候给个开始值，这样就可以少迭代了
3. 并且行数迭代也不会超过总行数

搞清楚这三点，这道题就可以accepted了，当然很烦，但是我看到其他人的回答也很烦

总而言之，这道题很烦，给个差评，费了我1小时。。

Runtime: 235 ms
Your runtime beats 40.00 % of python submissions.

'''


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        row = len(matrix)
        col = len(matrix[0])

        ans = [matrix[0][0]]

        def get_next(index):
            reverse = False
            if index % 2 == 0:
                reverse = True
            res = []
            # 最大不能超过行数
            irow = min(row, index + 1)
            # 如果irow小于col的话，就从0开始计算可用行
            start = max(irow - col, 0)
            # 行数开始
            for i in range(start, irow):
                j = index - i
                if j < col:
                    res.append(matrix[i][j])
            if res:
                if reverse:
                    res = res[::-1]
                ans.extend(res)
            return res

        n = 1
        next_ = get_next(n)
        while next_:
            n += 1
            next_ = get_next(n)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findDiagonalOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
