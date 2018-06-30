class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for element in A:
            processed_element = [ele ^ 1 for ele in element[::-1]]
            res.append(processed_element)
        return res


if __name__ == '__main__':
    array = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    assert Solution().flipAndInvertImage(array) == [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
