class Solution:
    def compress(self, chars: List[str]) -> int:
        writer = reader = count = 0
        n = len(chars)

        while reader < n:
            cur = chars[reader]
            count = 0

            while reader < n and chars[reader] == cur:
                reader += 1
                count += 1

            chars[writer] = cur
            writer += 1

            if count == 1:
                continue

            for c in str(count):
                chars[writer] = c
                writer += 1

        return writer
