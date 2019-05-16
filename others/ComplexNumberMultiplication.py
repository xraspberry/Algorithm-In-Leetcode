'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

这道题我一开始的思路就是：首先求笛卡尔积，然后在根据不同的情况进行判断，有以下这几种可能：

1. 两个数都是实数
2. 一个数是实数，另一个是虚数
3. 两个都是虚数

根据这些情况，计算出笛卡尔积每一项，然后合并的时候有两种情况：

1. 实数合并
2. 虚数合并

Runtime: 39 ms
Your runtime beats 54.80 % of python submissions.
'''


class SolutionA(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def handle(ele1, ele2):
            if 'i' not in ele1:
                if 'i' not in ele2:
                    return str(int(ele1) * int(ele2))
                else:
                    return str(int(ele1) * int(ele2[:-1])) + 'i'
            else:
                if 'i' in ele2:
                    return str(int(ele2[:-1]) * int(ele1[:-1]) * -1)
                else:
                    return str(int(ele2) * int(ele1[:-1])) + 'i'
        a_list = a.split('+')
        b_list = b.split('+')
        from itertools import product
        res = product(a_list, b_list)
        ret = {'digit': 0, 'i': 0}
        for ele in res:
            h_res = handle(ele[0], ele[1])
            if 'i' not in h_res:
                ret['digit'] += int(h_res)
            else:
                ret['i'] += int(h_res[:-1])
        return str(ret['digit']) + '+' + str(ret['i']) + 'i'

'''
那么现在就可以将其进行化简了，试着从最后结果入手：

1. 最后结果的实数的来源可能是，之前两者实数的相乘和两个虚数相乘的和
2. 虚数的来源是，实数和虚数相乘的和

那么问题就简化了

Runtime: 42 ms
Your runtime beats 39.92 % of python submissions.
'''


class SolutionB(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 抽出来实数和虚数
        al = a.split('+')
        bl = b.split('+')
        ar = int(al[0])
        ai = int(al[1][:-1])
        br = int(bl[0])
        bi = int(bl[1][:-1])

        # 最后结果的实数，是实数相乘和虚数相乘的和
        rr = ar * br - ai * bi
        # 最后结果的虚数，是虚数和实数相乘的结果
        ri = ar * bi + ai * br

        res = "{}+{}i".format(rr, ri)
        return res
