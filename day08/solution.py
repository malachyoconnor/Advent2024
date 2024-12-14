import numpy as np

# This solution is inefficient - the main problem for speed being the creation of numpy arrays for single loop iterations
# To solve this - I should write a little cheap, hashable vector class

current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/small_input.txt", "r")

levels = [list(l) for l in f.read().split("\n")[:-1]]
MAP_SIZE = len(levels)

obstacles = {}

for y, level in enumerate(levels):
    for x, item in enumerate(level):
        if item != '.':
            obstacles[item] = obstacles.get(item, set())
            obstacles.get(item, set()).add((y,x))

poss_locations = 0

for y in range(MAP_SIZE):
    for x in range(MAP_SIZE):
        loc = np.array([y,x])
        for obstacle_locations in obstacles.values():

            for obstacle_location in obstacle_locations:
                result  = tuple(loc - (2 * (loc - np.array(obstacle_location))))

                if (result in obstacle_locations) and levels[y][x] != '#' and (y,x) != obstacle_location:
                    levels[y][x] = '#'
                    poss_locations += 1

print(f"Solution 1: {poss_locations}")

for obstacle_locations in obstacles.values():

    for ob1 in obstacle_locations:
        ob1 = np.array(ob1)
        for ob2 in obstacle_locations:
            ob2 = np.array(ob2)
            diff = ob2 - ob1

            for N in range(-MAP_SIZE, MAP_SIZE):
                test = diff * N + ob1
                if all(np.array([0,0]) <= test) and all(test < np.array([MAP_SIZE, MAP_SIZE])) and levels[test[0]][test[1]] != '#':
                    levels[test[0]][test[1]] = '#'
                    poss_locations += 1


print(f"Solution 2: {poss_locations}")
               
