with open('./advent11.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

monkeys = {}

current_monkey = 0
for line in content:
    if line.startswith("Monkey"):
        current_monkey = int(line.split(" ")[1].split(":")[0])
        monkeys[current_monkey] = {}
    if line.startswith("Starting items"):
        monkeys[current_monkey]["items"] = [int(nb) for nb in line.split("Starting items: ")[1].split(", ")]
    if line.startswith("Operation"):
        monkeys[current_monkey]["operation"] = " ".join(line.split("Operation: ")[1].split(" ")[2:])
    if line.startswith("Test"):
        monkeys[current_monkey]["test"] = int(line.split("Test: ")[1].split(" ")[2])
    if line.startswith("If true"):
        monkeys[current_monkey]["if_true"] = int(line.split("If true: throw to monkey ")[1])
    if line.startswith("If false"):
        monkeys[current_monkey]["if_false"] = int(line.split("If false: throw to monkey ")[1])
        monkeys[current_monkey]["inspect_counter"] = 0


# Part 1

for round in range(20):
    for i in range(len(monkeys)):
        current_monkey = monkeys[i]
        for item in current_monkey["items"]:
            current_monkey["inspect_counter"] += 1

            new_worry_lvl = eval(current_monkey["operation"].replace("old", str(item)))
            new_worry_lvl = new_worry_lvl // 3

            if new_worry_lvl % current_monkey["test"] == 0:
                monkeys[current_monkey["if_true"]]["items"].append(new_worry_lvl)
            else:
                monkeys[current_monkey["if_false"]]["items"].append(new_worry_lvl)
        
        monkeys[i]["items"] = []

# print all monkeys inspect_counter
counters = [monkeys[i]["inspect_counter"] for i in range(len(monkeys))]
counters.sort(reverse=True)
# multiply the first two counters
print(counters[0] * counters[1])


# Part 2

current_monkey = 0
test_values_product = 1
for m in monkeys:
    test_values_product *= monkeys[m]["test"]

for round in range(10000):
    for i in range(len(monkeys)):
        current_monkey = monkeys[i]
        for item in current_monkey["items"]:
            current_monkey["inspect_counter"] += 1
            
            new_worry_lvl = eval(current_monkey["operation"].replace("old", str(item)))
            new_worry_lvl = new_worry_lvl % test_values_product

            if new_worry_lvl % current_monkey["test"] == 0:
                monkeys[current_monkey["if_true"]]["items"].append(new_worry_lvl)
            else:
                monkeys[current_monkey["if_false"]]["items"].append(new_worry_lvl)

        monkeys[i]["items"] = []

# print all monkeys inspect_counter
counters = [monkeys[i]["inspect_counter"] for i in range(len(monkeys))]
counters.sort(reverse=True)
# multiply the first two counters
print(counters[0] * counters[1])
