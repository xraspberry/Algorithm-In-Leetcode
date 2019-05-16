class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_a = len(A)
        from collections import defaultdict
        counter = defaultdict(int)
        for a in A:
            counter[a] += 1
            if counter[a] == len_a / 2:
                return a


class Solution1:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a_set = set()
        for a in A:
            if a in a_set:
                return a
            else:
                a_set.add(a)
