class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows, cols = len(matrix), len(matrix[0])
        zero_r, zero_c = False, False

        # Mark the columns and rows with 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        zero_r = True
                    if c == 0:
                        zero_c = True
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Change 0 submatrix (to not lose marks along the way)
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Update first row and column if needed
        if zero_r:
            for c in range(cols):
                matrix[0][c] = 0

        if zero_c:
            for r in range(rows):
                matrix[r][0] = 0
