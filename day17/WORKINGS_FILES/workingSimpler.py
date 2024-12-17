current_dir = "/".join(__file__.split("\\")[:-1])
data = open(f"{current_dir}/input.txt", "r").readlines()
program = [int(x) for x in data[-1].split(": ")[1].split(",")]

def next_state(A, B, current_instruction, output):
    B = ((3-A)%8) ^ (A // (2 ** ((A % 8) ^ 5)))
    A = A // 8

    output.append(B%8)
    
    return A, B, output

def test_a(A, B=0):
    output, current_instruction = [], 0

    # B = ((3-A)%8) ^ (A // (2 ** ((A % 8) ^ 5)))
    # A = A // 8
    if A >> (3 * max_index_of_sequence_found) == 0:
        return False, 0, None

    while True:
        A, B, output = next_state(A, B, current_instruction, output)

        if len(output) > max_index_of_sequence_found:
            if output[max_index_of_sequence_found] == program[max_index_of_sequence_found] and str(program[:len(output)]) == str(output):
                sequence.append(a)
                return True, A, output
            else:
                return False, 0, output

sequence = []

a = 281474976710656
max_index_of_sequence_found = 0
sequence = []

while max_index_of_sequence_found < len(program)-1:
    print(a, max_index_of_sequence_found, end="\r")

    if test_a(a) == None:
        a += 9
        continue

    found_correct_a, new_a, output = test_a(a)

    if found_correct_a:
        print(a, max_index_of_sequence_found)
        print(output)
        max_index_of_sequence_found += 1

    a += 9