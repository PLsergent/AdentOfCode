with open('./day2.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

# Part 1

bag_max = {"red": 12, "green": 13, "blue": 14}

sum_id = 0
for game in content:
    game_possible = True
    game_id = int(game.split(":")[0].split(" ")[1])
    draws = game.split(":")[1].split(";")
    for draw in draws:
        cubes = draw.split(",")
        for cube in cubes:
            _, number, color = cube.split(" ")
            if bag_max[color] < int(number):
                game_possible = False
                break
    if game_possible:
        sum_id += game_id

print(sum_id)

# Part 2

sum_power = 0
for game in content:
    bag_max = {"red": 0, "green": 0, "blue": 0}
    game_id = int(game.split(":")[0].split(" ")[1])
    draws = game.split(":")[1].split(";")
    for draw in draws:
        cubes = draw.split(",")
        for cube in cubes:
            _, number, color = cube.split(" ")
            if bag_max[color] < int(number):
                bag_max[color] = int(number)
    power = 1
    for color, max in bag_max.items():
        power *= max
    sum_power += power

print(sum_power)