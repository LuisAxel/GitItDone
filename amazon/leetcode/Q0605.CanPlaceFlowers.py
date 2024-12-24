class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        possible = 0

        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 1
                continue
            if i != 0 and flowerbed[i - 1] == 1:
                i += 1
                continue
            if i != len(flowerbed) - 1 and flowerbed[i + 1] == 1:
                i += 1
                continue

            possible += 1
            i += 2

            if possible >= n:
                return True

        return possible >= n
