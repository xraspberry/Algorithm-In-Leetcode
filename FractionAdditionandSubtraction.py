'''
https://leetcode.com/problems/fraction-addition-and-subtraction/description/

这道题可真是折腾啊，先是解析字符串，递归解决，求累积，累积完了，还得算最大公约数，总算accepted了
就觉的很坑爹

Runtime: 62 ms
Your runtime beats 18.27 % of python submissions.

'''

import re


class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        ans = ['0/0']

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def simplify(n, d):
            # 求最大公约数
            r = n % d
            if r == 0:
                return d
            else:
                return simplify(d, r)

        def accumulate(v):
            n0, d0 = list(map(int, ans[0].split('/')))
            n, d = list(map(int, v.split('/')))

            if d0 == 0:
                # 共同的分母，是被加数的，其他分子不变
                dc = d
            else:
                # 共同的分母
                dc = d0 * d
                # ans中的分子
                n0 = n0 * d
                # 被加数的分子
                n = n * d0

            # 都是带符号的，随便加
            rn = n0 + n

            cd = simplify(abs(rn), dc)
            ans[0] = '{}/{}'.format(rn // cd, dc // cd)

        def handle(e):
            if not e:
                return
            if e.startswith(('-', '+')):
                m = re.match(r'([-+]\d+/\d+)', e)
                value = m.group(1)
                e = e[m.span()[1]:]
            else:
                m = re.match(r'(\d+/\d+)', e)
                value = m.group(1)
                e = e[m.span()[1]:]
            accumulate(value)
            # 然后递归的处理后面的值
            handle(e)

        handle(expression)
        return ans[0]
