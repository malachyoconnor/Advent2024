current_dir = "/".join(__file__.split("\\")[:-1])
data = open(f"{current_dir}/input.txt", "r").read().split("\n")[:-1]

map_data, moves = data[:data.index('')], (data[data.index('')+1:])
moves = list("".join(moves))

map, position = [], ()
move_directions = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

# 2 = box, 1 = wall, 0 = nothing
for y, l in enumerate(map_data):
    if '@' in l:
        position = (y, l.index('@')) 
    map.append(list(l))

# For part 2
old_map = [x[:] for x in map]

def move_box(box_y, box_x, direction):
    if map[box_y][box_x] == ".":
        return True
    
    if map[box_y][box_x] == "#":
        return False
    
    if map[box_y][box_x] == "O":
        dy, dx = move_directions[direction]
        if move_box(box_y + dy, box_x + dx, direction):
            map[box_y][box_x], map[box_y+dy][box_x+dx] = map[box_y+dy][box_x+dx], map[box_y][box_x]
            return True
        return False


for move in moves:
    py, px = position
    dy, dx = move_directions[move]
    new_position = (py + dy, px + dx)
    if move_box(*new_position, move):
        position = new_position
        map[py][px], map[py+dy][px+dx] = map[py+dy][px+dx], map[py][px]

result = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == 'O':
            result += 100 * y + x

print(result)

def swap(y1, x1, y2, x2):
    new_map[y1][x1], new_map[y2][x2] = new_map[y2][x2], new_map[y1][x1]

def new_move_box(box_y, box_x, move, do_the_move=True):
    if new_map[box_y][box_x] == ".":
        return True
    
    if new_map[box_y][box_x] == "#":
        return False
    
    if new_map[box_y][box_x] == "]":
        return new_move_box(box_y, box_x-1, move, do_the_move)
    
    dy, dx = move_directions[move]

    my_position = (box_y, box_x)
    my_new_position = (box_y+dy, box_x+dx)
    my_neighours_position = (box_y, box_x+1)
    my_neighours_new_position = (box_y+dy, box_x+1+dx)

    if new_map[box_y][box_x] == "[":
        move_me = new_move_box(*my_new_position, move, False) if my_new_position != my_neighours_position else True
        move_neighbour = new_move_box(box_y+dy, box_x+1+dx, move, False) if my_neighours_new_position != my_position else True
        if (move_me and move_neighbour):
            if do_the_move:                
                if my_neighours_new_position == my_position:
                    new_move_box(*my_new_position, move, True)

                    swap(*my_position, *my_new_position)
                    swap(*my_neighours_position, *my_neighours_new_position)
                elif my_new_position == my_neighours_position:

                    new_move_box(*my_neighours_new_position, move, True)
                    swap(*my_neighours_position, *my_neighours_new_position)
                    swap(*my_position, *my_new_position)

                else:
                    new_move_box(*my_neighours_new_position, move, True)
                    new_move_box(*my_new_position, move, True) 
                    swap(*my_neighours_position, *my_neighours_new_position)
                    swap(*my_position, *my_new_position)

            return True
        
    return False



new_map = []
position = ()

for y, l in enumerate(old_map):
    new_l = []

    for x, item in enumerate(l):
        if item == "#":
            new_l += ["#", "#"]
        elif item == ".":
            new_l += [".", "."]
        elif item == "O":
            new_l += ["[", "]"]
        elif item == "@":
            new_l += ["@", "."]
            position = (y, 2*x)
        else:
            assert 0 == 1

    new_map.append(new_l)

import sys
import time
import os
os.system('')

def clear_lines(n=1):
    for x in range(n):
        print(f"\033[1A", end='\r', file=sys.stdout, flush=True)


for move in moves:
    py, px = position
    dy, dx = move_directions[move]
    new_position = (py + dy, px + dx)

    clear = 0
    
    for l in new_map:
        if "@" in l:
            b = l[:]
            b[b.index("@")] = "\033[31m@\033[0m"
            print("".join(b))
        else:
            print("".join(l))
        clear += 1

    clear_lines(clear)

    time.sleep(0.1)


    if new_move_box(*new_position, move):
        position = new_position
        new_map[py][px], new_map[py+dy][px+dx] = new_map[py+dy][px+dx], new_map[py][px]



result = 0
for y in range(len(new_map)):
    for x in range(len(new_map[y])):
        if new_map[y][x] == '[':
            result += 100 * y + x

print(result)