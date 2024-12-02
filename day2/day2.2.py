
def check_safety(report: list[int]) -> bool:
    errors = 0
    decreasing = None
    if report[1] < report[0]:
        decreasing = True
    elif report[1] > report[0]:
        decreasing = False
    for i in range(1, len(report)):
        if report[i] < report[i-1] and not decreasing:
            if i >= 2:
                if report[i] < report[i-2]:
                    return False
        elif report[i] > report[i-1] and decreasing:
            if i >= 2:
                if report[i] > report[i-2]:
                    return False
        elif report[i] < report[i-1]:
            if report[i-1] - report[i] < 1 or report[i-1] - report[i] > 3:
                return False
        elif report[i] > report[i-1]:
            if report[i] - report[i-1] < 1 or report[i] - report[i - 1] > 3:
                return False
        elif report[i] == report[i-1]:
            errors += 1
    if errors > 1:
        return False
    return True


reports = []
line = input()
counter = 0
while line != '':
    report = []
    line = line.split(' ')
    for _ in range(len(line)):
        report.append(int(line[_]))
    reports.append(report)
    try:
        line = input()
    except EOFError:
        break

for report in reports:
    if check_safety(report):
        counter += 1

print(counter)
