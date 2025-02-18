warehouse = []
instructions = []
directions = {'^' : (-1, 0), '>' : (0, 1), 'v' : (1, 0), '<' : (0, -1)}
wall, box, empty, robot = '#', 'O', '.', '@'

with open("warehouse.txt") as file:
    reading_warehoue = True
    
    for line in file:
        line = line.strip()

        if not line:
            reading_warehoue = False
            continue
        
        if reading_warehoue:
            warehouse.append([char for char in line])
        else:
            instructions.extend(line)

def push_box(warehouse, row, col, direction):
    
    while warehouse[row][col] != empty:
        # Reached wall, cant push
        if warehouse[row][col] == wall:
            return False
        row += direction[0]
        col += direction[1]

    warehouse[row][col] = box
    return True


def move_robot(warehouse, row, col, direction):
    new_row, new_col = row + direction[0], col + direction[1]

    # Stuck at wall, didnt move
    if warehouse[new_row][new_col] == wall:
        new_row, new_col = row, col
    
    # Push box or stay in place
    elif warehouse[new_row][new_col] == box:
        if not push_box(warehouse, new_row, new_col, direction):
            new_row, new_col = row, col

    warehouse[row][col] = empty
    warehouse[new_row][new_col] = robot
    return new_row, new_col

def initial_position(warehouse):

    rows, cols = len(warehouse), len(warehouse[0])
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if warehouse[row][col] == robot:
                return row, col

    return None, None

def sum_of_gps(warehouse):
    
    gps_sum = 0
    rows, cols = len(warehouse), len(warehouse[0])
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if warehouse[row][col] == box:
                gps_sum += (100 * row) + col

    return gps_sum

row, col = initial_position(warehouse)
for instruction in instructions:
    row, col = move_robot(warehouse, row, col, directions[instruction])

print(sum_of_gps(warehouse))
