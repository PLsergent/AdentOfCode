with open('./advent5.txt') as f:
    content = f.readlines()

content = [x.replace("[", "*").replace("]", "*").replace(" ", "*").strip() for x in content]
stacks = [[] for i in range(9)]

# Fill stacks
for i in content:
    if i.startswith("*1"):
        break

    i = "**" + i + "**"
    index_next_letter = 0
    for c in i:
        if c != "*":
            stack_number = index_next_letter//4 + 1
            stacks[stack_number-1].append(c)
        index_next_letter += 1

# Part 1
for act in content:
    if not act.startswith("move*"):
        continue
    
    act_split = act.split("*")
    how_many = int(act_split[1])
    from_stack = int(act_split[3])
    to_stack = int(act_split[5])

    stacks[to_stack-1] = stacks[from_stack-1][:how_many][::-1] + stacks[to_stack-1]
    stacks[from_stack-1] = stacks[from_stack-1][how_many:]

for stack in stacks:
    print(stack[0])

# Part 2
for act in content:
    if not act.startswith("move*"):
        continue
    
    act_split = act.split("*")
    how_many = int(act_split[1])
    from_stack = int(act_split[3])
    to_stack = int(act_split[5])

    stacks[to_stack-1] = stacks[from_stack-1][:how_many] + stacks[to_stack-1]
    stacks[from_stack-1] = stacks[from_stack-1][how_many:]

for stack in stacks:
    print(stack[0])