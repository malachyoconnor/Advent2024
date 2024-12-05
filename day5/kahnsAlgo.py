from typing import Iterable, TypeVar, Optional

# This solution is more of a method of remembering Kahn's algorithm - it's not efficient, especially part 1.

current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")

# Note: I added # to the input files
rules, orderings = f.read().split("#")
rules = [tuple(int(x) for x in line.split("|")) for line in rules.split("\n")[:-1]]
orderings = [[int(x) for x in line.split(",")] for line in orderings.split("\n")[1:-1]]

# Before -> After
graph: dict[int, set[int]] = dict()
T = TypeVar("T")

# Very space inefficient queue (:
class Queue[T]:
    def __init__(self, initializer: Iterable[T]) -> None:
        self.head: int = 0
        self.tail: int = 0
        self.queue: list[T] = []
        
        for node in initializer:
            self.put(node)

    def put(self, val: T) -> None:
        self.tail += 1
        self.queue.append(val)

    def get(self) -> Optional[T]:
        if self.head == self.tail:
            return None
        self.head += 1
        return self.queue[self.head - 1]
    
    def len(self) -> int:
        return self.tail - self.head

for rule in rules:
    graph[rule[0]] = graph.get(rule[0], set())
    graph[rule[0]].add(rule[1])

def solve(order: list[int]):
    all_nodes = set(order)
    pointed_at_count: dict[int, int] = dict()

    for node in all_nodes:
        all_nodes_we_point_to = all_nodes.intersection(graph.get(node, {}))

        for pointed_at_node in all_nodes_we_point_to:
            pointed_at_count[pointed_at_node] = pointed_at_count.get(pointed_at_node, 0) + 1

    lonesome_nodes = all_nodes - set(pointed_at_count.keys())
    queue = Queue(lonesome_nodes)
    result = []

    while queue.len() != 0:
        node = queue.get()

        result.append(node)

        pointed_at_nodes = all_nodes.intersection(graph.get(node, {}))

        for pointing_at in pointed_at_nodes:
            pointed_at_count[pointing_at] -= 1
            if pointed_at_count[pointing_at] == 0:
                queue.put(pointing_at)

    return result

solution1, solution2 = 0, 0

for order in orderings:
    correct_order = solve(order)
    if all([order[i] == correct_order[i] for i in range(len(order))]):
        solution1 += order[len(order)//2]
    else:
        solution2 += correct_order[len(correct_order)//2]

print(f"Solution 1: {solution1}")
print(f"Solution 2: {solution2}")


