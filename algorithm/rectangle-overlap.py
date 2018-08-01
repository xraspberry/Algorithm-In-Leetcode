class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # 重叠的可能有多种多样，不重叠的可能只有4种
        # 以第二个矩形为中心，进行判断
        if rec1[2] <= rec2[0] or rec1[1] >= rec2[3] or rec1[0] >= rec2[2] or rec1[3] <= rec2[1]:
            return False
        return True


if __name__ == '__main__':
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    res = Solution().isRectangleOverlap(rec1, rec2)
    print(res)
    assert res

    rec1 = [0, 0, 1, 1]
    rec2 = [1, 0, 2, 1]
    res = Solution().isRectangleOverlap(rec1, rec2)
    print(res)
    assert not res

    rec1 = [7, 8, 13, 15]
    rec2 = [10, 8, 12, 20]
    res = Solution().isRectangleOverlap(rec1, rec2)
    print(res)
    assert res
