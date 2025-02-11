from collections import defaultdict
from collections import deque

rules = []
updates = []

with open("rules_and_updates.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if "|" in line:
            rules.append(list(map(int, line.split("|"))))
        elif line:
            updates.append(list(map(int, line.split(","))))

def graph_order(rules, update):
    graph = defaultdict(set)
    in_degree = defaultdict(int)

    for a, b in rules:
        # Using the full set of rules creates cycles
        # Graphs containing only numbers from 1 update create a DAG
        if a not in update or b not in update:
            continue

        in_degree.setdefault(a, 0)
        in_degree.setdefault(b, 0)
        graph[a].add(b)
        in_degree[b] += 1

    # Numbers not in rules have rank 0
    for update in updates:
        for a in update:
            in_degree.setdefault(a, 0)
    
    rank = defaultdict(int)
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    # Toposort
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            rank[neighbor] = rank[node] + 1
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return rank

sum_fixed_updates = 0
for update in updates:
    rank = graph_order(rules, update)
    print(rank)
    fixed_update = sorted(update, key = lambda x : rank[x])
    if update != fixed_update:
        sum_fixed_updates += fixed_update[len(fixed_update) // 2]
    
print(sum_fixed_updates)