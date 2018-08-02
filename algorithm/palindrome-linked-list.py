# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        """
        1->2->2->1
        输出: true
        """
        res = []
        node = head
        while node:
            res.append(node.val)
            node = node.next
        return res == res[::-1]


class Solution1(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        """
        1->2->2->1->1
        输出: true
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow 在中间位置(奇数) 或者 中间靠右(偶数)
        # 将slow右边的链表反转
        node = slow
        left = None
        while node:
            right = node.next
            node.next = left
            left = node
            node = right
        while left and head:
            if head.val != left.val:
                return False
            left = left.next
            head = head.next
        return True
