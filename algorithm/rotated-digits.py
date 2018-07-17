class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        rotate_map = {
            '0': '0',
            '1': '1',
            '8': '8',
            '5': '2',
            '2': '5',
            '6': '9',
            '9': '6'
        }
        count = 0
        for n in range(N+1):
            n_list = []
            for d in str(n):
                if d not in rotate_map:
                    break
                n_list.append(rotate_map[d])
            else:
                if n != int(''.join(n_list)):
                    count += 1
        return count


if __name__ == '__main__':
    N = 10
    res = Solution().rotatedDigits(N)
    print(res)
    assert res == 0
