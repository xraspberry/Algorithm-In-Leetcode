class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [None] * 1000000

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.table[key] = key

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.table[key] = None

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        return self.table[key] is not None


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))
print(hashSet.contains(3))
hashSet.add(2)
print(hashSet.contains(2))
hashSet.remove(2)
print(hashSet.contains(2))
