class Solution1:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        i = 0
        max_dis = 0
        while i < len(seats):
            if seats[i] == 1:
                i += 1
                continue
            left = i
            while left >= 0 and seats[left] != 1:
                left -= 1
            right = i
            while right < len(seats) and seats[right] != 1:
                right += 1
            if left == -1:
                max_dis = max(max_dis, right - i)
            elif right == len(seats):
                max_dis = max(max_dis, i - left)
            else:
                max_dis = max(max_dis, min(i - left, right - i))
            i += 1
        return max_dis


class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        seated = [idx for idx in range(len(seats)) if seats[idx] == 1]
        max_dis = 0
        for idx in range(len(seated) - 1):
            dis = (seated[idx + 1] - seated[idx]) // 2
            max_dis = max(dis, max_dis)
        if seats[0] != 1:
            max_dis = max(max_dis, seated[0])
        if seats[-1] != 1:
            max_dis = max(max_dis, len(seats) - seated[-1] - 1)
        return max_dis


if __name__ == '__main__':
    seats = [1, 0, 0, 0, 1, 0, 1]
    res = Solution().maxDistToClosest(seats)
    print(seats)
    assert res == 2

    seats = [1, 0, 0, 0]
    res = Solution().maxDistToClosest(seats)
    print(seats)
    assert res == 3

    seats = [0, 0, 1, 0, 1, 1]
    res = Solution().maxDistToClosest(seats)
    print(seats)
    assert res == 2
