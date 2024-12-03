import re

current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")

all_lines = [l for l in f.read().split("\n")[:-1]]


# FIRST SOLUTION
# matches = []
# for line in all_lines:
#     matches += re.findall(r'(mul\(([0-9]+)\,([0-9]+)\))', line)

# total = 0

# for match in matches:
#     total += int(match[0]) * int(match[1])

# print(total)


matches = []
for line in all_lines:
    matches += re.findall(r'(mul\(([0-9]+)\,([0-9]+)\))|(do\(\))|(don\'t\(\))', line)

total, do = 0, True
do = True

for match in matches:
    if match[3] == 'do()':
        do = True
        continue
    if match[4] == "don't()":
        do = False
        continue

    if do:
        total += int(match[1]) * int(match[2])

print(total)

