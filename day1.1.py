list_1 = []
list_2 = []

line = input()

while line != '':
    line = line.split('   ')
    list_1.append(int(line[0]))
    list_2.append(int(line[1]))
    try:
        line = input()
    except EOFError:
        break

list_1.sort()
list_2.sort()
distance = 0
for _ in range(len(list_1)):
    distance += abs(list_1[_] - list_2[_])

print(distance)
