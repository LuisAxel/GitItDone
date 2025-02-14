with open("topographic_map.txt") as file:
    topographic_map = [list(map(int, line.strip())) for line in file.readlines()]

rows, cols = len(topographic_map), len(topographic_map[0])
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = set()

def inbounds(row, col):
    return 0 <= row < rows and 0 <= col < cols

def valid_path(row, col, last):
    return topographic_map[row][col] == last + 1

def dfs(row, col):
    if (row, col) in visited:
        return 0
    
    visited.add((row, col))
    if topographic_map[row][col] == 9:
        return 1
    
    found = 0
    for d_row, d_col in directions:
        if inbounds(row + d_row, col + d_col) and valid_path(row + d_row, col + d_col, topographic_map[row][col]):
            found += dfs(row + d_row, col + d_col)
    return found

paths = 0
for row in range(rows):
    for col in range(cols):
        if topographic_map[row][col] == 0:
            visited = set()
            paths += dfs(row, col)

print(paths)