class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        cur['EOS'] = ''

    def search(self, word: str) -> bool:
        cur = self.root

        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]

        return 'EOS' in cur


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(r, c, cur, word):
            nonlocal board, ans, n_r, n_c
            letter = board[r][c]

            if letter not in cur:
                return False

            word += letter
            cur = cur[letter]

            # Found word
            if 'EOS' in cur:
                ans.add(word)

            # Visited
            board[r][c] = '*'

            # UP
            if r > 0 and board[r - 1][c] != '*':
                dfs(r - 1, c, cur, word)
            # DOWN
            if r + 1 < n_r and board[r + 1][c] != '*':
                dfs(r + 1, c, cur, word)
            # LEFT
            if c > 0 and board[r][c - 1] != '*':
                dfs(r, c - 1, cur, word)
            # RIGHT
            if c + 1 < n_c and board[r][c + 1] != '*':
                dfs(r, c + 1, cur, word)

            # Revert changes for possible different valid starting point
            board[r][c] = letter

        trie = Trie()
        ans = set()
        n_r, n_c = len(board), len(board[0])

        for word in words:
            trie.insert(word)

        for r in range(n_r):
            for c in range(n_c):
                dfs(r, c, trie.root, '')

        return list(ans)
