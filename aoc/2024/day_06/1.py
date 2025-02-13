from collections import defaultdict

directions = {'^' : (-1, 0), 'v' : (1, 0), '<' : (0, -1), '>' : (0, 1)}
turn = {'^' : '>', '>' : 'v', 'v' : '<', '<' : '^'}

def count_visited_in_maze(row, col, direction):
    step = directions[direction]
    visited = defaultdict(set)
    while 0 <= row + step[0] < rows and 0 <= col + step[1] < cols:
        
        # Loop found, exit
        if direction in visited[(row, col)]:
            return len(visited.keys()) 
        
        visited[(row, col)].add(direction)

        new_row = row + step[0]
        new_col = col + step[1]
        
        # Stay in place and turn
        if maze[new_row][new_col] == '#':
            direction = turn[direction]
            step = directions[direction]
            new_row = row
            new_col = col
        
        row = new_row
        col = new_col

    return len(visited.keys()) + 1 # Cell next to exit

with open('maze.txt') as file:
    maze = [list(line.strip()) for line in file]

rows, cols = len(maze), len(maze[0])
start_row, start_col, start_direction = None, None, None

for row in range(rows):
    for col in range(cols):
        if maze[row][col] in directions:
            start_row, start_col = row, col
            start_direction = maze[row][col]
            maze[row][col] = '.'
            
print(count_visited_in_maze(start_row, start_col, start_direction))
