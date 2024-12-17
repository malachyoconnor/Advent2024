current_dir = "/".join(__file__.split("\\")[:-1])
data = open(f"{current_dir}/input.txt", "r").readlines()

A, B, C = [int(x.split(": ")[1].split("\n")[0]) for x in data[:3]]
program = [int(x) for x in data[-1].split(": ")[1].split(",")]

A = 109019476330651

def get_combo_operand(operand_code):
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

output = []
current_instruction = 0
sequence = []

while 0 <= current_instruction < len(program):
    opcode, operand_code = program[current_instruction], program[current_instruction+1]
    combo_operand = get_combo_operand(operand_code)

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
            sequence.append((A,B, combo_operand % 8))
            current_instruction += 2
        case 6:
            B = A // (2 ** combo_operand)
            current_instruction += 2
        case 7:
            C = A // (2 ** combo_operand)
            current_instruction += 2
        case _:
            current_instruction = 99999999

print(output)
