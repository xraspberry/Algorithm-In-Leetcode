# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 双指针
        i = j = head
        while i and j:
            if j.next and j.next.next:
                j = j.next.next
                i = i.next
            elif j.next:
                return i.next
            else:
                return i
