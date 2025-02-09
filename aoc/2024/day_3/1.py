from re import findall

def process_memory(memory):
    mul_pattern = r"mul\((-?\d{1,3}),(-?\d{1,3})\)"
    
    tokens = findall(mul_pattern, memory)
    
    total_sum = 0
    for token in tokens:
        a, b = map(int, token)
        total_sum += a * b
    return total_sum

with open("corrupted_memory.txt") as file:
    corrupted_memory = file.read()

print(process_memory(corrupted_memory))