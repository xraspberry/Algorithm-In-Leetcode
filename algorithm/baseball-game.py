class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res = []
        for op in ops:
            if op == '+':
                res.append(sum(res[-2:]))
            elif op == 'D':
                res.append(res[-1] * 2)
            elif op == 'C':
                res.pop(-1)
            else:
                res.append(int(op))
        return sum(res)


if __name__ == '__main__':
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(Solution().calPoints(ops))
