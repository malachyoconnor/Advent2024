import heapq

current_dir = "/".join(__file__.split("\\")[:-1])
map = open(f"{current_dir}/input.txt", "r").read().split("\n")[:-1]

# class PriorityQueue:


def dijkstra(map, start_y, start_x):
    queue = [(0, start_y, start_x, 1, [])]
    visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while len(queue) != 0:
        score, y, x, current_dir, path = heapq.heappop(queue)
        
        if map[y][x] == "E":
            print(score)
            continue

        if (y, x, current_dir) in visited:
            continue

        visited.add((y, x, current_dir))
        
        dy, dx = directions[current_dir]
        if (0 <= y + dy < len(map) and 0 <= x + dx < len(map[y])) and map[y+dy][x+dx] != "#" and (y + dy, x + dx, current_dir) not in visited:
            heapq.heappush(queue, (score+1, y+dy, x+dx, current_dir, path + [(y+dy, x+dx)]))

        for new_dir, cost in zip([current_dir, (current_dir+1)%4, (current_dir-1)%4, (current_dir+3)%4], [0, 1000, 1000, 2000]):
            # Standing still and turning
            if (y, x, new_dir) not in visited:
                heapq.heappush(queue, (score+cost, y, x, new_dir, path + [(y, x)]))

    return 0

for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "S":
            result = dijkstra(map, y, x)
            print(result)
            exit()
