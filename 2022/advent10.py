with open('./advent10.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

# part 1

queue = []
cycle = 0
x = 1
results = []
for instruction in content:
    cycle += 1

    if instruction.startswith("addx"):
        value = instruction.split(" ")[1]
        queue.extend([0, int(value)])
    else:
        queue.append(0)

    if cycle in [20, 60, 100, 140, 180, 220]:
        results.append(x * cycle)

    x += queue.pop(0)


for q in queue:
    cycle += 1

    if instruction.startswith("addx"):
        value = instruction.split(" ")[1]
        queue.extend([0, int(value)])
    else:
        queue.append(0)

    if cycle in [20, 60, 100, 140, 180, 220]:
        results.append(x * cycle)

    x += queue.pop(0)

print(sum(results))

# Part 2

queue = []
cycle = 0
row = 0
x = 1
results = [[], [], [], [], [], []]
for instruction in content:
    cycle += 1

    if instruction.startswith("addx"):
        value = instruction.split(" ")[1]
        queue.extend([0, int(value)])
    else:
        queue.append(0)

    if (cycle-1) in [x - 1, x, x + 1]:
        results[row].append("#")
    else:
        results[row].append(".")
    if cycle == 40:
        cycle = 0
        row += 1
    
    x += queue.pop(0)

for q in queue:
    cycle += 1

    if instruction.startswith("addx"):
        value = instruction.split(" ")[1]
        queue.extend([0, int(value)])
    else:
        queue.append(0)

    if (cycle-1) in [x - 1, x, x + 1]:
        results[row].append("#")
    else:
        results[row].append(".")
    if cycle == 40:
        cycle = 0
        row += 1

    x += queue.pop(0)

for row in results:
    print("".join(row))