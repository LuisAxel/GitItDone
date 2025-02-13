from collections import defaultdict

with open("list.txt") as file:
    list_1, list_2 = zip(*[map(int, line.split()) for line in file])
    list_1 = list(list_1)
    list_2 = list(list_2)

def get_similarity_score(a, b):
    similarity_score = 0
    counter_b = defaultdict(int)

    for num in b:
        counter_b[num] += 1

    for num in a:
        similarity_score += num * counter_b[num]

    return similarity_score

print(get_similarity_score(list_1, list_2))