from collections import defaultdict

with open("garden.txt") as file:
    garden = [line.strip() for line in file.readlines()]

rows, cols = len(garden), len(garden[0])
# Plant : (area, perimeter)
plots = defaultdict(lambda : [0, 0])
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
visited = set()

def inbounds(row, col):
    return 0 <= row < rows and 0 <= col < cols

def traverse_plot(plant, row, col):
    if (row, col) in visited:
        return
    visited.add((row, col))
    plots[plant][0] += 1  # Increment area

    for d_row, d_col in directions:
        nr, nc = row + d_row, col + d_col
        if inbounds(nr, nc) and garden[nr][nc] == plant:
            traverse_plot(plant, nr, nc)
        else:
            plots[plant][1] += 1  # Increment perimeter

cost = 0
for row in range(rows):
    for col in range(cols):
        if (row, col) not in visited:
            traverse_plot(garden[row][col], row, col)
            cost += plots[garden[row][col]][0] * plots[garden[row][col]][1]
            plots.clear()

print(cost)


