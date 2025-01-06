class Trie:

    def __init__(self):
        self.root = {}
        self.root['sug'] = []

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
                cur[letter]['sug'] = []
            if len(cur['sug']) < 3 and word not in cur['sug']:
                cur['sug'].append(word)
            cur = cur[letter]
        if len(cur['sug']) < 3 and word not in cur['sug']:
                cur['sug'].append(word)

    def search(self, word: str) -> list:
        cur = self.root
        for letter in word:
            if letter not in cur:
                return []
            cur = cur[letter]
        return cur['sug']


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        products.sort()
        for product in products:
            trie.insert(product)

        ans = []
        for i in range(1, len(searchWord) + 1):
            ans.append(trie.search(searchWord[:i]))

        return ans
