from functools import cache, lru_cache
import math
import re
current_dir = "/".join(__file__.split("\\")[:-1])
codes = open(f"{current_dir}/input.txt", "r").read().split("\n")[:-1]

test_code = codes[0]

def get_permutations_of_paths(list_of_paths):
    if len(list_of_paths) == 0:
        return [""]

    result = set()
    for sub_path in list_of_paths[0]:
        for tail_path in get_permutations_of_paths(list_of_paths[1:]):
            result.add(sub_path + tail_path)

    return result

@cache
def get_path_to_button_permutations(path: str):
    if len(path) == 0:
        return set([""])
    if len(path) == 1:
        return set([path])
    
    final_permutations = set()
    sub_perms = get_path_to_button_permutations(path[1:])

    for perm in sub_perms:
        
        for i in range(len(perm)+1):
            final_permutations.add(perm[:i] + path[0] + perm[i:])

    return final_permutations

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

def keypadShortestPath(code, start=(3, 2)):
    subPaths = []
    y, x = start

    button_locations = {
        "7": (0, 0), "8": (0, 1), "9": (0, 2), 
        "4": (1, 0), "5": (1, 1), "6": (1, 2), 
        "1": (2, 0), "2": (2, 1), "3": (2, 2), 
                     "0": (3, 1), "A": (3, 2),
    }
    directions = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1)}

    for button in code:
        y_new, x_new = button_locations[button]
        dy, dx = y_new - y, x_new - x
        base_path = abs(dx) * ("<" if dx < 0 else ">") + abs(dy) * ("^" if dy < 0 else "v")
        all_paths: set[str] = get_path_to_button_permutations(base_path).copy()

        for generated_path in all_paths.copy():
            curr_y, curr_x = y, x
            for step in generated_path:
                curr_y += directions[step][0]
                curr_x += directions[step][1]
                if (curr_y, curr_x) == (3,0):
                    all_paths.remove(generated_path)
            
        all_paths = {x + "A" for x in all_paths}
        subPaths.append(all_paths)
        y, x = y_new, x_new

    return get_permutations_of_paths(subPaths)

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
@cache
def get_arrow_key_path_for_single_button(button, y=0, x=2):
    path = ""
    button_locations = {
                    "^": (0, 1), "A": (0, 2),
        "<" : (1, 0), "v": (1, 1), ">": (1,2)
    }

    y_new, x_new = button_locations[button]
    dy, dx = y_new - y, x_new - x

    if (y, x) == (1, 0):
        path += abs(dx) * ("<" if dx < 0 else ">")
        path += abs(dy) * ("^" if dy < 0 else "v")

    elif (y,x) == (0, 1):
        path += abs(dy) * ("^" if dy < 0 else "v")
        path += abs(dx) * ("<" if dx < 0 else ">")

    elif dy < 0:
        path += abs(dy) * "^"
        path += abs(dx) * ("<" if dx < 0 else ">")

    elif dx > 0:
        path += abs(dx) * ">"
        path += abs(dy) * ("^" if dy < 0 else "v")

    else:
        path += abs(dy) * "v"
        path += abs(dx) * "<"
        
    path += "A"
    return path, y_new, x_new

@cache
def path_is_correct(path, y, x):
    directions = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1), "A": (0,0)}

    for button in path:
        dy, dx = directions[button]
        y, x = y + dy, x + dx

        if (y,x) == (0,0):
            return False

    return True

@cache
def get_best_chunk(button, layers, y, x):
    button_locations = {
                "^": (0, 1), "A": (0, 2),
    "<" : (1, 0), "v": (1, 1), ">": (1,2)
    }

    if layers == 0:
        return button, y, x

    y_new, x_new = button_locations[button]
    dy, dx = y_new - y, x_new - x
    basic_path = abs(dy) * ("^" if dy < 0 else "v") + abs(dx) * ("<" if dx < 0 else ">")

    min_result_path, min_permuted_path = None, None
    for permuted_path in [start + "A" for start in get_path_to_button_permutations(basic_path)]:
        path = ""
        if not path_is_correct(permuted_path, y, x):
            continue
        
        for button in permuted_path + "A":
            print(button, y, x, layers-1)
            sub_path, y, x = get_best_chunk(button, y, x, layers-1)
            path += sub_path

        if min_permuted_path is None or len(path) < len(min_permuted_path):
            min_result_path, min_permuted_path = permuted_path, path

    return min_result_path, y_new, x_new

for layer in range(1, 2):
    print(get_best_chunk("v", layer, 0, 2))

exit()


@cache
def get_next_chunks(chunk):
    assert chunk[-1] == "A"

    y, x = 0, 2
    path = ""
    for button in chunk:
        sub_path, y, x = get_arrow_key_path_for_single_button(button, y, x)
        path += sub_path

    assert (y,x) == (0, 2)
    return path

@cache
def get_total_chunk_cost(chunk, layers):
    assert chunk[-1] == "A"
    assert len(chunk) == 1 or chunk[-2] != "A"

    if layers == 0:
        return len(chunk)
    
    complete_path = get_next_chunks(chunk)
    split_chunks = re.split(r'(?<=A)', complete_path)[:-1]

    total_cost = 0

    for next_chunk in split_chunks:
        sub_cost = get_total_chunk_cost(next_chunk, layers-1)
        total_cost += sub_cost
    
    return total_cost
    

for NUMBER_OF_BOTS in 1, 2, 3:

    total_cost = 0
    for code in codes:
        minPathLen = math.inf
        paths = keypadShortestPath(code)

        for path in paths:
            cost = 0

            for chunk in re.split(r'(?<=A)', path)[:-1]:
                cost += get_total_chunk_cost(chunk, NUMBER_OF_BOTS)

            minPathLen = min(minPathLen, cost)

        total_cost += int(code[:-1]) * minPathLen


    print(total_cost)

