current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")

# Note: I added # to the input files
rules, orderings = f.read().split("#")
rules = [tuple(int(x) for x in line.split("|")) for line in rules.split("\n")[:-1]]
orderings = [[int(x) for x in line.split(",")] for line in orderings.split("\n")[1:-1]]

rules_dict = dict()
for rule in rules:
    rules_dict[rule[0]] = rules_dict.get(rule[0], set())
    rules_dict[rule[0]].add(rule[1])

def check_ordering(order):
    for i, item in enumerate(order):
        if not item in rules_dict:
            continue

        if any([x in rules_dict[item] for x in order[:i]]):
            return False
    return True

solution1 = 0
incorrect_orderings = []
for order in orderings:
    if check_ordering(order):
        solution1 += order[len(order)//2]
    else:
        incorrect_orderings.append(order)


result2 = 0
for order in incorrect_orderings:
    visited = set()
    result = []

    def dfs(node, ordering):
        if node in visited:
            return
        
        visited.add(node)

        for child in rules_dict.get(node, []):
            if child in ordering:
                dfs(child, ordering)

        result.append(node)

    for node in order:
        dfs(node, order)

    result2 += result[len(result)//2]

print(result2)


