from collections import deque

with open("disk_map.txt") as file:
    disk_map = [int(block) for block in file.readline()]

def decompress_disk_map(disk_map):
    file_blocks = deque()
    free_blocks = deque()
    decompressed_blocks = []
    position, file_id = 0, 0

    for index, block_size in enumerate(disk_map):
        if index % 2 == 0:  # File blocks
            for _ in range(block_size):
                file_blocks.append({"position": position, "id": file_id})
                decompressed_blocks.append(file_id)
                position += 1
            file_id += 1
        else:  # Free memory blocks
            for _ in range(block_size):
                free_blocks.append({"position": position})
                decompressed_blocks.append(None)
                position += 1

    return file_blocks, free_blocks, decompressed_blocks

def move_file_block(file_blocks, free_blocks, defragged_map):
    free_position = free_blocks.popleft()["position"]
    file_block = file_blocks.pop()
    file_position, file_id = file_block["position"], file_block["id"]
    
    defragged_map[free_position] = file_id
    defragged_map[file_position] = None

def defragment_disk(disk_map):
    file_blocks, free_blocks, defragged_map = decompress_disk_map(disk_map)

    while free_blocks and file_blocks and file_blocks[-1]["position"] > free_blocks[0]["position"]:
        move_file_block(file_blocks, free_blocks, defragged_map)
    
    return defragged_map

def calculate_checksum(disk_map):
    return sum(index * block_id for index, block_id in enumerate(disk_map) if block_id is not None)

defragment_map = defragment_disk(disk_map)
print(calculate_checksum(defragment_map))