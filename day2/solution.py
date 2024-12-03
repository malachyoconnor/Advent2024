current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")

all_levels = [list(int(a) for a in l.split(" ")) 
                for l in f.read().split("\n")[:-1]]

def is_safe(level):
    diffs = [(next - curr) for curr, next in zip(level, level[1:])]

    if not all([1 <= abs(x) <= 3 for x in diffs]):
        return False
    
    if not all([(diffs[0]>=0) == (x>=0) for x in diffs]):
        return False

    return True

solution1, solution2 = 0,0

# solution 1
for level in all_levels:
    if is_safe(level):
        solution1 += 1

# solution 2
for level in all_levels:
    
    if is_safe(level):
        solution2 += 1
        continue
    
    for index in range(len(level)):
        if is_safe(level[:index] + level[index+1:]):
            solution2 += 1
            break

print("Solution 1:", solution1)
print("Solution 2:", solution2)