current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")

level = [list(l) 
                for l in f.read().split("\n")[:-1]]

start_location = ()
for y in range(len(level)):
    for x in range(len(level)):
        if level[y][x] == "^":
            start_location = (y, x)

# ^ > v <
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set()

def step(guard_location, input_level):
    dy, dx = directions[0]

    # We've left the map
    while (0 <= guard_location[0] + dy < len(input_level)) and \
          (0 <= guard_location[1] + dx < len(input_level[0])):    
        if input_level[guard_location[0] + dy][guard_location[1] + dx] == "#":
            directions.append(directions[0])
            directions.remove(directions[0])
            dy, dx = directions[0]
        else:
            break
    else:
        return None

    input_level[guard_location[0] + dy][guard_location[1] + dx], input_level[guard_location[0]][guard_location[1]] = input_level[guard_location[0]][guard_location[1]], input_level[guard_location[0] + dy][guard_location[1] + dx]

    return (guard_location[0] + dy, guard_location[1] + dx)
    

location = start_location
while location != None:
    visited.add(location)
    location = step(location, level)
print("Solution 1:", len(visited))

loop_locations = 0

for y in range(len(level)):
    for x in range(len(level)):
        print(f"\rFinished: {(y * len(level[0]) + x)} / {(len(level[0]) * len(level))}", end='')

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        if level[y][x] == "#" or level[y][x] == "#":
            continue

        new_level = [sub_level[:] for sub_level in level]
        new_level[y][x] = "#"
        pos_and_dir = set()
        location = start_location

        while location != None:
            pos_and_dir.add((location, directions[0]))
            location = step(location, new_level)

            if (location, directions[0]) in pos_and_dir:
                # We've found a loop!
                loop_locations += 1
                break

print(f"Solution 2: {loop_locations}")