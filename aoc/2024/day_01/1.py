with open("list.txt") as file:
    list_1, list_2 = zip(*[map(int, line.split()) for line in file])
    list_1 = list(list_1)
    list_2 = list(list_2)

def get_min_distance_sum(a, b):
    a.sort()
    b.sort()
    min_distance_sum = 0

    for num_1, num_2 in zip(a, b):
        min_distance_sum += abs(num_1 - num_2)

    return min_distance_sum

print(get_min_distance_sum(list_1, list_2))