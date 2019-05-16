class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 通过对已知奇偶的元素的交换即可
        odd_idx = 1
        for even_idx in range(0, len(A), 2):
            if A[even_idx] % 2 == 0:
                continue
            else:
                while A[odd_idx] % 2 != 0:
                    odd_idx += 2
                A[odd_idx], A[even_idx] = A[even_idx], A[odd_idx]
                odd_idx += 2
        return A
