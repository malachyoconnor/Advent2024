current_dir = "/".join(__file__.split("\\")[:-1])
f = open(f"{current_dir}/input.txt", "r")

stones = [int(num) for l in f.read().split("\n")[:-1] for num in l.split(" ")]

# Rules:
# 0       -> 1
# abcd    -> ab cd [Note: Leading zeroes dropped ]
# ELSE: x -> x * 2024

memo = {}

def count_result(stone, iterations):
    if iterations == 0:
        return 1
    
    if (stone, iterations) in memo:
        return memo[(stone, iterations)]
    
    result_list = []
    if stone == 0:
        result_list.append(1)

    elif len(str(stone)) % 2 == 0:
        result_list.append(int(str(stone)[:len(str(stone))//2]))
        result_list.append(int(str(stone)[len(str(stone))//2:]))

    else:
        result_list.append(stone * 2024)


    result = sum([count_result(result_stone, iterations-1) for result_stone in result_list])
    memo[(stone, iterations)] = result
    return result


solution1, solution2 = 0, 0

for stone in stones:
    solution1 += count_result(stone, 25)
    solution2 += count_result(stone, 75)

print(f"Solution 1 {solution1}")
print(f"Solution 2 {solution2}")