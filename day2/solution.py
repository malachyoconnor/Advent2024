import os

current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")

all_levels = [list(int(a) for a in l.split(" ")) 
                for l in f.read().split("\n")[:-1]]

safe = 0

# solution 1
# for level in all_levels:
#     diffs = [(next - curr) for curr, next in zip(level, level[1:])]

#     if not all([1 <= abs(x) <= 3 for x in diffs]):
#         continue
#     if not all([(x>=0) == (diffs[0] >= 0) for x in diffs]):
#         continue

#     safe += 1

# print(safe)

# solution 2

def is_safe(level):
    diffs = [(next - curr) for curr, next in zip(level, level[1:])]

    if not all([1 <= abs(x) <= 3 for x in diffs]):
        return False
    
    if not all([(diffs[0]>=0) == (x>=0) for x in diffs]):
        return False

    return True


safe2 = 0

for level in all_levels:
    
    if is_safe(level):
        safe2 += 1
        continue
    
    for index in range(len(level)):
        if is_safe(level[:index] + level[index+1:]):
            safe2 += 1
            break

print(safe2)