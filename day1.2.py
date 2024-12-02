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
score = 0
for i in range(len(list_1)):
    cnt = 0
    for j in range(len(list_2)):
        if list_1[i] == list_2[j]:
            cnt += 1
        if list_1[i] < list_2[j]:
            break
    score += list_1[i] * cnt

print(score)
