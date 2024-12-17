current_dir = "/".join(__file__.split("\\")[:-1])
data = open(f"{current_dir}/input.txt", "r").readlines()
program = [int(x) for x in data[-1].split(": ")[1].split(",")]

def get_combo_operand(operand_code, A, B, C):
    if 0 <= operand_code <= 3:
        return operand_code
    if operand_code == 4:
        return A
    if operand_code == 5:
        return B
    if operand_code == 6:
        return C
    if operand_code == 7:
        raise TypeError
    assert 0 == 1

def next_state(A, B, C, current_instruction, output):
    opcode, operand_code = program[current_instruction], program[current_instruction+1]
    combo_operand = get_combo_operand(operand_code, A, B, C)

    match opcode:            
            case 0:
                A = A // (2 ** combo_operand)
                current_instruction += 2
            case 1:
                B = B ^ operand_code
                current_instruction += 2
            case 2:
                B = combo_operand % 8
                current_instruction += 2
            case 3:
                if A != 0:
                    if operand_code == current_instruction:
                        current_instruction = 99999
                    else:
                        current_instruction = operand_code
                else:
                    current_instruction += 2
            case 4:
                B = B ^ C
                current_instruction += 2
            case 5:
                output.append(combo_operand % 8)
                current_instruction += 2
            case 6:
                B = A // (2 ** combo_operand)
                current_instruction += 2
            case 7:
                C = A // (2 ** combo_operand)
                current_instruction += 2
            case _:
                current_instruction = 99999999

    return A, B, C, current_instruction, output

def test_a(A, B=0, C=0):
    output, current_instruction = [], 0

    while 0 <= current_instruction < len(program):
        A, B, C, current_instruction, output = next_state(A, B, C, current_instruction, output)

        if len(output) > max_index_of_sequence_found:
            if output[max_index_of_sequence_found] == program[max_index_of_sequence_found] and str(program[:len(output)]) == str(output):
                print(output, program)
                sequence.append(a)
                return True, a +1, output
            else:
                return False, 0, output

sequence = []




a = 0
max_index_of_sequence_found = 0

while max_index_of_sequence_found < len(program)-1:
    print(a, max_index_of_sequence_found, end="\r")

    if test_a(a) == None:
        a += 1
        continue

    found_correct_a, new_a, output = test_a(a)

    if found_correct_a:
        print(a, max_index_of_sequence_found)
        print(output)
        max_index_of_sequence_found += 1
        a = new_a

    a += 1