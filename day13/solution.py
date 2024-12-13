import numpy as np
current_dir = "/".join(__file__.split("\\")[:-1])
data = open(f"{current_dir}/input.txt", "r").read().split("\n")[:-1]

questions = [[]]
for d in data:
    if d == '':
        questions.append([])
    else:
        X = int(d.split("X")[1].split(",")[0][1:])
        Y = int(d.split("Y")[1][1:])
        questions[-1].append((X, Y))

def eq_solv(A, B, solution):
    A1, A2 = A
    B1, B2 = B
    S1, S2 = solution

    top = A1 * S2 - A2 * S1
    bottom = A1 * B2 - A2 * B1

    if top % bottom == 0:
        b = top // bottom
        A1a = S1 - B1 * b
        if A1a % A1 == 0:
            a = A1a // A1
            if b == 0:
                return a
            return a*3 + b
            
    return -1


solution1, solution2 = 0, 0
for A, B, destination in questions:
    cost = eq_solv(A, B, destination)
    if cost != -1:
        solution1 += cost
    
    cost = eq_solv(A, B, (destination[0] + 10000000000000, destination[1] + 10000000000000))
    if cost != -1:
        solution2 += cost


print(solution1, solution2)