class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r, mid_r = 0, len(matrix) - 1, 0

        while l <= r:
            mid_r = (l + r) // 2
            if matrix[mid_r][0] <= target and matrix[mid_r][-1] >= target:
                break

            if matrix[mid_r][-1] < target:
                l = mid_r + 1
            else:
                r = mid_r - 1

        l, r, mid_c = 0, len(matrix[0]) - 1, 0
        while l <= r:
            mid_c = (l + r) // 2
            if matrix[mid_r][mid_c] == target:
                return True

            if matrix[mid_r][mid_c] < target:
                l = mid_c + 1
            else:
                r = mid_c - 1

        return False
