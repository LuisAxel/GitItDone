directions = {'^' : (-1, 0), 'v' : (1, 0), '<' : (0, -1), '>' : (0, 1)}
turn = {'^' : '>', '>' : 'v', 'v' : '<', '<' : '^'}

def count_loops_in_maze(row, col, direction, checking_for_loop = False):
    step = directions[direction]
    visited = set()
    placed_walls = set()
    loops = 0
    
    while 0 <= row + step[0] < rows and 0 <= col + step[1] < cols:
        
        # Loop found, exit
        if (row, col, direction) in visited:
            return 1
        
        visited.add((row, col, direction))

        new_row = row + step[0]
        new_col = col + step[1]
        
        # Stay in place and turn
        if maze[new_row][new_col] == '#':
            direction = turn[direction]
            step = directions[direction]
            new_row = row
            new_col = col
        # Add temporary wall and check if loop is created
        elif checking_for_loop and maze[new_row][new_col] == '.' and (new_row, new_col) not in placed_walls:
            maze[new_row][new_col] = '#'
            placed_walls.add((new_row, new_col))
            loops += count_loops_in_maze(row, col, direction)
            maze[new_row][new_col] = '.'
        
        row = new_row
        col = new_col

    return loops

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


print(count_loops_in_maze(start_row, start_col, start_direction, True))
