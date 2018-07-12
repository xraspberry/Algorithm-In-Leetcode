class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        import math
        max_area = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    point_i, point_j, point_k = points[i], points[j], points[k]
                    distance_i_j = math.sqrt((point_i[0] - point_j[0]) ** 2 + (point_i[1] - point_j[1]) ** 2)
                    distance_i_k = math.sqrt((point_i[0] - point_k[0]) ** 2 + (point_i[1] - point_k[1]) ** 2)
                    distance_j_k = math.sqrt((point_k[0] - point_j[0]) ** 2 + (point_k[1] - point_j[1]) ** 2)
                    s = (distance_i_j + distance_i_k + distance_j_k) / 2
                    max_area = max(s * (s-distance_i_k) * (s-distance_i_j) * (s-distance_j_k), max_area)
        return math.sqrt(max_area)


if __name__ == '__main__':
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    res = Solution().largestTriangleArea(points)
    print(res)
