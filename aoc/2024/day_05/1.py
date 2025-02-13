from collections import defaultdict

rules = defaultdict(set)
updates = []

with open("rules_and_updates.txt") as file:
    for line in file.readlines():
        line = line.strip()
        if "|" in line:
            line = line.split("|")
            rules[int(line[1])].add(int(line[0]))
        elif line:
            updates.append(list(map(int, line.split(","))))

def valid_update(rules, update):
    cant_see = set()
    for number in update:
        if number in cant_see:
            return False
        cant_see.update(rules[number])
    return True

sum_correct_updates = 0
for update in updates:
    if valid_update(rules, update):
        sum_correct_updates += update[len(update)//2]
    
print(sum_correct_updates)