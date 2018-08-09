class Solution1:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = []
        while n != 0:
            n, bit = divmod(n, 2)
            bits.append(bit)
        bits = [0] * (32 - len(bits)) + bits[::-1]
        target_bits = ''.join(str(bit) for bit in bits[::-1])
        return int(target_bits, 2)


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = bin(n)[2:]
        bits = '0' * (32 - len(bits)) + bits
        return int(bits[::-1], 2)

if __name__ == '__main__':
    n = 43261596
    res = Solution().reverseBits(n)
    print(res)
    assert res == 964176192
    # 00000010100101000001111010011100
    # 00111001011110000010100101000000
