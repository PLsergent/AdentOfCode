with open('./day9.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

# Part 1

sum = 0
for line in content:
    steps = []
    l = 1
    line = line.split(" ")
    steps.append([int(x) for x in line])
    while True:
        prev_value = None
        for i in line:
            if prev_value == None:
                steps.append([])
            else:
                steps[l].append(int(i) - int(prev_value))
            prev_value = i
        if len(steps[l]) == steps[l].count(0):
            break
        else:
            line = steps[l]
        l += 1

    steps.reverse()
    next = 0
    for j in steps:
        if j[-1] == 0:
            next = 0
        else:
            next = j[-1] + next
    sum += next

print(sum)

# Part 2
sum = 0
for line in content:
    steps = []
    l = 1
    line = line.split(" ")
    steps.append([int(x) for x in line])
    while True:
        prev_value = None
        for i in line:
            if prev_value == None:
                steps.append([])
            else:
                steps[l].append(int(i) - int(prev_value))
            prev_value = i
        if len(steps[l]) == steps[l].count(0):
            break
        else:
            line = steps[l]
        l += 1

    steps.reverse()
    next = 0
    ind = 0
    for j in steps:
        if ind == 0:
            next = 0
        else:
            next = j[0] - next
        ind += 1
    sum += next

print(sum)