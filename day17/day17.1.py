def get_combo(operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return register_a
    elif operand == 5:
        return register_b
    elif operand == 6:
        return register_c
    else:
        raise ValueError('Invalid operand: {}'.format(operand))


program = []
for i in range(1, 6):
    line = input()
    if i == 1:
        register_a = int(line.split(': ')[1])
    elif i == 2:
        register_b = int(line.split(': ')[1])
    elif i == 3:
        register_c = int(line.split(': ')[1])
    elif i == 5:
        programs = line.split(': ')[1]
        for prog in programs.split(','):
            program.append(int(prog))

instruction_pointer = 0
output = []
while instruction_pointer < len(program):
    opcode = program[instruction_pointer]
    operand = program[instruction_pointer + 1]
    instruction_pointer += 2

    if opcode == 0:  # adv
        register_a //= 2 ** get_combo(operand)
    elif opcode == 1:  # bxl
        register_b ^= operand
    elif opcode == 2:  # bst
        register_b = get_combo(operand) % 8
    elif opcode == 3:  # jnz
        if register_a != 0:
            instruction_pointer = operand
    elif opcode == 4:  # bxc
        register_b ^= register_c
    elif opcode == 5:  # out
        output.append(get_combo(operand) % 8)
    elif opcode == 6:  # bdv
        register_b = register_a // 2 ** get_combo(operand)
    elif opcode == 7:  # cdv
        register_c = register_a // 2 ** get_combo(operand)
    else:
        raise ValueError("Invalid opcode")
print(",".join(map(str, output)))
