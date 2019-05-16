'''

https://leetcode.com/problems/linked-list-random-node/description/

看到这道题的时候是一脸懵逼的，不是太难，而是太容易，不知所以，在Python中可能很简单吧

最后将链表转换成了列表，这样就可以使用随机索引了

Runtime: 115 ms
Your runtime beats 95.45 % of python submissions.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from random import choice


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        # 将链表转换成列表，然后随机索引不就可以了？
        self._head = head
        node = self._head
        self._data = []
        while node:
            self._data.append(node.val)
            node = node.next
        self._index = list(range(len(self._data)))

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        return self._data[choice(self._index)]

        # Your Solution object will be instantiated and called as such:
        # obj = Solution(head)
        # param_1 = obj.getRandom()