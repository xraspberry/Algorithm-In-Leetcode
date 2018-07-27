# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution1(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return
        if head.val == val:
            return self.removeElements(head.next, val)
        elif head.next and head.next.val == val:
            head.next = self.removeElements(head.next.next, val)
        else:
            head.next = self.removeElements(head.next, val)
        return head


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        if not head:
            return
        node = head
        while node:
            if node.next and node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head
