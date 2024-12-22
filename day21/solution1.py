from functools import cache, lru_cache
import math
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

@lru_cache(maxsize=200_000)
def get_next_position(buttonCombination, y=0, x=2):
    if len(buttonCombination) == 0:
        return "", y, x
    if len(buttonCombination) == 1:
        return get_arrow_key_path_for_single_button(buttonCombination, y, x)
    
    next_power_of_two = 2 ** (len(bin(len(buttonCombination))) - 3)
    
    if next_power_of_two == len(buttonCombination):
        head_path, head_y, head_x = get_next_position(buttonCombination[:next_power_of_two//2], y, x)
        tail_path, tail_y, tail_x = get_next_position(buttonCombination[next_power_of_two//2:], head_y, head_x)
        return head_path + tail_path, tail_y, tail_x


    head_path, head_y, head_x = get_next_position(buttonCombination[:next_power_of_two], y, x)
    tail_path, tail_y, tail_x = get_next_position(buttonCombination[next_power_of_two:], head_y, head_x)
    return head_path + tail_path, tail_y, tail_x


#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
def get_arrow_key_path_for_single_button(button, y, x):
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



code = "379A"
total = 0
for code in codes:

    minPathLen = math.inf
    paths = keypadShortestPath(code)

    for i, path in enumerate(paths):

        x, _, _ = get_next_position(path)
        for j in range(1):
            x, _, _ = get_next_position(x)
            info = get_next_position.cache_info()
            print(info)

        minPathLen = min(minPathLen, len(x))

    total += int(code[:-1]) * minPathLen


print(total)