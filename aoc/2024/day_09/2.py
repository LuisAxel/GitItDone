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
            file_blocks.append({"start": position, "size": block_size, "id": file_id})
            for _ in range(block_size):
                decompressed_blocks.append(file_id)
                position += 1
            file_id += 1
        else:  # Free memory blocks
            free_blocks.append({"start": position, "size": block_size})
            for _ in range(block_size):
                decompressed_blocks.append(None)
                position += 1

    return file_blocks, free_blocks, decompressed_blocks

def block_fits(file_block, free_blocks):
    file_size, file_position = file_block["size"], file_block["start"]
    for index, free_block in enumerate(free_blocks):
        if file_size <= free_block["size"] and free_block["start"] <= file_position:
            return index, free_block["start"]
    return -1, -1

def move_file_block(file_block, free_blocks, defragged_map):
    space_index, destination = block_fits(file_block, free_blocks)
    if destination != -1:
        for i in range(file_block["size"]):
            defragged_map[destination + i] = file_block["id"]
            defragged_map[file_block["start"] + i] = None
        
        free_blocks[space_index]["start"] += file_block["size"]
        free_blocks[space_index]["size"] -= file_block["size"]
    
    return file_block

def defragment_disk(disk_map):
    file_blocks, free_blocks, defragged_map = decompress_disk_map(disk_map)

    while free_blocks and file_blocks and file_blocks[-1]["start"] > free_blocks[0]["start"]:
        move_file_block(file_blocks.pop(), free_blocks, defragged_map)
    
    return defragged_map

def calculate_checksum(disk_map):
    return sum(index * block_id for index, block_id in enumerate(disk_map) if block_id is not None)


defragged_map = defragment_disk(disk_map)
print(calculate_checksum(defragged_map))