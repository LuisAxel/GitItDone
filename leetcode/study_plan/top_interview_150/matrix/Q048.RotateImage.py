class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                tl, tr = matrix[l][l+i], matrix[l+i][r]
                bl, br = matrix[r-i][l], matrix[r][r-i]
                matrix[l][l+i], matrix[l+i][r], matrix[r][r-i], matrix[r-i][l] = bl, tl, tr, br

            l += 1
            r -= 1
