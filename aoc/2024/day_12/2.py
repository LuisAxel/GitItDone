from collections import defaultdict

with open("garden.txt") as file:
    garden = [line.strip() for line in file.readlines()]

rows, cols = len(garden), len(garden[0])
# Plant : (area, sides)
# direction : (row, col)
plots = defaultdict(lambda : [0, defaultdict(list)])
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
            # Record boundary wall
            plots[plant][1][(d_row, d_col)].append((row, col))
            
def count_sides(walls):
    sides = 0
    for direction in directions:
        if not walls[direction]:
            continue 
        if direction in ((1, 0), (-1, 0)):
            walls[direction].sort(key=lambda x: (x[0], x[1]))
        else:
            walls[direction].sort(key=lambda x: (x[1], x[0]))

        last_wall = walls[direction][0]
        sides += 1  # At least 1 wall
        for wall in walls[direction][1:]:
            if direction in ((1, 0), (-1, 0)):
                # !same row and adjacent columns
                if wall[0] != last_wall[0] or abs(wall[1] - last_wall[1]) != 1:
                    sides += 1
            else:
                # !same col and adjacent rows
                if wall[1] != last_wall[1] or abs(wall[0] - last_wall[0]) != 1:
                    sides += 1
            last_wall = wall
    return sides

cost = 0
for row in range(rows):
    for col in range(cols):
        if (row, col) not in visited:
            traverse_plot(garden[row][col], row, col)
            cost += plots[garden[row][col]][0] * count_sides(plots[garden[row][col]][1])
            plots.clear()
print(cost)