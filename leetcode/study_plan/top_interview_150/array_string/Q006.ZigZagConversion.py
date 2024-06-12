class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        ans = [""] * numRows # 1 String for each row
        direction = -1
        row = 0

        for c in s:
            ans[row] += c
            if row == 0 and direction == -1:
                direction = 1
            elif row == numRows - 1 and direction == 1:
                direction = - 1
            row += direction

        return "".join(ans)
