import sys
from PIL import Image
import numpy as np

current_dir = "/".join(__file__.split("\\")[:-1])
data = open(f"{current_dir}/input.txt", "r").read().split("\n")[:-1]

robots = []
for d in data:
    px, py = [int(p) for p in d.split(" ")[0].split("=")[1].split(",")]
    dx, dy = [int(p) for p in d.split(" ")[1].split("=")[1].split(",")]
    robots.append([(px,py), (dx,dy)])

WIDTH, HEIGHT = 101, 103
N = 100

def simulate(pos, velocity, steps):
    x, y = pos
    dx, dy = velocity
    for _ in range(steps):
        y = (y + dy) % HEIGHT
        x = (x + dx) % WIDTH
    return (x,y)

quadrants = {0: 0, 1: 0, 2:0, 3:0}

for p, v in robots:
    res_x, res_y = simulate(p, v, N)

    if res_x != WIDTH // 2 and res_y != HEIGHT // 2:
        quad = (res_x > WIDTH // 2) * 2 + (res_y > HEIGHT // 2)
        quadrants[quad] += 1

solution1 = 1 * quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    
print(f"Solution 1: {solution1}")

import os

def get_map_and_update(steps):
    map = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for i, (p, v) in enumerate(robots):
        res_x, res_y = simulate(p, v, steps)
        map[res_y][res_x] = 1
        robots[i][0] = (res_x, res_y)

    return map

def display_map(map, steps):
    print(steps)
    print(steps)
    map_copy = [["█" if a == 1 else " " for a in l ] for l in map]

    for l in map_copy:
        print("".join(l))
    
    print(" ".join([str(steps)] * 50))
    print(" ".join([str(steps)] * 50))

def list2d_to_image(pixel_list) -> Image:
    array = np.array(pixel_list) * 255
    return Image.fromarray(array.astype(np.uint8), mode='L')


steps = 0
while True:

    map = get_map_and_update(steps=1)

    img = list2d_to_image(map)
    img.save(f"{current_dir}/images/{(steps+1):08d}.png")

    print(f"{steps}", end="\r", file=sys.stdout, flush=True)

    steps += 1



