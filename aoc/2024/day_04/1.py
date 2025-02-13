crossword = []

with open("crossword.txt") as file:
    crossword = [list(line.strip()) for line in file.readlines()]
rows, cols = len(crossword), len(crossword[0])

def inbounds(row, col):
    return 0 <= row < rows and 0 <= col < cols

def find_word_in_crossword(row, col, direction, crossword, word):
    find_idx = 0
    while inbounds(row, col):
        if crossword[row][col] != word[find_idx]:
            break
        if find_idx == len(word) - 1:
            return 1
        row, col = row + direction[0], col + direction[1]
        find_idx += 1
    return 0

word = "XMAS"
found_count = 0
directions = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1))
for start_row in range(rows):
    for start_col in range(cols):
        for direction in directions:
            found_count += find_word_in_crossword(start_row, start_col, direction, crossword, word)
print(found_count)