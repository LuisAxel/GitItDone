class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])

        def neigh(i, j):
            s = 0

            #up
            if i > 0:
                if board[i - 1][j] % 2 == 1:
                    s += 1
                # up left and right
                if j > 0 and board[i - 1][j - 1] % 2 == 1:
                    s += 1
                if j < cols - 1 and board[i - 1][j + 1] % 2 == 1:
                    s += 1
            # down
            if i < rows - 1:
                if board[i + 1][j] % 2 == 1:
                    s += 1
                # down left and right
                if j > 0 and board[i + 1][j - 1] % 2 == 1:
                    s += 1
                if j < cols - 1 and board[i + 1][j + 1] % 2 == 1:
                    s += 1

            #left and right
            if j > 0 and board[i][j - 1] % 2 == 1:
                s += 1
            if j < cols - 1 and board[i][j + 1] % 2 == 1:
                s += 1
            return s

        # Update board
        # 3 live -> death
        # 4 death -> live
        for r in range(rows):
            for c in range(cols):
                s = neigh(r,c)
                if board[r][c] == 1 and (s < 2 or s > 3):
                    board[r][c] = 3
                if board[r][c] == 0 and s == 3:
                    board[r][c] = 4

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 3:
                    board[r][c] = 0
                elif board[r][c] == 4:
                    board[r][c] = 1
