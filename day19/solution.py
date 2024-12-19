current_dir = "/".join(__file__.split("\\")[:-1])
data = open(f"{current_dir}/input.txt", "r").read().split("\n")[:-1]

towels = data[0].split(", ")
desired_patterns = data[2:]

starts_with = dict()
for ingr in towels:
    starts_with[ingr[0]] = starts_with.get(ingr[0], set())
    starts_with[ingr[0]].add(ingr[1:])

counted_ways = dict()

def count_ways(finding):
    if len(finding) == 0:
        return 1
    if finding in counted_ways:
        return counted_ways[finding]
    
    head, tail, ways = finding[0], finding[1:], 0

    if head not in starts_with:
        return 0

    if '' in starts_with[head]:
        ways += count_ways(tail)

    for possible_tail in sorted(starts_with[head], reverse=True, key=lambda x: len(x)):
        if possible_tail == '':
            continue
        
        if tail.startswith(possible_tail):
            ways += count_ways(tail[len(possible_tail):])

    if finding not in counted_ways:
        counted_ways[finding] = ways
    return ways
    

print(f"Part 1: {sum([count_ways(pattern)>0 for pattern in desired_patterns])}")
print(f"Part 2: {sum([count_ways(pattern) for pattern in desired_patterns])}")
