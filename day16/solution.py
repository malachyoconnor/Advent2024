import heapq, math

current_dir = "/".join(__file__.split("\\")[:-1])
map = open(f"{current_dir}/input.txt", "r").read().split("\n")[:-1]
map = [list(x) for x in map]

def dijkstra(map, start_y, start_x):
    queue = [(0, start_y, start_x, 1, [])]
    visited_scores, best_paths_visited = dict(), []
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    max_score = math.inf

    while len(queue) != 0:
        score, y, x, current_dir, path = heapq.heappop(queue)
        
        if visited_scores.get((y,x,current_dir), math.inf) < score:
            continue

        if score > max_score:
            return score, best_paths_visited

        visited_scores[(y,x,current_dir)] = score

        if map[y][x] == "E":
            max_score = score
            best_paths_visited.append(path)
            continue

        dy, dx = directions[current_dir]

        for new_dir, cost in zip([current_dir, (current_dir+1)%4, (current_dir-1)%4, (current_dir+3)%4], [0, 1000, 1000, 2000]):
            if ((0 <= y + dy < len(map) and 0 <= x + dx < len(map[y])) and map[y+dy][x+dx] != "#" and 
                visited_scores.get((y + dy ,x + dx, new_dir), math.inf) > score + cost + 1):
                heapq.heappush(queue, (score+cost+1, y+dy, x+dx, new_dir, path + [(y,x)]))

    return 0


for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "S":
            result, paths = dijkstra(map, y, x)

            best_paths_visited_nodes = set()
            for path in paths:
                for location in path:
                    best_paths_visited_nodes.add(location)

            for vis_y,vis_x in best_paths_visited_nodes:
                map[vis_y][vis_x] = "O"
            
            for y_ in range(len(map)):
                for x_ in range(len(map[y_])):
                    if map[y_][x_] == '#':
                        map[y_][x_] = '█'
                    elif map[y_][x_] == '.':
                        map[y_][x_] = ' '

            for c in map:
                print("".join(c))
            print()


            print(f"Part 1 answer: {result}")
            print(f"Part 2 answer: {len(best_paths_visited_nodes)}")
            exit()