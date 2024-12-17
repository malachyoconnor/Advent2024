current_dir = "/".join(__file__.split("\\")[:-1])
data = open(f"{current_dir}/input.txt", "r").readlines()

A, B, C = [int(x.split(": ")[1].split("\n")[0]) for x in data[:3]]
program = [int(x) for x in data[-1].split(": ")[1].split(",")]

def get_combo_operand(operand_code):
    if 0 <= operand_code <= 3:
        return operand_code
    if operand_code == 4:
        return "A"
    if operand_code == 5:
        return "B"
    if operand_code == 6:
        return "C"
    if operand_code == 7:
        return "assert 0 == 1"
    assert 0 == 1

def get_operation(opcode, operand_code, current_instr):
    combo_operand = get_combo_operand(operand_code)
    if opcode == 0:
        return f"A = A // (2 ** {combo_operand})", current_instr + 2
    if opcode == 1:
        return f"B = B ^ {operand_code}", current_instr + 2
    if opcode == 2:
        return f"B = {combo_operand} % 8", current_instr + 2
    if opcode == 3:
        if A != 0:
            return "", operand_code
    if opcode == 4:
        return f"B = B ^ C", current_instr + 2
    if opcode == 5:
        return f"output += str({combo_operand} % 8) + ','", current_instr + 2
    if opcode == 6:
        return f"B = A // (2 ** {combo_operand})", current_instr + 2
    if opcode == 7:
        return f"C = A // (2 ** {combo_operand})", current_instr + 2
    
    
    return "", 99999

program_string = "".join([str(x)+"," for x in program])
init_A, init_B, init_C = [int(x.split(": ")[1].split("\n")[0]) for x in data[:3]]

for a in range(117441):
    A, B, C = a, init_B, init_C
    output = ""

    current_instruction = 0
    while 0 <= current_instruction < len(program):

        opcode, operand_code = program[current_instruction], program[current_instruction+1]

        to_exec, current_instruction = get_operation(opcode, operand_code, current_instruction)

        exec(to_exec)

    else:
        if output == program_string:
            print(a)
else:
    print(output)
# 4,2,5,6,7,7,7,7,3,1,0
# 4,2,5,6,7,7,7,7,3,1,0