import re

equations = []
with open("configs.txt") as file:
    content = file.read()
    a_pattern = r"Button A: X\+(\d+), Y\+(\d+)"
    b_pattern = r"Button B: X\+(\d+), Y\+(\d+)"
    p_pattern = r"Prize: X=(\d+), Y=(\d+)"

    a_tokens = [tuple(map(int, match)) for match in re.findall(a_pattern, content)]
    b_tokens = [tuple(map(int, match)) for match in re.findall(b_pattern, content)]
    p_tokens = [tuple(map(int, match)) for match in re.findall(p_pattern, content)]

    for equation in zip(a_tokens, b_tokens, p_tokens):
        equations.append(equation)

def solve(equation):
    a, b, p = equation
    a_presses = (p[0] * b[1] - p[1] * b[0]) / (a[0] * b[1] - a[1] * b[0])
    b_presses = (p[0] - a[0] * a_presses) / b[0]
    return a_presses, b_presses

cost = 0
for equation in equations:
    presses = solve(equation)

    if presses[0].is_integer() and presses[1].is_integer() and presses[0] < 100 and presses[1] < 100:
        cost += (3 *presses[0]) + presses[1]

print(cost)