def blink(numbers):
    new_numbers = []
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 1
            new_numbers.append(numbers[i])
        elif len(str(numbers[i])) % 2 == 0:
            first_half = str(numbers[i])[:len(str(numbers[i]))//2]
            second_half = str(numbers[i])[len(str(numbers[i]))//2:]
            new_numbers.append(int(first_half))
            new_numbers.append(int(second_half))
        else:
            numbers[i] = numbers[i] * 2024
            new_numbers.append(numbers[i])
    return new_numbers


line = input()

numbers = [int(x) for x in line.split(" ")]
cnt = 0
while cnt < 25:
    print("Blinking", cnt)
    numbers = blink(numbers)
    cnt += 1
print(len(numbers))
