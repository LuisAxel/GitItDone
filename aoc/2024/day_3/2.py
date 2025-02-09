from re import findall

def process_memory(memory):
    operation_pattern = r"(mul\((-?\d{1,3}),(-?\d{1,3})\)|do\(\)|don't\(\))"
    
    tokens = findall(operation_pattern, memory) 

    total_sum = 0
    enabled = True
    for token in tokens:
        if token[0] == "do()":
            enabled = True
        elif token[0] == "don't()":
            enabled = False
        elif enabled:
            a, b = map(int, token[1:])
            total_sum += a * b
    return total_sum

with open("corrupted_memory.txt") as file:
    corrupted_memory = file.read()

print(process_memory(corrupted_memory))