with open('./advent4.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

# Part 1

sum = 0
for i in content:
    range1_str = i.split(",")[0]
    range2_str = i.split(",")[1]
    range1 = [j for j in range(int(range1_str.split("-")[0]), int(range1_str.split("-")[1])+1)]
    range2 = [k for k in range(int(range2_str.split("-")[0]), int(range2_str.split("-")[1])+1)]
    union = set(range1).union(set(range2))
    if len(list(union)) == len(range1) or len(list(union)) == len(range2):
        sum += 1

print(sum)

# Part 2

sum = 0
for i in content:
    range1_str = i.split(",")[0]
    range2_str = i.split(",")[1]
    range1 = [j for j in range(int(range1_str.split("-")[0]), int(range1_str.split("-")[1])+1)]
    range2 = [k for k in range(int(range2_str.split("-")[0]), int(range2_str.split("-")[1])+1)]
    inter = set(range1).intersection(set(range2))
    if inter:
        sum += 1

print(sum)
