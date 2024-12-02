import os

current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")

output_pairs = [tuple(int(a) for a in l.split("   ")) 
                for l in f.read().split("\n")[:-1]]


l1, l2 = map(list, zip(*output_pairs))

# PART 1:
count = 0
for a,b in zip(sorted(l1), sorted(l2)):
    count += max(a,b) - min(a,b)

print(count)

counts = dict()

for v in l2:
    counts[v] = counts.get(v, 0) + 1

similarity = 0
for v in l1:
    similarity += counts.get(v, 0) * v

print(similarity)