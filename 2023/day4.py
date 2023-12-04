with open('./day4.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

numbers = [line.split(": ")[1] for line in content]

# Part 1

def count_points(cards):
    if len(cards) == 0:
        return 0
    if len(cards) == 1:
        return 1
    points = 0
    for c in cards:
        if points >= 1:
            points *= 2
        else:
            points += 1
    return points

points = 0

for line in numbers:
    card_points = []
    winning_numbers = line.split("|")[0]
    my_numbers = line.split("|")[1]
    winning_numbers.strip()
    my_numbers.strip()
    for win in winning_numbers.split(" "):
        if win != "" and win != " ":
            for mine in my_numbers.split(" "):
                if mine != "" and mine != " ":
                    if win == mine:
                        card_points.append(int(win))
    points += count_points(card_points)

print(points)

# Part 2

copies = {}
sum_copies = 0
for index, line in enumerate(numbers):
    card_matching_count = 0
    winning_numbers = line.split("|")[0]
    my_numbers = line.split("|")[1]
    winning_numbers.strip()
    my_numbers.strip()
    for win in winning_numbers.split(" "):
        if win != "" and win != " ":
            for mine in my_numbers.split(" "):
                if mine != "" and mine != " ":
                    if win == mine:
                        card_matching_count += 1

    for copy in range(index+2, card_matching_count+index+2):
        if copy in copies:
            if index+1 in copies:
                copies[copy] += 1 + copies[index+1]
            else:
                copies[copy] += 1
        else:
            if index+1 in copies:
                copies[copy] = 1 + copies[index+1]
            else:
                copies[copy] = 1

for copy, count in copies.items():
    sum_copies += count

print(sum_copies+len(numbers))
