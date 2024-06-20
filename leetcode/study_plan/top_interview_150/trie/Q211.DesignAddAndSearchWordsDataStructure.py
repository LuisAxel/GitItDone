class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        cur['EOS'] = ''

    def search(self, word: str) -> bool:
        def dfs(root, word, idx, n):
            # Ended word on EOS dict
            if idx == n and 'EOS' in root:
                return True
            # Ended word but not EOS
            elif idx == n:
                return False

            # Recursively search for all child dicts
            if word[idx] == '.':
                for k in root.keys():
                    if k != 'EOS':
                        # Ended word and found EOS
                        if dfs(root[k], word, idx + 1, n):
                            return True
            else:
                if word[idx] not in root:
                    return False
                return dfs(root[word[idx]], word, idx + 1, n)

        return dfs(self.root, word, 0, len(word))


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
