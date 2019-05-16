class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [None] * 1000000

    def put(self, key, value):
        """
        value will always be positive.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.map[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        value = self.map[key]
        if value is None:
            return -1
        else:
            return value

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        self.map[key] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


if __name__ == '__main__':
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    hashMap.get(1)
    hashMap.get(3)
    hashMap.put(2, 1)
    hashMap.get(2)
    hashMap.remove(2)
    hashMap.get(2)
