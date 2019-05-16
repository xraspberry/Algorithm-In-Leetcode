class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        """
        0
        10 11
        """
        start = 0
        if len(bits) == 1:
            return True
        while start < len(bits):
            if bits[start] == 1:
                start += 2
            else:
                start += 1
            if start == len(bits) - 1:
                return True
        return False


if __name__ == '__main__':
    bits = [1, 0, 0]
    res = Solution().isOneBitCharacter(bits)
    print(res)
