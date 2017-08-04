'''

将链表转换成数字，然后加起来，再转换成数字，效率如此之低
Runtime: 195 ms
Your runtime beats 7.92 % of python submissions.

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def get_num(l1):
            node = l1
            res = ''
            while node:
                res += str(node.val)
                node = node.next
            return int(res)

        res = str(get_num(l1) + get_num(l2))
        return list(map(int, res))

