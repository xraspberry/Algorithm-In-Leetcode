class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        # 2^19 == 524288
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        res = 0
        for number in range(L, R+1):
            count = bin(number).count('1')
            if count in primes:
                res += 1
        return res


if __name__ == '__main__':
    L = 10
    R = 15
    res = Solution().countPrimeSetBits(L, R)
    print(res)