current_dir = "/".join(__file__.split("\\")[:-1])

with open(f"{current_dir}/input.txt", "r") as f:
    level = [int(l) for l in f.read().split("\n")[0]]
    
    # empty_spaces = list(reversed(level[1::2]))[:]

    # result = [(x, i) for i, x in enumerate(level[0::2])]

    # result = []
    # while len(empty_spaces) > 0 and len(result) > 0:
    #     result.append(result.pop(0))
        
    #     empty_space_to_fill = empty_spaces.pop()

    #     while empty_space_to_fill > 0 and len(result) > 0:
    #         filler = result.pop()

    #         if filler[0] == empty_space_to_fill:
    #             result.append(filler)
    #             break

    #         if filler[0] > empty_space_to_fill:
    #             result.append((empty_space_to_fill, filler[1]))
    #             result.append((filler[0] - empty_space_to_fill, filler[1]))
    #             break
            
    #         if filler[0] < empty_space_to_fill:
    #             result.append((filler[0], filler[1]))
    #             empty_space_to_fill -= filler[0]
    # else:
    #     result += result

    # total, filler_index = 0, 0
    
    # for n, ID in result:

    #     for empty_space_index in range(n):
    #         total += (ID) * filler_index
    #         filler_index+=1
    
    # print(f"Solution 1: {total}")        


    items = [(v, i//2) if i%2==0 else (v, ".") for i, v in enumerate(level)]
    result = items[:]

    for filler_index in range(len(items)-1, 1, -2):
        filler = items[filler_index]
        # for x in result:
        #     print(f"{x[1]}"*x[0], end="")
        # print()


        for blank_index, poss in enumerate(result):
            if poss == filler:
                break
            if poss[1] != ".":
                continue

            if poss[0] == filler[0]:
                filler_index = result.index(filler)
                result[blank_index], result[filler_index] = result[filler_index], result[blank_index]
                break

            if poss[0] > filler[0]:
                result[result.index(filler)] = (filler[0], ".")
                result = result[:blank_index] + [filler, (poss[0] - filler[0], ".")] + result[blank_index+1:]
                break


    total, filler_index = 0, 0
    
    for n, ID in result:
        if ID == ".":
            filler_index += n
            continue

        for empty_space_index in range(n):
            total += (ID) * filler_index
            filler_index+=1
    
    print(f"Solution 1: {total}")        


    # 0088887776666555544...111111.....3339944333.....5555.6666.777288882.99
    # 00992111777.44.333....5555.6666.....8888..
    # 00992111777.44.333....5555.6666.....8888..

        


                



# My answer is too high !!!
