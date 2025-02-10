crossword = []

with open("crossword.txt") as file:
    crossword = [list(line.strip()) for line in file.readlines()]
rows, cols = len(crossword), len(crossword[0])

def find_xmas_in_crossword(row, col, crossword):
    if crossword[row][col] != 'A':
        return 0
    m_count, s_count = 0, 0

    for d_row, d_col in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        m_count += int(crossword[row + d_row][col + d_col] == 'M') 
        s_count += int(crossword[row + d_row][col + d_col] == 'S') 

    if m_count != 2 or s_count != 2:
        return 0
    
    return int(crossword[row - 1][col - 1] != crossword[row + 1][col + 1])

found_count = 0
for start_row in range(1, rows - 1):
    for start_col in range(1, cols - 1):
        found_count += find_xmas_in_crossword(start_row, start_col, crossword)

print(found_count)