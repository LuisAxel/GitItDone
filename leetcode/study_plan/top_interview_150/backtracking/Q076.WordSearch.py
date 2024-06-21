class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def prune(board, word):
            # Word bigger than board
            if len(board) * len(board[0]) < len(word):
                return False

            # Board missing word letters
            word_dict = defaultdict(int)
            for letter in word:
                word_dict[letter] += 1

            for r in board:
                for letter in r:
                    word_dict[letter] -= 1

            for letter in word:
                if word_dict[letter] > 0:
                    return False
            return True

        def helper(r, c, i):
            nonlocal visited, board, m, n, word, ans

            if board[r][c] != word[i]:
                return

            i += 1
            if i == len(word):
                ans = True
                return

            visited[r][c] = True

            if r > 0 and not visited[r - 1][c]:
                helper(r - 1, c, i)
            if r < m - 1 and not visited[r + 1][c]:
                helper(r + 1, c, i)
            if c > 0 and not visited[r][c - 1]:
                helper(r, c - 1, i)
            if c < n - 1 and not visited[r][c + 1]:
                helper(r, c + 1, i)

            visited[r][c] = False

        if not prune(board, word):
            return False

        m = len(board)
        n = len(board[0])
        ans = False

        for r in range(m):
            for c in range(n):
                if ans:
                    break
                visited = [[False for _ in range(n)] for __ in range(m)]
                helper(r, c, 0)
        return ans
