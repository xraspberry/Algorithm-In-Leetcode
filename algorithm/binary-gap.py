class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        i = 0
        binary = bin(N)[2:]
        res = 0
        while i < len(binary):
            step = 1
            j = i + 1
            while j < len(binary) and binary[j] != '1':
                j += 1
                step += 1
            if j == len(binary):
                break
            i = j
            res = max(step, res)
        return res


if __name__ == '__main__':
    N = 6
    res = Solution().binaryGap(N)
    print(res)
    assert res == 2
