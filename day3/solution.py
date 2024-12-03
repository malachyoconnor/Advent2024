import re

current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")

all_lines = "#".join([l for l in f.read().split("\n")[:-1]])

def evaluate_script(regex: str) -> int:
    matches = re.findall(regex, all_lines)
    total, do = 0, True

    for match in matches:
        if len(match) > 2 and match[2] == 'do()':
            do = True
        if len(match) > 2 and match[3] == "don't()":
            do = False
        if do and match[0] != '':
            total += int(match[0]) * int(match[1])

    return total


print("Solution 1:", evaluate_script(r'mul\(([0-9]+)\,([0-9]+)\)'))
print("Solution 2:", evaluate_script(r'mul\(([0-9]+)\,([0-9]+)\)|(do\(\))|(don\'t\(\))'))
