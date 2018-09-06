class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        count = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i - 1 < 0 and i + 1 >= len(flowerbed):
                    count += 1
                    break
                elif i - 1 < 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    count += 1
                elif i - 1 < 0 and flowerbed[i + 1] != 0:
                    i += 1
                    continue
                elif i + 1 >= len(flowerbed) and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    count += 1
                elif i + 1 >= len(flowerbed) and flowerbed[i - 1] != 0:
                    i += 1
                    continue
                elif flowerbed[i - 1] == flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    count += 1
            i += 1
        return count >= n


if __name__ == '__main__':
    flowerbed = [1, 0, 0, 0, 0, 1]
    n = 2
    res = Solution().canPlaceFlowers(flowerbed, n)
    print(res)
    assert not res

    flowerbed = [1, 0]
    n = 1
    res = Solution().canPlaceFlowers(flowerbed, n)
    print(res)
    assert not res

    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    res = Solution().canPlaceFlowers(flowerbed, n)
    print(res)
    assert res

    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    res = Solution().canPlaceFlowers(flowerbed, n)
    print(res)
    assert not res
