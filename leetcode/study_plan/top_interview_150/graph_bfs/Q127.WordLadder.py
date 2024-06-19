class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n = len(beginWord)

        def diff(a, b):
            count = 0
            for i in range(n):
                if a[i] != b[i]:
                    count += 1
                if count > 1:
                    break

            return count

        q = deque()
        seen = set()

        q.append([beginWord, 1])

        while q:
            word, transformations = q.popleft()

            if word in seen:
                continue
            if word == endWord:
                return transformations

            seen.add(word)

            for test in wordList:
                if test in seen:
                    continue
                if diff(word, test) == 1:
                    q.append([test, transformations + 1])
        return 0
