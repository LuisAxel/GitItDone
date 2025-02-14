
with open("stones.txt") as file:
    stones = [line.strip() for line in file.readlines()]
    stones = list(map(int, stones[0].split()))

even_nums = {}
num_digits = {}
num_halves = {}
stone_res = {}

def count_digits(num):
    if num in num_digits:
        return num_digits[num]
    
    count = 1
    aux = num
    while aux >= 10:
        aux //= 10
        count += 1
    num_digits[num] = count
    return count

def is_even(num):
    return even_nums.setdefault(num , count_digits(num) % 2 == 0)

def split_num(num):
    if num in num_halves:
        return num_halves[num]
    
    digits = count_digits(num)
    half = digits // 2
    
    left = num // (10 ** half)
    right = num % (10 ** half)

    num_halves[num] = (left, right)
    return left, right

def blink(stone, time):
    if (stone, time) in stone_res:
        return stone_res[(stone, time)]
    
    if time == 0:
        stone_count = 1
    elif stone == 0:
        stone_count = blink(1, time - 1)
    elif is_even(stone):
        left, right = split_num(stone)
        stone_count = blink(left, time - 1) + blink(right, time - 1)
    else:
        stone_count = blink(stone * 2024, time - 1)
    
    stone_res[(stone, time)] = stone_count
    return stone_count

iterations = 75
ans = sum(blink(stone, iterations) for stone in stones)

print(ans)