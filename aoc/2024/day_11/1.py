
with open("stones.txt") as file:
    stones = [line.strip() for line in file.readlines()]
    stones = list(map(int, stones[0].split()))

digits_count = {}
num_halves = {}

def count_digits(num):
    if num in digits_count:
        return digits_count[num]
    
    digits = 1
    aux = num
    while aux >= 10:
        aux //= 10
        digits += 1
    digits_count[num] = digits
    return digits

def split_num(num):
    if num in num_halves:
        return num_halves[num]
    
    digits = count_digits(num)
    half = digits // 2
    
    left = num // (10 ** half)
    right = num % (10 ** half)

    num_halves[num] = (left, right)
    return left, right

def blink(stone):
    if stone == 0:
        return 1
    digits = count_digits(stone)
    if digits % 2 == 0:
        return split_num(stone)
    return stone * 2024

iterations = 25
for i in range(iterations):
    new_stones = []
    for stone in stones:
        result = blink(stone)
        if isinstance(result, tuple):
            new_stones.extend(result)
        else:
            new_stones.append(result)
    stones = new_stones

print(len(stones))