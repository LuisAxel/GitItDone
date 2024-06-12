class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        row = []
        justified = []
        row_len = 0

        for word in words:
            # row_words + spaces 4 each 1 + new_word
            if row_len + len(row) + len(word) <= maxWidth:
                row.append(word)
                row_len += len(word)
                continue

            # Left justified
            if len(row) == 1:
                row[0] += " " * (maxWidth - row_len)
            # Distribute spaces
            else:
                for space in range(maxWidth - row_len):
                    row[space % (len(row) - 1)] += " "

            justified.append("".join(row))
            row, row_len = [word], len(word)

        # last line left justified
        justified.append(" ".join(row))
        justified[-1] += " " * (maxWidth - row_len - len(row) + 1)

        return justified
