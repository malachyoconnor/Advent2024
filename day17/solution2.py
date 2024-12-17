
# Mangling of the original program to find patterns in it
def next_state(A, B, output):
    B = ((3-A)%8) ^ (A // (2 ** ((A % 8) ^ 5)))
    A = A // 8

    output.append(B%8)
    
    return A, B, output

def check_if_a_works(A, B=0):
    output = []

    # Once for A=0 (;
    A, B, output = next_state(A, B, output)
    while A > 0:
        A, B, output = next_state(A, B, output)
        
    if len(output) > len(real_program):
        return False, 0, output
            
    for x,y in zip(output, real_program[len(real_program) - len(output):]):
        if x != y:
            return False, 0, output

    return True, A, output
                        

real_program = [2, 4, 1, 5, 7, 5, 0, 3, 4, 0, 1, 6, 5, 5, 3, 0]
a = -1
while True:
    a+=1
    worked, _, output = check_if_a_works(a)

    if worked:
        if len(output) == len(real_program):
            print(output)
            print(f"{a} I DID IT")
            exit()

        # We can SHIFT the output right by one by multiplying by 8!
        # Based on next_state analysis - A always divides by 8 - so A * 8 is going to be the smallest
        # items with all the items shifted to the left (As A//8 will then produce us our output again!)
        a = a*8 - 1

    print(a, end="\r", flush=False)