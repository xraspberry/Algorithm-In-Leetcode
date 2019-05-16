# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        """
        A:          a1 → a2
                           ↘
                             c1 → c2 → c3
                           ↗            
        B:     b1 → b2 → b3
        c1相交
        """
        # 1. 给节点上加标记
        node_a = headA
        node_b = headB
        while node_a or node_b:
            if node_a:
                if not hasattr(node_a, 'visited'):
                    node_a.visited = True
                else:
                    return node_a
                node_a = node_a.next
            if node_b:
                if not hasattr(node_b, 'visited'):
                    node_b.visited = True
                else:
                    return node_b
                node_b = node_b.next


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 双指针，同时开始遍历
        if not headA or not headB:
            return
        node_a, node_b = headA, headB
        while node_a and node_b and node_a != node_b:
            node_a = node_a.next
            node_b = node_b.next
            # 如果相等退出，包含None的情况
            if node_a == node_b:
                return node_a
            # 如果node_a完了，跳到b链表，
            # 两个链表如果相交的化，第二次遍历的时候肯定会重合
            if not node_a:
                node_a = headB
            if not node_b:
                node_b = headA
        return node_a
