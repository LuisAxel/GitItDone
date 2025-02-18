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

def get_safety_factor(grid):
    q = [[0, 0], \
         [0, 0]] # Quadrants
    for row in range(rows):
        if rows % 2 == 1 and row == rows // 2:
            continue
        for col in range(cols):
            if cols % 2 == 1 and col == cols // 2:
                continue
            if grid[row][col] > 0:
                q[int(row > rows // 2)][int(col > cols // 2)] += grid[row][col]
    return q[0][0] * q[0][1] * q[1][0] * q[1][1]

print(get_safety_factor(emulate_positions(robots_info, 100)))