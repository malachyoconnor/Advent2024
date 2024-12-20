import heapq

current_dir = "/".join(__file__.split("\\")[:-1])
real_map = open(f"{current_dir}/input.txt", "r").read().split("\n")[:-1]
real_map = [list(x) for x in real_map]

def dijkstra(start, end, map, max_time):
    queue = [(0, *start)]
    visited_times = dict()

    while len(queue) != 0:
        time, y, x = heapq.heappop(queue)
        visited_times[(y,x)] = time

        if time > max_time:
            return max_time+1000
        
        if (y,x) == end:
            return time

        
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if not (0 <= y + dy < len(map) and 0 <= x + dx < len(map[y + dy])):
                continue

            previous_time = visited_times.get((y + dy, x + dx), time + 2)

            if map[y+dy][x+dx] != "#" and (time + 1 < previous_time):
                heapq.heappush(queue, (time+1, y+dy, x+dx))
        
    return max_time+1000

start, end = None, None

for y in range(len(real_map)):
    for x, node in enumerate(real_map[y]):

        if node == "S":
            start = (y,x)
        if node == "E":
            end = (y,x)

# Walking = 84

best_time_without_cheating = dijkstra(start, end, real_map, 100000000000000000)
savings = {}

count = 0
for y in range(len(real_map)):
    for x in range(len(real_map[y])):
        print(y, end="\r", flush=False)
        if real_map[y][x] == "#":
            real_map[y][x] = "."
            time = dijkstra(start, end, real_map, best_time_without_cheating - 100)
            if time <= best_time_without_cheating - 100:
                count += 1
            real_map[y][x] = "#"

print(count)
