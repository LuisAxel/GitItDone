class Solution:
    def reverseWords(self, s: str) -> str:
	# Make list of words
        s = s.split()
        i, j = 0, len(s) - 1
	# Reverse words
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
	# Join with space
        return " ".join(s)
