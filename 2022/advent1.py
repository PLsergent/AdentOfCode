# read file content advent1.txt

# read file content
with open('./advent1.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

# Part 1
sums = []

current_sum = 0
for i in content:
    if i == '':
        sums.append(current_sum)
        current_sum = 0
    else:
        current_sum += int(i)
sums.append(current_sum)

sums.sort(reverse=True)
print(sums[0])

# Part 2
print(sums[0] + sums[1] + sums[2])

