with open('./day5.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

# Part 1

seeds = content[0].split(": ")[1].split(" ")

def define_lowest(seeds):
    i = -1
    maps = []
    next_line = []
    for line in content[2:]:
        if "map" in line:
            if i != -1:
                maps.append(next_line)
            i += 1
            next_line = []
        else:
            if line != "":
                next_line.append(line)
    maps.append(next_line)

    mapped_list = []
    for line in maps:
        mapped = []
        for instruction in line:
            dest = instruction.split(" ")[0]
            source = instruction.split(" ")[1]
            lenght = instruction.split(" ")[2]
            mapped.append(( (int(source), int(source)+int(lenght)-1), (int(dest), int(dest)+int(lenght)-1) ))
        mapped_list.append(mapped)

    results = {}
    for seed in seeds:
        results[int(seed)] = []

    supposed_lenght = 1
    for map in mapped_list:
        for instruction in map:
            sources = instruction[0]
            dest = instruction[1]
            for seed in seeds:
                if supposed_lenght != len(results[int(seed)]):
                    if results[int(seed)] != []:
                        if results[int(seed)][-1] >= int(sources[0]) and results[int(seed)][-1] <= int(sources[1]):
                            results[int(seed)].append(results[int(seed)][-1] - sources[0] + dest[0])
                    else:
                        if int(seed) >= int(sources[0]) and int(seed) <= int(sources[1]):
                            results[int(seed)].append(int(seed) - sources[0] + dest[0])
        for seed in seeds:
            if supposed_lenght > len(results[int(seed)]):
                if results[int(seed)] == []:
                    results[int(seed)].append(int(seed))
                else:
                    results[int(seed)].append(results[int(seed)][-1])
        supposed_lenght += 1

    return min([result[-1] for result in results.values()])

print(define_lowest(seeds))

# Part 2

seeds_range = content[0].split(": ")[1].split(" ")
seeds = []

for j in range(0, len(seeds_range), 2):
    seeds.append(int(seeds_range[j]))
    seeds.append(int(seeds_range[j]) + int(seeds_range[j+1]) - 1)

print(seeds)
print(define_lowest(seeds))