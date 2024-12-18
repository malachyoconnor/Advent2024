import heapq

current_dir = "/".join(__file__.split("\\")[:-1])

data = open(f"{current_dir}/input.txt", "r").read().split("\n")[:-1]
SIZE = 71

obstacles = [(int(l.split(",")[0]), int(l.split(",")[1])) for l in data]

def dijkstra(obstacles: set[tuple[int, int]]):
    queue = [(0, (0, 0))]
    heapq.heapify(queue)
    visited = {(0,0): 0}
    directions = [(-1,0), (0,1),(1,0),(0,-1)]

    while len(queue) != 0:
        current_score, (y, x) = heapq.heappop(queue)

        if (y,x) == (SIZE-1, SIZE-1):
            return True, current_score

        for dy, dx in directions:
            if ((y+dy, x + dx) in visited and visited[(y+dy, x+dx)] <= current_score + 1) or (x + dx, y+dy) in obstacles:
                continue

            if not (0 <= y+dy < SIZE and 0 <= x+dx < SIZE):
                continue
            
            heapq.heappush(queue, (current_score+1, (y+dy, x+dx)))
            visited[(y+dy, x+dx)] = current_score + 1
    
    return False, -1


_, score = dijkstra(set(obstacles[:1024]))
print(f"Part 1: {score}")


for i in range(len(obstacles)-1, -1, -1):
    works, _ = dijkstra(set(obstacles[:i]))
    if works:
        print(f"Part 2 solution: {obstacles[i][0]},{obstacles[i][1]}")
        exit()
