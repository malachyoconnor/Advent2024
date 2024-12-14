current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")

map = [list(l) for l in f.read().split("\n")[:-1]]

explored = set()

def find_region(y, x, input_map, name):
    if (y,x) in explored:
        return []
    
    if input_map[y][x] != name:
        return []

    explored.add((y,x))

    result = [(y,x)]
    if input_map[y][x] == name:
        for exp_y, exp_x in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
            if 0 <= exp_y < len(input_map) and 0 <= exp_x < len(input_map[0]):
                result += find_region(exp_y, exp_x, input_map, name)

    return result

regions = []
for y in range(len(map)):
    for x in range(len(map[y])):
        if (y,x) not in explored:
            regions.append(find_region(y,x, map, map[y][x]))


def find_perimeter(region: list[tuple[int, int]]):
    region_name, perimeter = map[region[0][0]][region[0][1]], 0

    for y,x in region:
        for exp_y, exp_x in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
            if not (0 <= exp_y < len(map) and 0 <= exp_x < len(map[0])):
                perimeter += 1
            elif map[exp_y][exp_x] != region_name:
                perimeter += 1

    return perimeter

result1 = 0
for region in regions:
    result1 += find_perimeter(region) * len(region)

print(result1)