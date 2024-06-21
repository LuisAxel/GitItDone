class Solution:
    def totalNQueens(self, n: int) -> int:
        def mark(row, col, n, mark):
            nonlocal board
            # Tower
            for i in range(row, n):
                board[i][col] += mark

            # Bishop
            # Primary diagonal
            i, j = row, col
            while i < n and j < n:
                board[i][j] += mark
                i += 1
                j += 1
            # Seconday diagonal
            i, j = row, col
            while i < n and j >= 0:
                board[i][j] += mark
                i += 1
                j -= 1

        def dfs(row, n):
            nonlocal ans, board
            if row == n:
                ans += 1
                return

            for col in range(n):
                if board[row][col] == 0:
                    mark(row, col, n, 1)
                    dfs(row + 1, n)
                    mark(row, col, n, -1)

        board = [[0 for _ in range(n)] for __ in range(n)]
        ans = 0
        dfs(0, n)
        return ans
