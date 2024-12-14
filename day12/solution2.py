from collections import deque

current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")
map = [list(l) for l in f.read().split("\n")[:-1]]


def get_sides(region: set[tuple[int, int]]) -> int:
    sides, possible_corners = 0, set()
    
    directions = ((0.5, -0.5), (0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5))
    for node in region:
        ny, nx = node
        for dy, dx in directions:
            corner = (ny + dy, nx + dx)
            possible_corners.add(corner)

    for corner in possible_corners:
        cy, cx = corner
        adj_cells = [(cy + dy, cx + dx) in region for dy, dx in directions]
        n_adj = sum(adj_cells)
        
        # We're a corner of an edge - if we're diagonal to 3 nodes - We're in the middle of an L
        # And we're a corner!
        if n_adj == 1 or n_adj == 3:
            sides += 1

        # If we're the meeting point of two different parts of our region diagonally
        # We're two corners!
        elif adj_cells == [True, False, True, False] or adj_cells == [False, True, False, True]:
            sides += 2
    return sides


def find_region(y, x, input_map, name, explored):
    if (y,x) in explored:
        return set()
    
    if input_map[y][x] != name:
        return set()

    explored.add((y,x))

    result = set([(y,x)])
    if input_map[y][x] == name:
        for exp_y, exp_x in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
            if 0 <= exp_y < len(input_map) and 0 <= exp_x < len(input_map[0]):
                result = result.union(find_region(exp_y, exp_x, input_map, name, explored))

    return result


visited = set()
res = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if (y,x) not in visited:
            region = find_region(y, x, map, map[y][x], visited)
            res += get_sides(region) * len(region)
            
print(res)