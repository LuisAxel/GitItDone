class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        can_build = [False] * n

        for i in range(0,n):
            for word in wordDict:
                # Missing chars to build this word
                if i < len(word) - 1:
                    continue

                # creating from start or at
                # past created position
                if i == len(word) - 1 or can_build[i - len(word)]:
                    if s[i - len(word) + 1 : i + 1] == word:
                        can_build[i] = True
                        break

        return can_build[-1]
