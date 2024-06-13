class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r1, r2, c1, c2 = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        r, c = 0,0
        ans = []

        while r1 <= r2 and c1 <= c2:

            # right
            c = c1
            while c <= c2:
                ans.append(matrix[r1][c])
                c += 1

            # down
            r = r1 + 1
            while r <= r2:
                ans.append(matrix[r][c2])
                r += 1

            # left
            c = c2 - 1
            while c >= c1:
                if r1 == r2:
                    break
                ans.append(matrix[r2][c])
                c -= 1

            # up
            r = r2 - 1
            while r > r1:
                if c1 == c2:
                    break
                ans.append(matrix[r][c1])
                r -= 1

            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return ans
