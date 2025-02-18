warehouse = []
instructions = []
directions = {'^' : (-1, 0), '>' : (0, 1), 'v' : (1, 0), '<' : (0, -1)}
wall, old_box, box, empty, robot = '#', 'O', ['[', ']'], '.', '@'

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

def push_box_up_down(warehouse, row, col, direction):
    left = col - 1 if warehouse[row][col] == box[1] else col

    boxes_to_push = [(row, left)]
    pushing_boxes = [(row, left)]
    while pushing_boxes:
        row, left = pushing_boxes.pop()
        new_row = row + direction

        # Reached wall, cant push
        if warehouse[new_row][left] == wall or warehouse[new_row][left + 1] == wall:
            return False
        
        # Append boxes being pushed
        for neigh in range(left - 1, left + 2):
            if warehouse[new_row][neigh] == box[0]:
                pushing_boxes.append((new_row, neigh))
                boxes_to_push.append((new_row, neigh))

        row = new_row

    while boxes_to_push:
        row, left = boxes_to_push.pop()
        new_row = row + direction
        warehouse[row][left] = empty
        warehouse[row][left + 1] = empty
        warehouse[new_row][left] = box[0]
        warehouse[new_row][left + 1] = box[1]

    return True

def push_box_left_right(warehouse, row, col, direction):

    initial_col = col
    while warehouse[row][col] != empty:
        # Reached wall, cant push
        if warehouse[row][col] == wall:
            return False 
        col += direction * 2 # wide
 
    for i in range(col, initial_col, - direction):
        warehouse[row][i] = warehouse[row][i - direction]

    return True

def push_box(warehouse, row, col, direction):
    if direction in ((0, 1), (0, -1)):
        return push_box_left_right(warehouse, row, col, direction[1])
    return push_box_up_down(warehouse, row, col, direction[0])

def move_robot(warehouse, row, col, direction):
    new_row, new_col = row + direction[0], col + direction[1]

    # Stuck at wall, didnt move
    if warehouse[new_row][new_col] == wall:
        new_row, new_col = row, col
    
    # Push box or stay in place
    elif warehouse[new_row][new_col] in box:
        if not push_box(warehouse, new_row, new_col, direction):
            new_row, new_col = row, col

    warehouse[row][col] = empty
    warehouse[new_row][new_col] = robot
    return new_row, new_col

def initial_position(warehouse):

    rows, cols = len(warehouse), len(warehouse[0])
    for row in range(2, rows - 2):
        for col in range(2, cols - 2):
            if warehouse[row][col] == robot:
                return row, col

    return None, None

def sum_of_gps(warehouse):
    gps_sum = 0
    rows, cols = len(warehouse), len(warehouse[0])
    for row in range(1, rows - 1):
        for col in range(2, cols - 2):
            if warehouse[row][col] == box[0]:
                gps_sum += (100 * row) + col
    return gps_sum

def resize_warehouse(warehouse):
    expanded_warehouse = []
    rows, cols = len(warehouse), len(warehouse[0])

    for row in range(rows):
        new_row = []
        for col in range(cols):
            tile = warehouse[row][col]
            
            if tile == robot:
                new_row.extend([robot, empty])
            elif tile in {wall, empty}:
                new_row.extend([tile, tile])
            elif tile == old_box:
                new_row.extend(box)
            
        expanded_warehouse.append(new_row)

    return expanded_warehouse


warehouse = resize_warehouse(warehouse)
row, col = initial_position(warehouse)

for instruction in instructions:
    row, col = move_robot(warehouse, row, col, directions[instruction])

print(sum_of_gps(warehouse))
