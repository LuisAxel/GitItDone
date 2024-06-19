class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def parse_position(pos, n):
            row, col = divmod(pos - 1, n)
            # Zig zag
            if row % 2 == 0:
                return n - row - 1, col

            return n - row - 1, n - 1 - col

        n = len(board)
        q = deque()
        seen = [False] * ((n * n) + 1)
        q.append([1, 0])
        m = 0

        while q:
            pos, moves = q.popleft()
            row, col = parse_position(pos, n)
            pos = pos if board[row][col] == -1 else board[row][col]

            if seen[pos]:
                continue
            if pos == n * n:
                return moves

            seen[pos] = True
            for i in range(1, 7):
                new = pos + i
                if new <= n * n:
                    q.append([new, moves + 1])

        return -1
