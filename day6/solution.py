current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")

level = [list(l) for l in f.read().split("\n")[:-1]]

# Assume a square
MAP_SIZE = len(level)

start_location = ()
obstacles = set()
for y in range(len(level)):
    for x in range(len(level)):
        if level[y][x] == "^":
            start_location = (y, x)
        elif level[y][x] == "#":
            obstacles.add((y,x))

# ^ > v <
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set()

def step(guard_location):
    dy, dx = directions[0]

    # We've left the map
    while (0 <= guard_location[0] + dy < MAP_SIZE) and (0 <= guard_location[1] + dx < MAP_SIZE):
        
        if (guard_location[0] + dy, guard_location[1] + dx) in obstacles:
            directions.append(directions[0])
            directions.remove(directions[0])
            dy, dx = directions[0]
        else:
            break
    else:
        return None

    return (guard_location[0] + dy, guard_location[1] + dx)
    

# Used in part 2
default_path = set()
location = start_location

while location != None:
    default_path.add(location)
    visited.add(location)
    location = step(location)

print("Solution 1:", len(visited))

loop_locations = 0

for i, (y,x) in enumerate(default_path):
    print(f"\rFinished: {(i)} / {(len(default_path))}", end='')

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if (y,x) in obstacles:
        continue
    
    obstacles.add((y,x))
    pos_and_dir = set()
    location = start_location

    while location != None:
        pos_and_dir.add((location, directions[0]))
        location = step(location)

        if (location, directions[0]) in pos_and_dir:
            # We've found a loop!
            loop_locations += 1
            break

    obstacles.remove((y,x))

print(f"Solution 2: {loop_locations}")


# 4789
# 1304