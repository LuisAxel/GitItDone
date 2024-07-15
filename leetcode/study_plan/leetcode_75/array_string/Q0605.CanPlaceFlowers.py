class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, i = 0, 0
        n1 = len(flowerbed)

        while i < n1:
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i-1] == 0) and (i == n1-1 or flowerbed[i+1] == 0):
                    i += 1
                    n -= 1
                    if n <= 0:
                        break
            i += 1
        return n <= 0
