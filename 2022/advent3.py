with open('./advent3.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

# part 1

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = alphabet + alphabet.upper()

sum = 0
for i in content:
    first_rack = i[:len(i)//2]
    second_rack = i[len(i)//2:]
    common = set(first_rack).intersection(set(second_rack))
    sum += alphabet.index(list(common)[0]) + 1

print(sum)

# part 2

sum = 0
for i in range(0, len(content), 3):
    first_row = content[i]
    second_row = content[i+1]
    third_row = content[i+2]
    common = set(first_row).intersection(set(second_row)).intersection(set(third_row))
    sum += alphabet.index(list(common)[0]) + 1

print(sum)