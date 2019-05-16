class Solution:

    def dfs(self, x, y, color, seen):
        # top
        if x - 1 >= 0 and not seen[x-1][y] and self.image[x-1][y] == self.image[x][y]:
            seen[x-1][y] = True
            self.dfs(x-1, y, color, seen)
            self.image[x - 1][y] = color
        if y + 1 < len(self.image[0]) and not seen[x][y+1] and self.image[x][y+1] == self.image[x][y]:
            seen[x][y+1] = True
            self.dfs(x, y+1, color, seen)
            self.image[x][y+1] = color
        if x + 1 < len(self.image) and not seen[x+1][y] and self.image[x+1][y] == self.image[x][y]:
            seen[x + 1][y] = True
            self.dfs(x+1, y, color, seen)
            self.image[x+1][y] = color
        if y - 1 >= 0 and not seen[x][y-1] and self.image[x][y-1] == self.image[x][y]:
            seen[x][y-1] = True
            self.dfs(x, y-1, color, seen)
            self.image[x][y-1] = color

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.image = image
        seen = []
        for i in range(len(image)):
            inner = []
            for j in range(len(image[0])):
                inner.append(False)
            seen.append(inner)
        self.dfs(sr, sc, newColor, seen)
        self.image[sr][sc] = newColor
        return self.image

if __name__ == '__main__':
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    res = Solution().floodFill(image, sr, sc, newColor)
    print(res)
    assert res == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
