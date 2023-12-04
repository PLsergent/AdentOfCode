with open('./day3.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

# Part 1

symbols = ["*", "$", "+", "#", "%", "@", "-", "/", "=", "&"]

def find_adjacent_symbol(x, y):
    adjacent = []
    content_grid = []
    for line in content:
        splited = list(line)
        content_grid.append(splited)

    if x - 1 > 0:
        adjacent.append(content_grid[y][x-1])
    if y - 1 > 0:
        adjacent.append(content_grid[y-1][x])
    if y - 1 > 0 and x - 1 > 0:
        adjacent.append(content_grid[y-1][x-1])
    
    if x + 1 < len(content_grid[0]):
        adjacent.append(content_grid[y][x+1])
    if y + 1 < len(content_grid):
        adjacent.append(content_grid[y+1][x])
    if y + 1 < len(content_grid) and x + 1 < len(content_grid[0]):
        adjacent.append(content_grid[y+1][x+1])
    
    if x + 1 < len(content_grid[0]) and y - 1 > 0:
        adjacent.append(content_grid[y-1][x+1])
    if y + 1 < len(content_grid[0]) and x - 1 > 0:
        adjacent.append(content_grid[y+1][x-1])
    
    return adjacent

part_numbers = []

y = -1
for line in content:
    y += 1
    replaced = line.replace("*", ".").replace("#", ".").replace("+", ".").replace("$", ".").replace("%", ".").replace("/", ".").replace("=", ".").replace("-", ".").replace("@", ".").replace("&", ".")
    line_list = replaced.split(".")
    x = -1
    for elt in line_list:
        x += 1
        if elt != "" and elt not in symbols:
            total_adj = []
            for digit in elt:
                adj = find_adjacent_symbol(x, y)
                total_adj += adj
                x += 1
            for adj in total_adj:
                if adj in symbols:
                    part_numbers.append(int(elt))
                    break

print(sum(part_numbers))

# Part 2

def find_adjacent_gears(x, y):
    adjacent = []
    content_grid = []
    for line in content:
        splited = list(line)
        content_grid.append(splited)

    if x - 1 > 0:
        adjacent.append((content_grid[y][x-1], (x-1, y)))
    if y - 1 > 0:
        adjacent.append((content_grid[y-1][x], (x, y-1)))
    if y - 1 > 0 and x - 1 > 0:
        adjacent.append((content_grid[y-1][x-1], (x-1, y-1)))
    
    if x + 1 < len(content_grid[0]):
        adjacent.append((content_grid[y][x+1], (x+1, y)))
    if y + 1 < len(content_grid):
        adjacent.append((content_grid[y+1][x], (x, y+1)))
    if y + 1 < len(content_grid) and x + 1 < len(content_grid[0]):
        adjacent.append((content_grid[y+1][x+1], (x+1, y+1)))
    
    if x + 1 < len(content_grid[0]) and y - 1 > 0:
        adjacent.append((content_grid[y-1][x+1], (x+1, y-1)))
    if y + 1 < len(content_grid[0]) and x - 1 > 0:
        adjacent.append((content_grid[y+1][x-1], (x-1, y+1)))
    
    return adjacent

y = -1
gears = {}
gear_ratios = 0
for line in content:
    y += 1
    replaced = line.replace("*", ".").replace("#", ".").replace("+", ".").replace("$", ".").replace("%", ".").replace("/", ".").replace("=", ".").replace("-", ".").replace("@", ".").replace("&", ".")
    line_list = replaced.split(".")
    x = -1
    for elt in line_list:
        x += 1
        if elt != "" and elt not in symbols:
            total_adj = []
            for digit in elt:
                adj = find_adjacent_gears(x, y)
                total_adj += adj
                x += 1
            for symb, coord in total_adj:
                if symb == "*":
                    if coord in gears:
                        gears[coord].append(int(elt))
                    else:
                        gears[coord] = [int(elt)]
                    break

for coord, numbers in gears.items():
    if len(numbers) == 2:
        gear_ratios += numbers[0] * numbers[1]

print(gear_ratios)