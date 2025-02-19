from heapq import heappop
from heapq import heappush

maze = []
wall_tile, start_tile, end_tile, empty_tile = '#', 'S', 'E', '.'
walkable_tile = (start_tile, end_tile, empty_tile)

with open("maze.txt") as file:
    maze = [line.strip() for line in file.readlines()]

def get_start_end(maze):

    start, end = None, None
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == start_tile:
                start = [row, col]
            elif maze[row][col] == end_tile:
                end = [row, col]
            
    return start, end

def inbounds(maze, row, col):
    return 0 <= row < len(maze) and 0 <= col < len(maze[0])

def distance_to_tiles(maze, start, end):
    turns = {(0, 1)  : [(1, 0), (-1, 0)], 
             (0, -1) : [(1, 0), (-1, 0)], 
             (1, 0)  : [(0, -1), (0, 1)],
             (-1, 0) : [(0, -1), (0, 1)]}
    
    min_to_path = {}
    min_end_points = None
    
    steps = []
    forward = 1

    if maze[start[0]][start[1]] == start_tile:
        heappush(steps, (0, start[0], start[1], 0, 1))
    else:
        forward = -1
        for (d_row, d_col) in turns.keys():
            heappush(steps, (0, start[0], start[1], d_row, d_col))
            
    while steps:
        points, row, col, d_row, d_col = heappop(steps)

        if (row, col, d_row, d_col) in min_to_path:
            continue

        min_to_path[(row, col, d_row, d_col)] = points

        if maze[row][col] == maze[end[0]][end[1]] and min_end_points is None:
            min_end_points = points

        if min_end_points is not None:
            continue

        for it, step in enumerate([[d_row, d_col]] + turns[(d_row, d_col)]):
            new_row = row + (step[0] * forward)    if it == 0 else row
            new_col = col + (step[1] * forward)    if it == 0 else col
            new_points = 1                         if it == 0 else 1000

            if inbounds(maze, new_row, new_col) and maze[new_row][new_col] in walkable_tile:
                heappush(steps, (points + new_points, new_row, new_col, step[0], step[1]))
    
    return min_to_path, min_end_points

def unique_tiles_in_shortest_path(maze, start, end):

    from_start, shortest_distance = distance_to_tiles(maze, start, end)
    from_end, _ = distance_to_tiles(maze, end, start)

    end_path_tiles = 0

    for row in range(len(maze)):
        for col in range(len(maze[0])):
            for (d_row, d_col) in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                key = (row, col, d_row, d_col)
                if from_start.get(key, float('inf')) + from_end.get(key, float('inf')) == shortest_distance:
                    end_path_tiles += 1
                    break

    return end_path_tiles

start, end = get_start_end(maze)
print(unique_tiles_in_shortest_path(maze, start, end))
