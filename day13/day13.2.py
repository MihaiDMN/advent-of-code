import sys
from math import gcd


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, x, x - y * (a // b)


def solve_linear_diophantine(a, b, c):
    g, x, y = extended_gcd(a, b)
    if c % g != 0:
        return None
    x *= c // g
    y *= c // g
    step_x = b // g
    step_y = -a // g
    return x, y, step_x, step_y


def solve_claw_machine(ax, ay, bx, by, px, py):
    gcd_x = gcd(ax, bx)
    gcd_y = gcd(ay, by)
    if px % gcd_x != 0 or py % gcd_y != 0:
        return None
    scale_x = gcd_x
    scale_y = gcd_y

    xa, xb, xp = ax // scale_x, bx // scale_x, px // scale_x
    ya, yb, yp = ay // scale_y, by // scale_y, py // scale_y

    result = solve_linear_diophantine(xa, xb, xp)
    result2 = solve_linear_diophantine(ya, yb, yp)
    if not result or not result2:
        return None

    x, y, step_x, step_y = result
    x2, y2, step_x2, step_y2 = result2

    best_cost = float('inf')
    best_a, best_b = None, None

    for i in range(-100, 100):
        a = x + i * step_x
        b = y + i * step_y
        for j in range(-100, 100):
            a2 = x2 + j * step_x2
            b2 = y2 + j * step_y2
            if a == a2 and b == b2:
                cost = 3 * a + b
                if cost < best_cost:
                    best_cost = cost
                    best_a = a
                    best_b = b
    if best_cost == float('inf'):
        return None
    return best_cost, best_a, best_b


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
    px = px + 10000000000000
    py = py + 10000000000000
    result = solve_claw_machine(ax, ay, bx, by, px, py)
    if result:
        total_cost += result[0]
print(total_cost)
