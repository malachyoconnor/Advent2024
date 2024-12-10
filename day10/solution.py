current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")

map = [[int(num) for num in list(l)] for l in f.read().split("\n")[:-1]]


def count_solutions(input_y, input_x):
    visited = set()
    solutions = set()

    def find_num(y, x, number):
        visited.add((y,x))

        if number > 9:
            return

        if map[y][x] == 9 and number == 9:
            solutions.add((y,x))
            return

        options = [(y+1,x), (y-1,x), (y,x+1), (y,x-1)]

        for option in options:
            if option not in visited and 0 <= option[0] < len(map) and 0 <= option[1] < len(map[0]):
                if map[option[0]][option[1]] == number+1:
                    find_num(option[0], option[1], number+1)

    assert map[input_y][input_x] == 0

    find_num(input_y, input_x, 0)

    return len(solutions)


total_solutions = 0


for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 0:
            total_solutions += count_solutions(y,x)

print(total_solutions)


def count_solutions2(input_y, input_x):
    paths = set()
    solutions: dict[tuple[int,int], set[str]] = dict()

    def find_num(y, x, number, path):
        if path in paths:
            return
        paths.add(path)
        
        if number > 9:
            return

        if map[y][x] == 9 and number == 9:
            solutions[(y,x)] = solutions.get((y,x), set())
            solutions[(y,x)].add(path)
            return

        options = [(y+1,x), (y-1,x), (y,x+1), (y,x-1)]

        for option_index, option in enumerate(options):
            if 0 <= option[0] < len(map) and 0 <= option[1] < len(map[0]):
                if map[option[0]][option[1]] == number+1:
                    find_num(option[0], option[1], number+1, path + str(option_index))

    assert map[input_y][input_x] == 0

    find_num(input_y, input_x, 0, "")

    return sum([len(solution) for solution in solutions.values()])


total_solutions = 0

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 0:
            total_solutions += count_solutions2(y,x)

print(total_solutions)