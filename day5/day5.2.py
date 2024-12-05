import sys


def correct_order(rules, update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) >= update.index(rule[1]):
                return False
    return True


def fix_order(rules, update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) >= update.index(rule[1]):
                update[update.index(rule[0])] = rule[1]
                update[update.index(rule[1])] = rule[0]
    if correct_order(rules, update):
        return update
    else:
        return fix_order(rules, update)


input = sys.stdin.read()

sections = input.strip().split('\n\n')
rules = [_.split("|") for _ in sections[0].split('\n')]
updates = [_.split(",") for _ in sections[1].split('\n')]

total = 0
for update in updates:
    if not correct_order(rules, update):
        fix_order(rules, update)
        middle = update[len(update)//2]
        total += int(middle)
print(total)
