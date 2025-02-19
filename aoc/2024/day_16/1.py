import heapq

maze = []
wall_tile, start_tile, end_tile, empty_tile = '#', 'S', 'E', '.'
walkable_tile = (start_tile, end_tile, empty_tile)

with open("maze.txt") as file:
    maze = [line.strip() for line in file.readlines()]

def get_start(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == start_tile:
                return row, col
    return None, None

def inbounds(maze, row, col):
    return 0 <= row < len(maze) and 0 <= col < len(maze[0])

def min_points(maze, start):
    
    turns = {(0, 1)  : [(1, 0), (-1, 0)], 
             (0, -1) : [(1, 0), (-1, 0)], 
             (1, 0)  : [(0, -1), (0, 1)],
             (-1, 0) : [(0, -1), (0, 1)]}

    visited = set()
    steps = [(0, start[0], start[1], 0, 1)] 

    while steps:
        points, row, col, d_row, d_col = heapq.heappop(steps)

        if maze[row][col] == end_tile:
            return points
        
        if (row, col, d_row, d_col) in visited:
            continue

        visited.add((row, col, d_row, d_col))
        
        for it, step in enumerate([[d_row, d_col]] + turns[(d_row, d_col)]):
            new_row = row + step[0] if it == 0 else row  # Step or stay in place and turn
            new_col = col + step[1] if it == 0 else col
            new_points = 1          if it == 0 else 1000

            if inbounds(maze, new_row, new_col) and maze[new_row][new_col] in walkable_tile:
                heapq.heappush(steps, (points + new_points, new_row, new_col, step[0], step[1]))

    return -1 # No end tile

print(min_points(maze, get_start(maze)))
