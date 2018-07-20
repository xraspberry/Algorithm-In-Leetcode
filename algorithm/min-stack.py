import heapq

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_heap = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        heapq.heappush(self.min_heap, x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            value = self.stack.pop(len(self.stack)-1)
            if value is not None:
                self.min_heap.remove(value)

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[len(self.stack)-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_heap:
            return heapq.nsmallest(1, self.min_heap)[0]

import sys

class MinStack1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = sys.maxsize
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.min:
            # 在小于x的最小的值
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        peak = self.stack.pop()
        if peak == self.min:
            self.min = self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


if __name__ == '__main__':
    minStack = MinStack1()
    minStack.push(2)
    minStack.push(0)
    minStack.push(3)
    minStack.push(0)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())
    minStack.pop()
    print(minStack.getMin())
