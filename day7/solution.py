current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")

levels = [[int(num[:-1]) if num[-1] == ":" else int(num) for num in l.split(" ")] for l in f.read().split("\n")[:-1]]

def concatenate(a, b):
    temp = b
    while temp > 0:
        temp //= 10
        a *= 10
    return a + b

def count_possibilities(ls, total=0, i=1):
    if i >= len(ls):
        return total == ls[0]
    if total > ls[0]:
        return False
    
    return count_possibilities(ls, total + ls[i], i+1) \
         + count_possibilities(ls, total * ls[i], i+1) \
         + count_possibilities(ls, concatenate(total, ls[i]), i+1)

solution1, solution2 = 0, 0

for level in levels:
    if count_possibilities(level) > 0:
        solution2 += level[0]

concatenate = lambda x,y: 1000000000000000000000 # We'll discard any solution that involves concatenate (:

for level in levels:
    if count_possibilities(level) > 0:
        solution1 += level[0]