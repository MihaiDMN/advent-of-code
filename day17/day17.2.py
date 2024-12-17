def run_program_with_A(initial_A, program):
    A, B, C = initial_A, 0, 0
    instruction_pointer = 0
    output = []

    def get_combo_value(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        else:
            raise ValueError("Invalid combo operand")

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        instruction_pointer += 2

        if opcode == 0:
            A //= 2 ** get_combo_value(operand)
        elif opcode == 1:
            B ^= operand
        elif opcode == 2:
            B = get_combo_value(operand) % 8
        elif opcode == 3:
            if A != 0:
                instruction_pointer = operand
        elif opcode == 4:
            B ^= C
        elif opcode == 5:
            output.append(get_combo_value(operand) % 8)
        elif opcode == 6:
            B = A // 2 ** get_combo_value(operand)
        elif opcode == 7:
            C = A // 2 ** get_combo_value(operand)
        else:
            raise ValueError("Invalid opcode")

    return output


def find_lowest_A(program):
    target_output = program[:]
    A = 1

    while True:
        output = run_program_with_A(A, program)
        if output == target_output:
            return A
        A += 1


program = [2, 4, 1, 6, 7, 5, 4, 4, 1, 7, 0, 3, 5, 5, 3, 0]


lowest_A = find_lowest_A(program)
print("The lowest positive initial value for register A is:", lowest_A)
