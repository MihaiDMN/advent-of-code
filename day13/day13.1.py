import sys
from math import gcd
from itertools import product


def solve_claw_machine(ax, ay, bx, by, px, py):
    results = []
    gcd_x = gcd(ax, bx)
    gcd_y = gcd(ay, by)
    if px % gcd_x != 0 or py % gcd_y != 0:
        return None
    scale_x = gcd_x
    scale_y = gcd_y

    xa, xb, xp = ax // scale_x, bx // scale_x, px // scale_x
    ya, yb, yp = ay // scale_y, by // scale_y, py // scale_y

    for a, b in product(range(101), repeat=2):
        if a * xa + b * xb == xp and a * ya + b * yb == yp:
            cost = 3 * a + b
            results.append((cost, a, b))
    if results:
        return min(results)
    return None


input = sys.stdin.read()
total_cost = 0
sections = input.strip().split('\n\n')
for section in sections:
    lines = section.split('\n')
    button_a = lines[0].split(":")[1].strip().split(",")
    button_b = lines[1].split(":")[1].strip().split(",")
    prize = lines[2].split(":")[1].strip().split(",")
    ax = int(button_a[0].strip().split("+")[1])
    ay = int(button_a[1].strip().split("+")[1])
    bx = int(button_b[0].strip().split("+")[1])
    by = int(button_b[1].strip().split("+")[1])
    px = int(prize[0].strip().split("=")[1])
    py = int(prize[1].strip().split("=")[1])
    result = solve_claw_machine(ax, ay, bx, by, px, py)
    if result:
        total_cost += result[0]
print(total_cost)
