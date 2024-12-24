class Solution:
    def compress(self, chars: List[str]) -> int:
        reader = writer = count = 0
        n = len(chars)

        while reader < n:
            cur = chars[reader]
            count = 0

            while reader < n and chars[reader] == cur:
                count += 1
                reader += 1

            chars[writer] = cur
            writer += 1

            if count == 1:
                continue

            for digit in str(count):
                chars[writer] = digit
                writer += 1

        return writer
