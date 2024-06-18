class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def fill(row, col, n, m, char):
            nonlocal board
            nonlocal visited
            if row < 0 or row >= n or col < 0 or col >= m:
                return

            if board[row][col] == 'X' or visited[row][col] == 1:
                return

            board[row][col] = char
            visited[row][col] = 1

            fill(row - 1, col, n , m, char)
            fill(row + 1, col, n , m, char)
            fill(row, col - 1, n , m, char)
            fill(row, col + 1, n , m, char)

        n = len(board)
        m = len(board[0])

        visited = [[0 for _ in range(m)] for _ in range(n)]

        # Mark not surrounded island by visiting edges
        for col in range(m):
            if board[0][col] == 'O':
                fill(0, col, n, m, 'S')
            if board[n - 1][col] == 'O':
                fill(n - 1, col, n, m, 'S')
        for row in range(n):
            if board[row][0] == 'O':
                fill(row, 0, n, m, 'S')
            if board[row][m - 1] == 'O':
                fill(row, m - 1, n, m, 'S')

        # Mark as X all other islands
        for row in range(1, n - 1):
            for col in range(1, m - 1):
                if board[row][col] == 'O':
                    fill(row, col, n, m, 'X')

        # Revert changes to safe islands
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'S':
                    board[row][col] = 'O'
