current_dir = "/".join(__file__.split("\\")[:-1])
real_map = open(f"{current_dir}/input.txt", "r").read().split("\n")[:-1]
real_map = [list(x) for x in real_map]


def calc_dist_to_empty(y, x, map, cost_to_get_here, normal_distance, distance_from_end: dict):
    count = 0
    ends = set()
    for dy in range(-20, 20+1):
        for dx in range(-20, 20 + 1):
            if ( not (0 <= y + dy < len(map) and 0 <= x + dx < len(map[y+dy])) or 
                 dy == dx == 0 or map[y + dy][x + dx] == "#" or 
                #  distance_from_end[(y+dy, x+dx)] == 0 or
                 abs(dy) + abs(dx) > 20):
                continue
            
            total_distance = distance_from_end[(y + dy, x + dx)] + cost_to_get_here + abs(dy) + abs(dx)

            if total_distance + 100 <= normal_distance:
                ends.add((y+dy, x+dx))
                count += 1

    return ends

end_tile = None
for y in range(len(real_map)):
    for x in range(len(real_map[y])):
        if real_map[y][x] == "E":
            end_tile = (y,x)
            break

prev, path = None, [(*end_tile, 0)]

while real_map[path[-1][0]][path[-1][1]] != "S":
    y,x, distance = path[-1]

    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if (not (0 <= y + dy < len(real_map) and 0 <= x + dx < len(real_map[y]))
            or (y+dy, x+dx) == prev or real_map[y+dy][x+dx] == "#"):
            continue
        
        prev = (y, x)
        path.append((y + dy, x + dx, distance + 1))
        break


distance_from_end = {(y, x): distance for y,x,distance in path}
normal_distance = path[-1][2]


solutions = set()
for y, x, distance in path:
    ends = calc_dist_to_empty(y, x, real_map, normal_distance-distance, normal_distance, distance_from_end)

    for end in ends:
        solutions.add(((y,x), end))

print(len(solutions))


# 285