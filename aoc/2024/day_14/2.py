from re import findall

with open("robots.txt") as file:
    contents = file.read()
    robot_pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
    robots_info = [list(map(int, match)) for match in findall(robot_pattern, contents)]

rows, cols = 103, 101
grid = [[0 for _ in range(cols)] for __ in range(rows)]

def inbounds(row, col):
    return 0 <= row < rows and 0 <= col < cols

def calculate_robot_position(x, y, v_x, v_y, times):
    new_x = x + (v_x * times)
    new_y = y + (v_y * times)
    return new_x % cols, new_y % rows

def emulate_positions(robots_info, second):
    grid = [[0 for _ in range(cols)] for __ in range(rows)]
    for r_x, r_y, v_x, v_y in robots_info:
        new_x, new_y = calculate_robot_position(r_x, r_y, v_x, v_y, second)
        grid[new_y][new_x] += 1
    return grid

def count_surrounded_robots(grid):
    count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] >= 1:
                candidate = 0
                for d_r, d_c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    new_r, new_c = row + d_r, col + d_c
                    if inbounds(new_r, new_c) and grid[new_r][new_c] >= 1:
                        candidate += 1
                count += int(candidate == 4)
    return count

def print_grid(grid):
    for row in grid:
        for v in row:
            if v <= 0:
                print(" ", end='')
            else:
                print("#", end='')
        print()

most_surrounded = float('-inf')
ocurred_at = -1
for i in range(rows * cols): # 1 full cycle
    count = count_surrounded_robots(emulate_positions(robots_info, i))
    if most_surrounded < count:
        ocurred_at = i
        most_surrounded = count

print_grid(emulate_positions(robots_info, ocurred_at))
print(most_surrounded, ocurred_at)