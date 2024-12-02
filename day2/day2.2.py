
def check_safety(report: list[int]) -> bool:
    if report[1] < report[0]:
        for i in range(1, len(report)):
            difference = report[i-1] - report[i]
            if difference < 1 or difference > 3:
                return False

    elif report[1] > report[0]:
        for i in range(1, len(report)):
            difference = report[i] - report[i-1]
            if difference < 1 or difference > 3:
                return False

    elif report[1] == report[0]:
        return False

    return True


def check_safety_error(report: list[int]) -> bool:
    if report[1] < report[0]:
        for i in range(1, len(report)):
            difference = report[i-1] - report[i]
            if difference < 1 or difference > 3:
                report = report[:i-1] + report[i:]
                return check_safety(report)

    elif report[1] > report[0]:
        for i in range(1, len(report)):
            difference = report[i] - report[i-1]
            if difference < 1 or difference > 3:
                report = report[:i-1] + report[i:]
                return check_safety(report)

    elif report[1] == report[0]:
        report = report[1:]
        return check_safety(report)

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
    if check_safety_error(report):
        counter += 1

print(counter)
