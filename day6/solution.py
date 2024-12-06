current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")

level = [list(l) for l in f.read().split("\n")[:-1]]

# Assume a square
MAP_SIZE = len(level)

start_location = ()
obstacle_exists_here = [[False]*len(x) for x in level]

for y in range(len(level)):
    for x in range(len(level)):
        if level[y][x] == "^":
            start_location = (y, x)
        obstacle_exists_here[y][x] = level[y][x] == "#"

# ^ > v <
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
CURRENT_DIRECTION = 0
visited = set()

def step(guard_location):
    global CURRENT_DIRECTION
    dy, dx = directions[CURRENT_DIRECTION]

    # We're still in the map
    while (0 <= guard_location[0] + dy < MAP_SIZE) and (0 <= guard_location[1] + dx < MAP_SIZE):
        if obstacle_exists_here[guard_location[0] + dy][guard_location[1] + dx]:
            CURRENT_DIRECTION = (CURRENT_DIRECTION+1)%4
            dy, dx = directions[CURRENT_DIRECTION]
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

    if obstacle_exists_here[y][x]:
        continue
    
    CURRENT_DIRECTION = 0
    obstacle_exists_here[y][x] = True
    pos_and_dir = set()
    location = start_location

    while location != None:
        pos_and_dir.add((location, directions[CURRENT_DIRECTION])) 
        location = step(location)

        if (location, directions[CURRENT_DIRECTION]) in pos_and_dir: 
            # We've found a loop!
            loop_locations += 1
            break

    obstacle_exists_here[y][x] = False

print(f"\nSolution 2: {loop_locations}")

