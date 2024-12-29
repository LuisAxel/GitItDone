class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for i in range(len(word1)):
            count1[word1[i]] += 1
            count2[word2[i]] += 1

        for char in count1.keys():
            if char not in count2:
                return False

        freq1 = sorted(count1.values())
        freq2 = sorted(count2.values())

        return freq1 == freq2
