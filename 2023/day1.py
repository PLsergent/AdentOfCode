with open('./day1.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

# Part 1
# numbers = "1234567890"
# total = 0
# for line in content:
#     line_numbers = []
#     for i in line:
#         if i in numbers:
#             line_numbers.append(i)

#     total += int(line_numbers[0] + line_numbers[-1])

# print(total)

# Part 2
numbers_spelled = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# list of numbers spelled out with last letter equal to first letter of another number
combinaison = ["zerone", "twone", "oneight", "eightwo", "eightree", "nineight", "sevenine", "threeight", "fiveight"]
combinaison_numbers = ["01", "21", "18", "82", "83", "98", "79", "38", "58"]
numbers = "0123456789"

total = 0
for line in content:
    for i in combinaison:
        line = line.replace(i, combinaison_numbers[combinaison.index(i)])
    for i in numbers_spelled:
        line = line.replace(i, numbers[numbers_spelled.index(i)])
    line_numbers = []
    for i in line:
        if i in numbers:
            line_numbers.append(i)
    print(line_numbers)
    total += int(line_numbers[0] + line_numbers[-1])

print(total)