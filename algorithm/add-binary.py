class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_stack = [int(ele) for ele in a]
        b_stack = [int(ele) for ele in b]
        res = []
        carry = 0
        while a_stack or b_stack or carry != 0:
            a_ele = a_stack.pop(-1) if a_stack else 0
            b_ele = b_stack.pop(-1) if b_stack else 0
            ele_sum = a_ele + b_ele + carry
            carry, res_ele = divmod(ele_sum, 2)
            res.append(str(res_ele))
        return ''.join(res[::-1])


if __name__ == '__main__':
    a = "11"
    b = "1"
    res = Solution().addBinary(a, b)
    print(res)
    assert res == "100"
