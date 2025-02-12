from re import findall
from operator import add
from operator import mul
from collections import deque

with open("equations.txt") as file:
    equations_pattern = r"(\d+):((?: \d+)+)"
    tokens = findall(equations_pattern, "".join(file.readlines()))

def check_equation(target, operands):
    if not operands:
        return 0
    
    operators = [add, mul]
    queue = deque([[operands[0], 1]]) # curr value, next operand idx

    while queue:
        value, next_operand_idx = queue.popleft()
        
        if next_operand_idx == len(operands) and value == target :
            return target

        if next_operand_idx >= len(operands):
            continue

        next_operand = operands[next_operand_idx]
        for op in operators:
            new_val = op(value, next_operand)
            if new_val <= target:
                queue.append([new_val, next_operand_idx + 1])
            
    return 0


equation = []
valid_equation_sum = 0
for token in tokens:
    target = int(token[0])
    operands = list(map(int, token[1].split()))
    valid_equation_sum += check_equation(target, operands)

print(valid_equation_sum)