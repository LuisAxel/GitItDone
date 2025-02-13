from collections import deque
from collections import defaultdict

with open("antenna_map.txt") as file:
    antenna_map = [line.strip() for line in file.readlines()]

rows, cols = len(antenna_map), len(antenna_map[0])

def inbounds(row, col):
    return 0 <= row < rows and 0 <= col < cols

def find_antennas():
    antennas = defaultdict(list)
    for row in range(0, rows):
        for col in range(0, cols):
            candidate = antenna_map[row][col]
            if candidate != '.':
                antennas[candidate].append((row, col))
    return antennas

def get_antinodes(antenna_1, antenna_2):
    antinodes = set()

    d_row, d_col = antenna_1[0] - antenna_2[0], antenna_1[1] - antenna_2[1]
    row, col = antenna_1
    if inbounds(row + d_row, col + d_col):
        antinodes.add((row + d_row, col + d_col))

    row, col = antenna_2
    if inbounds(row - d_row, col - d_col):
        antinodes.add((row - d_row, col - d_col))

    return antinodes


def get_anti_nodes_count():
    antenna_positions = find_antennas()
    antinodes = set()

    for positions in antenna_positions.values():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                antinodes.update(get_antinodes(positions[i], positions[j]))
    return len(antinodes)

print(get_anti_nodes_count())