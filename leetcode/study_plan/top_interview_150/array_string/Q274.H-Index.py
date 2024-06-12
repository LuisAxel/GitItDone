class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = [0] * 1001

        # Count number of books with n citations
        for i in range(len(citations)):
            count[citations[i]] += 1

        prev = 0
        # Check if for n citations theres at least n books
        for i in range(1000, -1, -1):
            if count[i] + prev >= i:
                return i
            prev += count[i]

        return 0
